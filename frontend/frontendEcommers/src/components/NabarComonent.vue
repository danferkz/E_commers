<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <router-link class="nav-link active" aria-current="page" to="/">Inicio</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about">Acerca de Nosotros</router-link>
                </li>
            </ul>
            <form class="d-flex" role="search" @submit.prevent="submitForm" v-if="$route.path === '/'" >
                <input class="form-control me-2" type="search" placeholder="Buscar..." aria-label="Search" v-model="searchText">
                <button class="btn btn-outline-success" type="submit" @click="getSearch">Buscar</button>
            </form>
        </div>
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
</script>

<style>
    /* Estilos adicionales del footer */
</style>