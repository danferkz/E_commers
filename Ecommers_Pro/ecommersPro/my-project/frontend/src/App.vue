<template>
  <div>
    <h1>Welcome to the Vue.js App!</h1>
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
h1 {
  color: blue;
}
</style>