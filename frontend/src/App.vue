<template>
  <div id="app">
    <Banner msg="Welcome to Your Vue.js App" />
<<<<<<< HEAD
    <TopLine />
    <DataList />
    <Information />
=======
    <Information />
    <TopLine />
    <DataList />
>>>>>>> 38151d5a07194a438cdf4c9d4ea29c22aa81f9fe
    <Footer />
  </div>
</template>

<script>
import Banner from "./components/banner.vue";
import TopLine from "./components/topline.vue";
import Information from "./components/information.vue";
import DataList from "./components/datalist.vue";
import Footer from "./components/footer.vue";

export default {
  name: "App",
  components: {
    Banner,
    TopLine,
    DataList,
    Information,
    Footer
  }
};
</script>

<style>
#app {
  background-color: #cafbb6;
  padding-bottom: 15px;
}
</style>
