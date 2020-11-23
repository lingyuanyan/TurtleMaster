<template>
  <div class="footer">
    <img alt="TurtleMaster Logo" class="game-link" />Here is a game you can play <a href="">Monster Slayer</a>
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
  border: 5px groove #38f576;
  font-family: 'Dancing Script', 'Great Vibes', cursive, fantasy, serif, monospace, sans-serif;
  position: absolute;
  bottom: 0px;
  width: 100%;
  left: 0px;
}

.game-link {
  color: #4040ff;
  text-decoration: none;
}

.game-link:hover, .game-link:focus {
  color: #0000bf;
  text-decoration: underline;
}
</style>
