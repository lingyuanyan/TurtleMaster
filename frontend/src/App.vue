<template>
  <div id="app">
    <Banner msg="Welcome to Your Vue.js App" />
    <TopLine />
    <Information />
    <DataList />
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
    Information,
    DataList,
    Footer
  }
};
</script>

<style>
#app {
  background-color: #62a219;
  padding-bottom: 15px;
}
</style>
