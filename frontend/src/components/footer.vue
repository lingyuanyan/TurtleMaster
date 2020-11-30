<template>
  <div class="footer">
    Stay safe from COVID-19
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
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Great+Vibes&display=swap');
.footer{
  background: #20f030;
  border: 5px groove #5eac64;
  font-family: 'Dancing Script', 'Great Vibes', cursive, serif, monospace, sans-serif;
  width: 100%;
  position: fixed;
  bottom: 0px;
  left: 0px;
  text-align: center;
}
</style>
