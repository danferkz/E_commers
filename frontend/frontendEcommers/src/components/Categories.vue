<template>
    <div class="button-container">
      <button v-for="(category, index) in categories" :key="index" @click="handleClick(category)">
        {{ category }}
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: "HorizontalButtons",
    data() {
      return {
        categories: ["Plásticos", "Metales", "Herramientas", "Pinturas", "Electricidad", "Jardinería"]
      };
    },
    methods: {
      handleClick(category) {
        console.log(`Button ${category} clicked`);
      }
    }
  };
  </script>
  
  <style scoped>
  .button-container {
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  button {
    padding: 10px 20px;
    margin: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f0f0f0;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  button:hover {
    background-color: #ddd;
  }
  </style>
  