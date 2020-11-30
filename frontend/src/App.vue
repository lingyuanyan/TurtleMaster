<template>
  <div id="app">
    <header>
      <Banner msg="Welcome to Your Vue.js App" />
    </header>
    <main>
      <TopLine />
      <DataList />
      <Information />
    </main>
    <footer>
      <Footer />
    </footer>
  </div>
</template>

<script>
import Banner from "./components/banner.vue";
import TopLine from "./components/topline.vue";
import DataList from "./components/datalist.vue";
import Information from "./components/information.vue";
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
}
</style>
