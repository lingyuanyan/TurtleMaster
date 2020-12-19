<template>
  <div class="footer">
    Made by the TurtleMaster Group<br />
    Other sites on health
    <ul>
      <li><a href="https://www.cdc.gov/" target="_blank">cdc.gov</a></li>
    </ul>
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

.footer{
  font-family: cursive;
  border: 5px double #c4dbaa;
}
</style>
