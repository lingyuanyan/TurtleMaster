<template>
  <div class="banner">
    <h1>Welcome to TurtleMaster</h1>
    <img
      src="../assets/lmc_logo.jpg"
      alt="Little Master's Club Logo"
      width="50px"
      height="50px"
    />
    <img
      src="../assets/turtlemaster_logo.jpg"
      alt="TurtleMaster Logo"
      width="50px"
      height="50px"
      class="tm_logo"
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
img[src="../assets/lmc_logo.jpg"] {
  position: fixed;
  right: 15px;
  top: 15px;
}
img[src="../assets/turtlemaster_logo.jpg"] {
  position: fixed;
  left: 15px;
  top: 15px;
}
.active {
  background-color: #5f4238;
}
a:hover{
  background-color:#8b6152
}
nav a {
  text-decoration: none;
  border-radius: 12px;
  padding: 5px;
  display: inline;
  margin-top: 3px;
  margin-left: auto;
  margin-right: auto;
  top: 5px;
  background-color: #4a810c;
  text-align: center;
  font-family: cursive;
  color: white;
}
nav {
  position: relative;
  text-align: center;
  bottom: 12px;
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
  top: 2px;
}
</style>
