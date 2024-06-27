<template>
    <section class="mt-5 text-center mx-auto">
        <h1 class="text-danger">Panadería y Rotisería Carlitos</h1>
        <img class="img-fluid" :src="require('@/assets/img/fondo.png')" alt="">
        <div class="mt-3" v-if="$route.path !== '/about'">
            <button type="button" class="btn btn-warning" v-for="category in categories" :key="category.id" @click="getCategory(category.id, category.name)">{{ category.name }}</button>
            <hr>
        </div>
    </section>
</template>

<script setup>
    import axios from 'axios'
    import { ref, defineEmits, onMounted } from 'vue'

    const categories = ref([])
    const categoryID = ref(null)
    const categoryName = ref(null)

    const emit = defineEmits(['getCategoryID'])

    const getCategory = (id, name) => {
        emit('getCategoryID', id, name)
    }

    onMounted(() => {
        axios.get('http://127.0.0.1:8000/api/categories/')
        .then(response => {
            categories.value = response.data
        })
        .catch(error => {
            console.log(error)
        })
    })
</script>

<style>
    /* Estilos adicionales del Navigation */
    button {
        margin-rigth: 5px;
    }

    button + button, button:first-child {
        margin-left: 5px;
    }

    @media (max-width: 768px) {
        button {
            width: 100%;
            margin: 0 0 5px !important;
            box-sizing: border-box;
        }
    }
</style>