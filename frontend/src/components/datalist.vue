<template>
<div class="datalist">
  <table>
    <tr>
      <th class="th">Location</th>
      <th class="th">Confirmed</th>
      <th class="th">Deaths</th>
      <th class="th">Recovered</th>
      <th class="th">Last Update</th>
    </tr>
    <tr>
      <th>US</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr v-for="record in us_satistics_json" :key="record.province_state">
      <td>{{ record.province_state }}-</td>
      <td>confirmed {{record.confirmed}},</td>
      <td>deaths {{record.deaths}},</td>
      <td>recovered {{record.recovered}}</td>
      <td>Last Update {{record.last_update}}</td>
    </tr>
    <tr>
      <th>World</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr v-for="record in world_statistics_json" :key="record.province_state">
      <td>{{ record.country_region }}-{{ record.province_state }}-</td>
      <td>confirmed {{record.confirmed}},</td>
      <td>deaths {{record.deaths}},</td>
      <td>recovered {{record.last_update}}</td>
      <td>Last Update {{record.last_update}}</td>
    </tr>
  </table>
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
      us_satistics_json: "",
      world_statistics_json: ""
    };
  },
  created() {
    this.fetchUsStatics();
    this.fetchWorldStatics();
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
<style scoped>
table {
  background-color: #c4dbaa;
  top: 50px;
  margin: auto;
}
</style>