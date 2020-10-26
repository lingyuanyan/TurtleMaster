<template>
  <div class="post">
    <details>
      <summary>Comments</summary>
      <form action="/action_page.php">
        <textarea name="message" rows="10" cols="30" placeholder="Your review"></textarea>

        <input type="submit">
      </form>
    </details>
  </div>
</template>

<script>
export default {
  name: 'Post',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
details {
  text-align: center;
}
</style>
