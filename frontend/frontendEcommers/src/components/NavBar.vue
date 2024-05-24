<template>
    <nav class="GHeader">
        <div class="logo">
            <router-link to="/">
                <img src="../assets/vue.svg" alt="Logo de la empresa">
            </router-link>
        </div>
        <div class="navigation">
            <router-link class="nav-link" to="/">Inicio</router-link>
            <router-link class="nav-link" to="/about">Acerca de Nosotros</router-link>
        </div>
        <div class="search">
            <form class="d-flex" role="search" @submit.prevent="submitForm">
                <input type="search" placeholder="Buscar productos por nombre..." aria-label="Search" v-model="searchText">
                <button type="submit" @click="getSearch">Buscar</button>
            </form>
        </div>
        <div class="cart">
            <button type="button">Carrito</button>
        </div>
    </nav>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const searchText = ref('')
const emitSearch = defineEmits(['getSearchText'])

const getSearch = () => {
    emitSearch('getSearchText', searchText.value)
}

const submitForm = () => {
    getSearch()
}
</script>

<style>
/* Estilos generales */
.GHeader {
  background-color: #333;
  position: fixed;
  color: #fff;
  top: 0;
  left: 0;
  display: flex;
  width: 100vw;
  justify-content: space-between;
  padding: 10px;
}

.logo {
  margin-right: auto;
}

.logo img {
  height: 50px;
}

.navigation {
  display: flex;
  align-items: center;
  margin: 0 10px;
}

.nav-link {
  color: white;
  margin: 0 10px;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

.search {
  margin: 0 10px;
}

.search input[type="search"] {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.search button {
  padding: 8px 15px;
  border-radius: 5px;
  border: none;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

.cart {
  margin-left: auto;
}

.cart button {
  padding: 8px 15px;
  border-radius: 5px;
  border: none;
  background-color: #008CBA;
  color: white;
  cursor: pointer;
}
</style>