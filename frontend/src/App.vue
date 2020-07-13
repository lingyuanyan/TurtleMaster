<template>
  <div id="app">
    <Banner msg="Welcome to Your Vue.js App" />
    <TopLine />
    <DataList />
    <Information />
    <Post />
    <Footer />
  </div>
</template>

<script>
import Banner from "./components/banner.vue";
import TopLine from "./components/topline.vue";
import DataList from "./components/datalist.vue";
import Information from "./components/information.vue";
import Post from "./components/post.vue";
import Footer from "./components/footer.vue";

export default {
  name: "App",
  components: {
    Banner,
    TopLine,
    DataList,
    Information,
    Post,
    Footer
  }
};
</script>

<style>
</style>
