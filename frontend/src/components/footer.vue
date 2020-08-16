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
  background-color:#0abf12;
  border:1px solid #64794d;
  font-family: cursive;
  position:fixed;
  bottom: 0px;
  width: 100%;
  left: 0px;
}
</style>
