<template>
  <div class="banner">
    <div class="title" id="title">
      <h1>CovidHub</h1>
    </div>
    <div class="menu-bar">

    </div>
    <div class="icon-bar">
      <img src="../assets/lmc_logo.jpg" alt="Little Master's Club Logo" width="50px" height="50px"
        class="little_masters_logo" />
      <img src="../assets/TurtleMaster_Logo.png" alt="TurtleMaster Logo" width="50px" height="50px"
        class="turtle_master_logo" />
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
<style scoped>
.little_masters_logo {
  position: fixed;
  right: 15px;
  top: 15px;
}

.turtle_master_logo {
  position: fixed;
  left: 15px;
  top: 15px;
}

.banner {
  /* nav */


  /* Auto layout */

  display: flex;
  flex-direction: row;
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
  top: 0px;
  left: 0px;
  height: 75px;
}

.title {
  /* CovidHub */


  width: 156px;
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

.mene-bar {}
</style>
