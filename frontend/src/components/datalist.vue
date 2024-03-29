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

    formatYAxixTick(d) {
      const s = (d / 1e6).toFixed(1);
      return `${s} M`;
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
      var minDate = new Date(); // the current time
      var maxDate = new Date(2000, 1, 1); // the date earler than 2020,1,1 will be fine

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
        var last_update = new Date(data[len].last_update);
        if (last_update < minDate) {
          minDate = last_update;
        }
        if (last_update > maxDate) {
          maxDate = last_update;
        }
      }

      const axisMargin = {
        left: Math.max(50, w * 0.10),
        top: Math.max(10, h * 0.1),
        right: Math.min(w - 50, w * 0.9),
        bottom: Math.min(h - 20, h * 0.9)
      }; // Make some empty space around your x axis using margin
      const colorOfConfirmed = '#6FDC8C';
      const colorOfDeath = '#AFAFAF';

      var xScale = d3.scaleTime().domain([0, n]).range([axisMargin.left, axisMargin.right]);
      var xAxiScale = d3.scaleTime().domain([minDate, maxDate]).range([axisMargin.left, axisMargin.right]);
      var yScaleConfirmed = d3.scaleLinear().domain([minConfirmed, maxConfirmed]).range([axisMargin.bottom, axisMargin.top]);
      var yScaleDeaths = d3.scaleLinear().domain([minDeaths, maxDeaths]).range([axisMargin.bottom, axisMargin.top]);
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
          .attr("stroke", colorOfConfirmed)
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
          .attr("stroke", colorOfDeath)
          .attr("stroke-width", 2)
          .attr("fill", "none");
      }


      var xAxis = svg.append('g').call(d3.axisBottom(xAxiScale));
      if (!xAxis.empty()) {
        xAxis
          .attr("class", "axis")
          .attr("transform", "translate(0," + axisMargin.bottom + ")");

      }

      var yAxisConfirmed = svg.append('g').call(d3.axisLeft(yScaleConfirmed).ticks(5).tickFormat(this.formatYAxixTick));
      if (!yAxisConfirmed.empty()) {
        yAxisConfirmed
          .attr("class", "axis")
          .attr("transform", "translate(" + axisMargin.left + ",0)")
          .attr("stroke", colorOfConfirmed)
          .attr("stroke-width", 1)
          .attr("fill", "none");
      }

      var yAxisDeaths = svg.append('g').call(d3.axisRight(yScaleDeaths).ticks(5).tickFormat(this.formatYAxixTick));
      if (!yAxisDeaths.empty()) {
        yAxisDeaths
          .attr("class", "axis")
          .attr("transform", "translate(" + axisMargin.right + ",0)")
          .attr("stroke", colorOfDeath)
          .attr("stroke-width", 1)
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
