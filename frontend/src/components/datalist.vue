<template>
  <div id="data-table" class="datalist">
    <div class="data-subtitle">
      <label for="data-table-select" class="data-subtitle-text">Data</label>
      <select name="data-table-select" id="data-table-select" class="data-table-select" v-model="current_data_source"
        @change="onCurrentDataSource">
        <option class="data-table-select-option" v-for="(option, i) in data_table_options" v-bind:value="option"
          :key="i">{{ option }}</option>
      </select>
    </div>
    <div id="chart" class="chart-container">
      <svg>
        <path id="deaths" />
      </svg>
      <select name="state" id="states" v-model="current_state" @change="onStateSelected">
        <option v-for="(option, i) in time_serise_us_states" v-bind:value="option" :key="i">{{ option }}</option>
      </select>
      <span>Selected: {{ current_state }}</span>
    </div>

    <div class="container">
      <div class="row">
        <div class="data-table-first-row">
          Location
        </div>
        <div class="data-table-first-row">
          Confirmed
        </div>
        <div class="data-table-first-row">
          Deaths
        </div>
        <div class="data-table-first-row">
          Recovered
        </div>
        <div class="data-table-first-row">
          Last Update
        </div>
      </div>
      <div class="row" v-for="record in us_satistics_json" :key="record.province_state">
        <div class="data-table-first-col">
          {{ record.province_state }}
        </div>
        <div class="data-table-col">
          {{ Number(record.confirmed).toLocaleString() }}
        </div>
        <div class="data-table-col">
          {{ Number(record.deaths).toLocaleString() }}
        </div>
        <div class="data-table-col">
          {{ Number(record.recovered).toLocaleString() }}
        </div>
        <div class="data-table-col">
          {{ record.last_update }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import covidhubAxios from "./axios-ins";

import * as d3 from "d3";
export default {
  name: "DataList",
  props: {
    msg: String
  },
  data() {
    return {
      data_table_options: ["US"],
      current_data_source: "US",
      us_satistics_json: "",
      world_statistics_json: ""
    };
  },
  created() {
    this.fetchUsStatics();
    //this.fetchWorldStatics();
  },
  methods: {
    fetchUsStatics() {
      covidhubAxios
        .get("/api/InfectionDataUsStatistics/")
        .then(response => (this.us_satistics_json = response.data.results))
        .catch(error => console.log(error));
    },
    fetchWorldStatics() {
      covidhubAxios
        .get("/api/InfectionDataWorldStatistics/")
        .then(response => (this.world_statistics_json = response.data.results))
        .catch(error => console.log(error));
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
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.data-table {
  width: 90%;
  @extend .mx-auto;
  /* Neutral/Background */

  background: #F5F7F9;

  /* Inside auto layout */

  flex: none;
  order: 3;
  align-self: stretch;
  flex-grow: 0;
}

.data-subtitle {
  @extend .d-flex;

  @extend .justify-content-start;
  width: 90%;
  @extend .mx-auto;
}

.data-subtitle-text {

  /* Title 1 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 29px;
  /* identical to box height */

  text-transform: capitalize;

  /* Neutral/Charcoal */

  color: #222222;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.data-table-select {

  @extend .mx-3;
  @extend .my-1;
  background: #1CB0F6;
  box-shadow: 2px 2px 22px rgba(229, 229, 229, 0.5);
  border-radius: 50px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}

.data-table-select-option {

  /* Global */
  /* Title 4 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 17px;
  /* identical to box height */

  text-transform: uppercase;

  /* Neutral/White */

  color: #FFFFFF;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}

.data-table-first-row {
  @extend .col;

  /* Title 3 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-transform: capitalize;

  /* Neutral/Charcoal */

  color: #222222;


  /* Inside auto layout */

  order: 0;
  @extend .my-3;
}

.data-table-first-col {

  @extend .col;

  /* Title 3 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-transform: capitalize;

  /* Neutral/Charcoal */

  color: #222222;


  /* Inside auto layout */
  order: 0;
}

.data-table-col {

  @extend .col;
}
</style>
