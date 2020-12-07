<template>
  <div class="footer">
    <p>More sites on Covid-19</p>
    <a href="https://www.cdc.gov/coronavirus/2019-ncov
">CDC.gov</a>
<a href="https://coronavirus.jhu.edu/map.html">Johns Hopkins</a>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

footer{
  background-color:#00aeff;
  border:1px solid #00aeff;
  font-family: cursive;
  bottom: 0px;
}
</style>
