<template>
  <div class="information">
    <section class="videos">
      <h1>Videos</h1>
      <a href="https://www.youtube.com/watch?v=n6QwnzbRUyA" target="_blank">click here to learn how to lower your risk of getting covid.</a><br/>
      <a href="https://www.youtube.com/watch?v=FVIGhz3uwuQ" target="_blank">click here to learn covid vs the flu.</a><br/>
      <a href="https://www.youtube.com/watch?v=r6ewlQs8CAQ" target="_blank">click here to learn what the US did wrong about testing covid.</a><br/>
      <a href="https://www.youtube.com/watch?v=-LKVUarhtvE" target="_blank">click here to learn about soap vs covid.</a><br/>
      <a href="https://www.youtube.com/watch?v=O-3Mlj3MQ_Q" target="_blank">click here to learn about covid charts misleading us.</a><br/>
      <a href="https://www.youtube.com/watch?v=421fmflQX0E" target="_blank">click here to learn about the look of covid.</a><br/>
      <a href="https://www.youtube.com/watch?v=U8r3oTVMtQ0" target="_blank">click here to learn about the symptoms</a><br/>
      <a href="https://www.youtube.com/watch?v=x7KKkElpyKQ" target="_blank">click here to learn about soap vs. hand sanitizer</a>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Information.vue',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  section.videos a{
  display: block;
  text-decoration: none;
  color: #8080ff;
  transition: all 0.3s cubic-bezier(0.93, 0.43, 0.66, 0.29);
  -webkit-transition: all 0.3s cubic-bezier(0.93, 0.43, 0.66, 0.29);
  -moz-transition: all 0.3s cubic-bezier(0.93, 0.43, 0.66, 0.29);
  -o-transition: all 0.3s cubic-bezier(0.93, 0.43, 0.66, 0.29);
  -ms-transition: all 0.3s cubic-bezier(0.93, 0.43, 0.66, 0.29);
  background-color: #000;
  margin: 5px;
  padding: 1vh 1vw;
  border-radius: 50%;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -o-border-radius: 50%;
  -ms-border-radius: 50%;
  text-align: center;
  width: 95vw;
  height: 5vh;
  }

  section.videos a:hover{
  color: #bfbfff;
  border-radius: 0;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  -o-border-radius: 0;
  -ms-border-radius: 0;
  }
</style>
