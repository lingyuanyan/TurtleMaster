<template>
  <div id="toplineContainer" class="topline">
    <table>
      <tr v-for="record in topline_json" :key="record.country_region">
        <td>{{record.country_region}} -</td>
        <td>confirmed {{record.confirmed}},</td>
        <td>deaths {{record.deaths}},</td>
        <td>recovered {{record.recovered}}</td>
        <td>Last Update {{record.last_update}}</td>
      </tr>
    </table>
    <table>
      <tr v-for="record in time_series_us_json" :key="record.country_region">
        <td>{{ record.country_region }}-</td>
        <td>state {{record.province_state}},</td>
        <td>confirmed {{record.confirmed}},</td>
        <td>deaths {{record.deaths}},</td>
        <td>Last Update {{record.last_update}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import covidhubAxios from "./axios-ins";
import * as d3 from "d3";

export default {
  name: "TopLine",
  props: {},

  data() {
    return {
      topline_json: null,
      time_series_us_json: null,
      time_serise_us_states:null,
      trending_chart_width: 300,
      trending_chart_height: 400,
    };
  },
  created() {
  },
  mounted(){
    this.fetchTopline();
    this.fetchTimeSeriesUs("Florida");

  },
  methods: {

    fetchTopline() {
      covidhubAxios
        .get("/api/ViewStatisticsData/")
        .then(response => (this.topline_json = response.data.results))
        .catch(error => console.log(error));
    },

    fetchTimeSeriesUs(province_state) {
      covidhubAxios
        .get("/api/TimeSeriesDataUs/?province_state="+province_state)
        .then(response => (
          this.time_series_us_json = response.data.results, 
          this.buildTrendingChart()
          ))
        .catch(error => console.log(error));
    },

    fetchTimeSeriesUsStates() {
      covidhubAxios
        .get("/api/TimeSeriesDataUs/?distinct_on=province_state")
        .then(response => (
          this.time_serise_us_states = response.data.results, 
          this.buildTrendingChart()
          ))
        .catch(error => console.log(error));
    },

    buildTrendingChart() {
      var w = this.trending_chart_width;
      var h = this.trending_chart_height;
      
      var data = this.time_series_us_json;
      var n = data.length;
      var containerId = "#toplineContainer";
      console.log(data);
      console.log(n);
      var lineFun = d3.line()
                          .x((d, i) => {console.log(d,i); return w * i / n;})
                          .y((d) => {return h - d.confirmed;})
                          .curve(d3.curveLinear);
      console.log(lineFun(data));
      var svg = d3.select(containerId)
                            .append("svg")
                            .attr("width", w)
                            .attr("height", h);

      // eslint-disable-next-line no-unused-vars                    
      var vix = svg.append("path")
                            .attr("d", lineFun(data))
                            .attr("stroke", "purple")
                            .attr("stroke-width", 2)
                            .attr("fill", "none");

      }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.topline {
  top: 75px;
}

table {
  background-color: #c4dbaa;
  top: 50px;
  margin: auto;
}
</style>
