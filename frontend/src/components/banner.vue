<template>
  <div class="banner">
    <div id = "title">
      <h1>Welcome to TurtleMaster</h1>
    </div>
    <img
      src="../assets/lmc_logo.jpg"
      alt="Little Master's Club Logo"
      width="50px"
      height="50px"
      class="little_masters_logo"
    />
    <img
      src="../assets/TurtleMaster_Logo.png"
      alt="TurtleMaster Logo"
      width="50px"
      height="50px"
      class="turtle_master_logo"
    />
  </div>
</template>
<script>
export default {
  name: "Banner",
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
  position: fixed;
  background-color: #97d64e;
  border: 3px solid #8bc34a;
  width: 100%;
  top: 0px;
  left: 0px;
  height: 75px;
}
h1 {
  text-align: center;
  height:40px;
}
nav a {
  background-color: #4a810c;
  border-radius: 15%;
  color: #a1c891;
  border-radius: 100%;
  -webkit-border-radius: 100%;
  -moz-border-radius: 100%;
  width: 25%;
  padding: 0.5%;
}

nav {
  text-align: center;
  height: 30px;
}
</style>
