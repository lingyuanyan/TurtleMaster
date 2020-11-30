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
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Great+Vibes&display=swap');
.footer{
  background: #20f030;
  border: 5px groove #659274;
  font-family: 'Dancing Script', 'Great Vibes', cursive, serif, monospace, sans-serif;
  position: absolute;
  bottom: 0px;
  width: 100%;
  left: 0px;
}
</style>
