<template>
  <div class="app-body">
    <header class="body-header">
      <router-view name="header"></router-view>
    </header>
    <main class="body-main">
      <router-view></router-view>
    </main>
    <footer class="body-footer">
      <router-view name="footer"></router-view>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  computed: {},
  methods: {},
  created() {
  }
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.body-header {
  width: 100%;
  height: 5vmax;
  background: #1CB0F6;
}
.body-main {
  margin-top: 0px;
  width: 100%;
  min-height: calc(100vh - 1vmax);
}
.body-footer {
  width: 100%;
  height: 5vmax;
  background: #222222;
}
.app-body {
  margin-top: 0px;
  width: 100%;
}
</style>
