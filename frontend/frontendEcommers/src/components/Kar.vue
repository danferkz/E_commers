<template>
  <div class="carousel-container">
    <div class="slides" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div class="slide" v-for="(image, index) in images" :key="index">
        <img class="img-fluid" :src="image" :alt="'Image ' + (index + 1)">
      </div>
    </div>
    <button class="nav-button prev" @click="prevSlide">‹</button>
    <button class="nav-button next" @click="nextSlide">›</button>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import image1 from '@/assets/img/imagenFerreteria.jpg';
import image2 from '@/assets/img/imagenFerreteria.jpg';
import image3 from '@/assets/img/imagenFerreteria.jpg';

export default {
  setup() {
    const images = [image1, image2, image3];
    const currentIndex = ref(0);
    let interval;

    const nextSlide = () => {
      currentIndex.value = (currentIndex.value + 1) % images.length;
    };

    const prevSlide = () => {
      currentIndex.value = (currentIndex.value - 1 + images.length) % images.length;
    };

    const startAutoSlide = () => {
      interval = setInterval(nextSlide, 3000);
    };

    const stopAutoSlide = () => {
      clearInterval(interval);
    };

    onMounted(startAutoSlide);
    onBeforeUnmount(stopAutoSlide);

    return {
      images,
      currentIndex,
      nextSlide,
      prevSlide,
      startAutoSlide,
      stopAutoSlide
    };
  }
};
</script>

<style scoped>
.carousel-container {
  width: 95vw;
  height: 30vh;
  position: relative;
  overflow: hidden;
  margin: 0 auto;
}

.slides {
  display: flex;
  width: 100%; /* Ajusted to fit the number of slides */
  height: 100%;
  transition: transform 0.5s ease;
}

.slide {
  width: 90vw;
  height: 110%;
  flex: 0 0 100%;
  overflow: hidden;
}

.slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.5);
  border: none;
  padding: 10px;
  cursor: pointer;
  z-index: 10;
}

.nav-button.prev {
  left: 10px;
}

.nav-button.next {
  right: 10px;
}
</style>
