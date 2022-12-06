<template>
  <div id="topline" class="topline">
    <div class="topline-subtitle">
      <label for="live-tracker-select" class="topline-subtitle-text">Covid-19 Live Tracker</label>
      <select name="live-tracker-select" id="live-tracker-select" class="live-tracker-select"
        v-model="current_live_tracker" @change="onLiveTrackerSelected">
        <option class="live-tracker-select-option" v-for="(option, i) in live_tracker_options" v-bind:value="option"
          :key="i">{{ option }}</option>
      </select>
    </div>
    <div class="information-board">
      <div class="total-confirmded-board">
        <div class="total-confirmded-board-number-box">
          <p class="total-confirmded-board-number">{{ Number(total_confirmed).toLocaleString() }}</p>
        </div>
        <div class="total-confirmded-board-title-box">
          <p class="total-confirmded-board-title">Total Confirmed</p>
        </div>
      </div>
      <div class="total-recovered-board">
        <div class="total-recovered-board-number-box">
          <p class="total-recovered-board-number">{{ Number(total_recovered).toLocaleString() }}</p>
        </div>
        <div class="total-recovered-board-text-box">
          <p class="total-recovered-board-text">Total Recovered</p>
        </div>

      </div>
      <div class="total-death-board">
        <div class="total-death-board-number-box">
          <p class="total-death-board-number">{{ Number(total_dead).toLocaleString() }}</p>
        </div>
        <div class="total-death-board-text-box">
          <p class="total-death-board-text">Total Deaths</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import covidhubAxios from "./axios-ins";

export default {
  name: "TopLine",
  props: {},

  data() {
    return {
      topline_json: null,
      current_live_tracker: "US",
      trending_chart_width: 300,
      total_confirmed: 0,
      total_recovered: 0,
      total_dead: 0,
      time_series_us_json: null,
      time_serise_us_states: [],
      live_tracker_options: [],
      trending_chart_height: 400,
      current_state: "Washington",
    };
  },
  created() { },
  mounted() {
    this.fetchTopline();
    //    this.fetchTimeSeriesUsStates();
  },
  methods: {

    updateLiveTracker() {
      this.topline_json.forEach((element) => {
        if (element.country_region == this.current_live_tracker) {
          this.total_confirmed = element.confirmed;
          this.total_recovered = element.recovered,
            this.total_dead = element.deaths
        }
      })
    },
    fetchTopline() {
      covidhubAxios
        .get("/api/ViewStatisticsData/")
        .then((response) => (
          this.topline_json = response.data.results,
          this.live_tracker_options.length = 0,
          this.topline_json.forEach((element) => {
            this.live_tracker_options.push(element.country_region);
          }),
          this.updateLiveTracker()
        )
        )
        .catch((error) => console.log(error));
    },

    onLiveTrackerSelected() {
      this.updateLiveTracker()
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.topline {
  width: 100%;
  @extend .my-3;
}

.topline-subtitle {
  @extend .d-flex;
  @extend .justify-content-start;
  width: 90%;
  @extend .mx-auto;
}

.topline-subtitle-text {
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

.live-tracker-select {
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

.live-tracker-select-option {
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

.information-board {
  @extend .d-flex;
  @extend .justify-content-center;
  width: 90%;
  @extend .mx-auto;
  @extend .my-2;
}

.total-confirmded-board {
  width: 30%;
  @extend .mx-auto;

  @extend .d-flex;
  @extend .flex-column;
}

.total-confirmded-board-number-box {
  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  width: 100%;
  background: #FFE6D5;
  border-radius: 8px 8px 0px 0px;

  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.total-confirmded-board-title-box {

  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  width: 100%;

  background: #FFD3B3;
  border-radius: 0px 0px 8px 8px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.total-confirmded-board-number {
  /* Display | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height */

  text-transform: capitalize;

  /* Key colors/Orange */

  color: #FF832B;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.total-confirmded-board-title {

  /* Title 3 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-transform: capitalize;

  /* Key colors/Orange */

  color: #FF832B;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.total-recovered-board {
  width: 30%;
  @extend .mx-auto;
}

.total-recovered-board-number-box {
  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  background: #EAFAEE;
  border-radius: 8px 8px 0px 0px;

  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.total-recovered-board-number {
  /* Display | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height */

  text-transform: capitalize;

  /* Key colors/Green */

  color: #198038;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.total-recovered-board-text-box {

  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  background: #C1F0CE;
  border-radius: 0px 0px 8px 8px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.total-recovered-board-text {

  /* Title 3 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-transform: capitalize;

  /* Key colors/Green */

  color: #198038;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.total-death-board {
  width: 30%;
  @extend .mx-auto;
}

.total-death-board-number-box {
  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  /* Neutral/Gray01 */

  background: #F8F8F8;
  border-radius: 8px 8px 0px 0px;

  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.total-death-board-number {
  /* Display | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height */

  text-transform: capitalize;

  /* Neutral/Gray04 */

  color: #777777;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.total-death-board-text-box {
  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  /* Neutral/Gray02 */

  background: #E5E5E5;
  border-radius: 0px 0px 8px 8px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.total-death-board-text {
  /* Title 3 | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-transform: capitalize;

  /* Neutral/Gray04 */

  color: #777777;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

table {
  background-color: #c4dbaa;
  float: right;

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

.th {
  font-size: 20px;
}

td,
th {
  border: 1px solid #8bc34a;
}

tr:hover {
  background-color: #bccd12;
}

.white {
  height: 80px;
}

#placeholder {
  height: 60px;
}
</style>
