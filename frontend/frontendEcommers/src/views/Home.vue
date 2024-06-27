<template>
    <div>
      <!-- NAVABAR -->
      <navbar-component-vue @getSearchText="search"/>
  
      <!-- NAVIGATION -->
      <navigation-component-vue @getCategoryID="categoryID" />
  
      <div class="mb-3" v-if="searchTextRule">
        <h3>Productos con el texto <strong>{{ searchTextRule }}</strong></h3>
        <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los Productos</button>
        <div class="alert alert-warning mt-3" role="alert" v-if="filteredProducts.length === 0" >
          Lamentablemente no existen productos con el texto <strong>{{ searchTextRule }}</strong>
        </div>
      </div>
  
      <div class="mb-3" v-if="categoryReceived">
        <h3>Productos de la Categoría <strong>{{ categoryReceived }}</strong></h3>
        <button class="btn btn-lg btn-warning" @click="resetFilter">Mostrar todos los Productos</button>
        <div class="alert alert-warning mt-3" role="alert" v-if="filteredProducts.length === 0" >
          Lamentablemente no existen productos para la categoría <strong>{{ categoryReceived }}</strong>
        </div>
      </div>
  
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="product in filteredProducts" :key="product.id">
          <div class="card text-center">
            <img :src="product.image" class="card-img-top" alt="Imagen de {{ product.name }}">
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <h6 class="card-subtitle mb-2 text-body-secondary">{{ product.category_name }}</h6>
              <p class="card-text">{{ product.description }}</p>
            </div>
            <div class="card-footer text-danger">
              PRECIO: $ {{ product.price }} - Por {{ product.price_type_description }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import axios from 'axios'
    import NavigationComponentVue from '../components/NavigationComponent.vue'
    import NavbarComponentVue from '../components/NavbarComponent.vue'
    import { ref, onMounted } from 'vue'
  
    const products = ref([])
    const filteredProducts = ref([])
    const categoryReceived = ref(null)
    const searchTextRule = ref(null)
  
    const search = (searchText) => {
      categoryReceived.value = null
      searchTextRule.value = searchText
  
      if(searchText) {
        filteredProducts.value = products.value.filter((product) => {
          const productName = product.name.toLowerCase();
          const productDescription = product.description.toLowerCase();
          const searchTerm = searchText.toLowerCase();
  
          return (
            productName.includes(searchTerm) ||
            productDescription.includes(searchTerm)
          )
        })
      } else {
        filteredProducts.value = products.value
      }
    }
  
    const categoryID = (categoryID, categoryName) => {
      searchTextRule.value = null
      categoryReceived.value = categoryName
      if(categoryID) {
        filteredProducts.value = products.value.filter((product) => product.category === categoryID)
      } else {
        filteredProducts.value = products.value
      }
    }
  
    const resetFilter = () => {
      categoryReceived.value = null
      searchTextRule.value = null
      filteredProducts.value = products.value
    }
  
    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/products/')
      .then(response => {
        products.value = response.data
        filteredProducts.value = products.value
      })
      .catch(error => {
        console.log(error)
      })
    })
  </script>
  
  <style>
    .card {
      border: 2px solid gray !important;
    }
  </style>