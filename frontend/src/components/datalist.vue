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
    <div id="chart-container" ref="chartContainer" class="chart-container">
      <svg view-box="0,0,100,100">
        <path id="deaths" />
      </svg>
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
      world_statistics_json: "",
      time_series_json: "",
      trending_chart_width: 300,
      trending_chart_height: 300

    };
  },
  created() {
    this.fetchUsStatics();
    //this.fetchWorldStatics();
    this.fetchTimeSeriesByRegion(this.current_data_source)
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

    fetchTimeSeriesByRegion(country_region) {
      covidhubAxios
        .get("/api/ViewTimeSeriesStatisticsData/?country_region=" + country_region)
        .then(
          (response) => (
            (this.time_series_json = response.data.results),
            this.buildTrendingChart()
          )
        )
        .catch((error) => console.log(error));
    },

    buildTrendingChart() {
      var w = this.$refs.chartContainer.clientWidth;
      var h = this.trending_chart_height;
      var data = this.time_series_json;
      var n = data.length;
      var containerId = "#chart-container";

      var maxConfirmed = 0;
      var minConfirmed = Infinity;
      var maxDeaths = 0;
      var minDeaths = Infinity;

      var len = data.length;
      while (len--) {
        if (data[len].confirmed < minConfirmed) {
          minConfirmed = data[len].confirmed;
        }
        if (data[len].deaths < minDeaths) {
          minDeaths = data[len].deaths;
        }
        if (data[len].confirmed > maxConfirmed) {
          maxConfirmed = data[len].confirmed;
        }
        if (data[len].deaths > maxDeaths) {
          maxDeaths = data[len].deaths;
        }
      }


      var xScale = d3.scaleLinear().domain([0, n]).range([10, w]);
      var yScaleConfirmed = d3.scaleLinear().domain([minConfirmed, maxConfirmed]).range([h, 0]);
      var yScaleDeaths = d3.scaleLinear().domain([minDeaths, maxDeaths]).range([h, 0]);
      var lineConfirmed = d3
        .line()
        .x((d, i) => {
          return xScale(i);
        })
        .y((d) => {
          return yScaleConfirmed(Number(d.confirmed));
        })
        .curve(d3.curveLinear);

      var lineDeaths = d3
        .line()
        .x((d, i) => {
          return xScale(i);
        })
        .y((d) => {
          return yScaleDeaths(Number(d.deaths));
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
      if (!confirmedVix.empty()) {
        confirmedVix
          .attr("d", lineConfirmed(data))
          .attr("stroke", "blue")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      }
      // eslint-disable-next-line no-unused-vars
      var deathsVix = svg.select("#deaths");
      if (deathsVix.empty()) {
        deathsVix = svg.append("path");
        deathsVix.attr("id", "deaths");
      }

      if (!deathsVix.empty()) {
        deathsVix
          .attr("d", lineDeaths(data))
          .attr("stroke", "red")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      }
    },

    onCurrentDataSource() {
      this.fetchTimeSeriesByRegion(this.current_data_source)
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
