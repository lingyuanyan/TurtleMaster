<template>
  <div class="footer">
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
  background: #20f030;
  border:1px solid #008000;
  font-family: cursive;
  position:fixed;
  bottom: 0px;
  width: 100%;
  left: 0px;
}
</style>
