<script setup>
import WebHeader from './components/Header.vue'
import WebFooter from './components/Footer.vue'
import WebCarrousel from './components/Carrousel.vue'
import WebCategories from './components/Categories.vue'
</script>

<template>
  <template>
  <div class="container">
    <!-- NAVBAR -->
    <navbar-component-vue v-if="$route.path != '/'" />

    <!-- NAVIGATION -->
    <navigation-component-vue v-if="$route.path === '/about'" />

    <router-view/>

    <!-- FOOTER -->
    <footer-component-vue />
  </div>

</template>
<script setup>
  import NavbarComponentVue from './components/NavbarComponent.vue'
  import NavigationComponentVue from './components/NavigationComponent.vue'
  import FooterComponentVue from './components/FooterComponent.vue'
</script>

</template>

<style>

</style>
