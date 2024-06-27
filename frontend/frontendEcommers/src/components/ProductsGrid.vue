<template>
    <div class="product-grid">
      <div class="product-card" v-for="(product, index) in products" :key="index">
        <img :src="product.image" alt="Product Image" class="product-image" />
        <h2>{{ product.name }}</h2>
        <h4>{{ product.category }}</h4>
        <p>{{ product.description }}</p>
        <hr />
        <p class="price">{{ product.price }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProductGrid",
    data() {
      return {
        products: [
          {
            name: "Producto 1",
            category: "Categoría 1",
            image: "ruta/a/la/imagen1.jpg",
            description: "Descripción del producto 1",
            price: "$10.00"
          },
          {
            name: "Producto 2",
            category: "Categoría 2",
            image: "ruta/a/la/imagen2.jpg",
            description: "Descripción del producto 2",
            price: "$20.00"
          },
          {
            name: "Producto 3",
            category: "Categoría 3",
            image: "ruta/a/la/imagen3.jpg",
            description: "Descripción del producto 3",
            price: "$30.00"
          },
          {
            name: "Producto 4",
            category: "Categoría 4",
            image: "ruta/a/la/imagen4.jpg",
            description: "Descripción del producto 4",
            price: "$40.00"
          },
          {
            name: "Producto 5",
            category: "Categoría 5",
            image: "ruta/a/la/imagen5.jpg",
            description: "Descripción del producto 5",
            price: "$50.00"
          },
          {
            name: "Producto 6",
            category: "Categoría 6",
            image: "ruta/a/la/imagen6.jpg",
            description: "Descripción del producto 6",
            price: "$60.00"
          }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .product-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .product-card {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 15px;
    margin: 10px;
    width: calc(33.33% - 20px); /* Ajusta el ancho para tener 3 productos por fila */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .product-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
  .price {
    font-weight: bold;
    color: #2a9d8f;
  }
  hr {
    margin: 10px 0;
  }
  </style>
  