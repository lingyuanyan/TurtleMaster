<template>
  <div>
    <div id="topline">
    <div>
    <p id="placeholder"></p>
    <div id="toplineContainer" class="topline">
      <svg>
        <path id="deaths"/>
      </svg>
      <select name="state" id="states" v-model="current_state" @change="onStateSelected">
        <option
          v-for="(option,i) in time_serise_us_states"
          v-bind:value="option"
          :key="i"
        >{{ option }}</option>
      </select>
      <span>Selected: {{ current_state }}</span>
    </div>
    <table>
      <tr v-for="record in topline_json" :key="record.country_region">
        <td>{{record.country_region}} -</td>
        <td>confirmed {{record.confirmed}},</td>
        <td>deaths {{record.deaths}},</td>
        <td>recovered {{record.recovered}}</td>
        <td>Last Update {{record.last_update}}</td>
      </tr>
  </table>
</div>

  </div>
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
      time_serise_us_states: [],
      trending_chart_width: 300,
      trending_chart_height: 400,
      current_state: "Washington",
    };
  },
  created() {},
  mounted() {
    this.fetchTopline();
    this.fetchTimeSeriesUsStates();
  },
  methods: {
    fetchTopline() {
      covidhubAxios
        .get("/api/ViewStatisticsData/")
        .then((response) => (this.topline_json = response.data.results))
        .catch((error) => console.log(error));
    },

    fetchTimeSeriesUs(province_state) {
      covidhubAxios
        .get("/api/TimeSeriesDataUsByState/?province_state=" + province_state)
        .then(
          (response) => (
            (this.time_series_us_json = response.data.results),
            this.buildTrendingChart()
          )
        )
        .catch((error) => console.log(error));
    },

    fetchTimeSeriesUsStates() {
      covidhubAxios
        .get("/api/TimeSeriesDataUs/?distinct_on=province_state")
        .then(
          (response) => (
            response.data.results.forEach((element) => {
              this.time_serise_us_states.push(element.province_state);
            }),
            this.fetchTimeSeriesUs(this.current_state)
          )
        )
        .catch((error) => console.log(error));
    },

    buildTrendingChart() {
      var w = this.trending_chart_width;
      var h = this.trending_chart_height;

      var data = this.time_series_us_json;
      var n = data.length;
      var containerId = "#toplineContainer";

      var xScale = d3.scaleLinear().domain([0, n]).range([10, w]);
      var yScale = d3.scaleLinear().domain([0, 50000]).range([h, 0]);
      var lineConfirmed = d3
        .line()
        .x((d, i) => {
          return xScale(i);
        })
        .y((d) => {
          return yScale(d.confirmed);
        })
        .curve(d3.curveLinear);

      var lineDeaths = d3
        .line()
        .x((d, i) => {
          return xScale(i);
        })
        .y((d) => {
          return yScale(d.deaths);
        })
        .curve(d3.curveLinear);

      // eslint-disable-next-line no-unused-vars
      var svg = d3
        .select(containerId)
        .select("svg")
        .attr("width", w)
        .attr("height", h);

      // eslint-disable-next-line no-unused-vars
      var confirmedVix = svg.select("#confirmed");
      if (confirmedVix.empty()) {
        confirmedVix = svg.append("path");
        confirmedVix.attr("id", "confirmed");
      }
      confirmedVix
        .attr("d", lineConfirmed(data))
        .attr("stroke", "blue")
        .attr("stroke-width", 2)
        .attr("fill", "none");

      // eslint-disable-next-line no-unused-vars
      var deathsVix = svg.select("#deaths");
      if (deathsVix.empty()) {
        deathsVix = svg.append("path");
        deathsVix.attr("id", "deaths");
      }

      deathsVix
        .attr("d", lineDeaths(data))
        .attr("stroke", "red")
        .attr("stroke-width", 2)
        .attr("fill", "none");
    },
    onStateSelected() {
      this.fetchTimeSeriesUs(this.current_state);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#topline {

}
.topline {
  top: 275px;
  text-align: center;
}

table {
  background-color: #c4dbaa;
  float:right;

}
#toplineContainer {
  background-color: #E8E8E8;
  width: auto;
  text-align: center;
  border-radius: 15px/15px;
  border: 2px solid black;
  text-align: center;
}
#deaths {
  color: #f00;
}
.th{
  font-size: 20px;
}
td, th{
  border: 1px solid #8bc34a;
}
tr:hover{
  background-color:#bccd12;
}
.white {
  height: 80px;
}

#placeholder {
  height: 60px;
}
</style>
