<template>
    <div class="categories-grid">
      <div 
        class="category-item" 
        v-for="(category, index) in categories" 
        :key="index"
        :style="{ backgroundImage: 'url(' + category.image + ')' }"
        @click="navigateTo(category.link)"
      >
        <div class="category-text">{{ category.text }}</div>
      </div>
    </div>
  </template>


<script>
export default {
  data() {
    return {
      categories: [
        { image: 'https://via.placeholder.com/300?text=Category+1', text: 'Herramientas', link: '/herramientas' },
        { image: 'https://via.placeholder.com/300?text=Category+2', text: 'Materiales de Construcción', link: '/materiales-de-construccion' },
        { image: 'https://via.placeholder.com/300?text=Category+3', text: 'Electricidad', link: '/electricidad' },
        { image: 'https://via.placeholder.com/300?text=Category+4', text: 'Fontanería', link: '/fontaneria' },
        { image: 'https://via.placeholder.com/300?text=Category+5', text: 'Pinturas', link: '/pinturas' },
        { image: 'https://via.placeholder.com/300?text=Category+6', text: 'Jardinería', link: '/jardineria' }
      ]
    };
  },
  methods: {
    navigateTo(link) {
      this.$router.push(link);
    }
  }
};
</script>

<style scoped>
.categories-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 20px;
}

.category-item {
  position: relative;
  width: 100%;
  padding-top: 100%; /* This creates a square based on the width */
  background-size: cover;
  background-position: center;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.category-text {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 10px;
  text-align: center;
}
</style>