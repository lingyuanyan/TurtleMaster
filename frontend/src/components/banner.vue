<template>
  <div class="banner">
    <div class="title" id="title">
      <h1>CovidHub</h1>
    </div>
    <div class="linkBox">
      <router-link class="routerLink" to="#" v-scroll-to="'#topline'">Home</router-link>
      <router-link class="routerLink" to="#" v-scroll-to="'#information'">Information</router-link>
      <router-link class="routerLink" to="#" v-scroll-to="'#data-table'">Data</router-link>
    </div>
    <div class="icon-bar">
      <div class="icon-container">
        <img src="../assets/lmc_logo.jpg" alt="Little Master's Club Logo" class="little_masters_logo" />
      </div>
      <div class="icon-container">
        <img src="../assets/TurtleMaster_Logo.png" alt="TurtleMaster Logo" class="turtle_master_logo" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "TopBanner",
  props: {
    msg: String
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.banner {
  /* nav */


  /* Auto layout */

  @extend .d-flex;
  @extend .justify-content-between;

  align-items: center;
  padding: 32px 88px;
  gap: 54px;


  /* Key colors/Dark Blue */

  background: #2B70C9;
  box-shadow: inset 0px -1px 0px #AFAFAF;

  /* Inside auto layout */

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;

  width: 100%;
  height: 108px;
}

.linkBox {
  @extend .d-flex;
  @extend .justify-content-between;
  width: 25%;
  @extend .mx-auto;
}

a {

  /* Title3 | Black */

  font-family: 'Nunito';
  font-style: normal;
  font-weight: 200;
  font-size: 21px;
  line-height: 36px;
  text-decoration: none;


  /* identical to box height, or 150% */
  text-align: center;

  /*padding*/
  @extend .mx-3;
  /* White */
  color: #FFFFFF;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

a:hover {
  color: #2B70C9;
}


.title {
  /* CovidHub */


  width: 15%;
  height: 39px;

  /* Display | Bold */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height */

  text-transform: capitalize;

  /* Neutral/White */

  color: #FFFFFF;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.icon-bar {
  @extend .d-flex;
  @extend .justify-content-end;
  width: 15%;
}

.icon-container {
  width: 40%;
  margin: auto;
}

.little_masters_logo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  overflow: hidden;
}

.turtle_master_logo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  overflow: hidden;
}
</style>
