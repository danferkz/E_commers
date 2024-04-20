<template>
  <div class="hello-world">
    <h1>{{ greeting }}</h1>
    <p>Welcome to my Vue.js app with Vite!</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      greeting: 'Hello, World!'
    }
  }
}
</script>

<style scoped>
.hello-world {
  text-align: center;
  margin-top: 20px;
}
</style>