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
    }
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
