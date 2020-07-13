<template>
  <div class="topline">
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

export default {
  name: "TopLine",
  props: {},

  data() {
    return {
      topline_json: "",
      time_series_us_json: ""
    };
  },
  created() {
    this.fetchTopline();
    this.fetchTimeSeriesUs();
  },
  methods: {
    fetchTopline() {
      covidhubAxios
        .get("/api/ViewStatisticsData/")
        .then(response => (this.topline_json = response.data.results))
        .catch(error => console.log(error));
    },
    fetchTimeSeriesUs() {
      covidhubAxios
        .get("/api/TimeSeriesDataUs/")
        .then(response => (this.time_series_us_json = response.data.results))
        .catch(error => console.log(error));
    }
  }
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
