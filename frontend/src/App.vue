<template>
  <div class="app-body">
    <header class="body-header">
      <router-view name="header"></router-view>
    </header>
    <div class="warning">
      All the data for the Recovered Sections are empty since we have not not found a suitable source to gather that data. We apoligize if this causes any inconvienence,
    </div>
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
.warning {
  width: 100%;
  background-color: rgb(235, 95, 95);
  border: 3px rgb(253, 155, 155);
}
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
  background: #1CB0F6;
}
.body-main {
  margin-top: 0px;
  width: 100%;
}
.body-footer {
  width: 100%;
  background: #222222;
}
.app-body {
  margin-top: 0px;
  width: 100%;
}
</style>
