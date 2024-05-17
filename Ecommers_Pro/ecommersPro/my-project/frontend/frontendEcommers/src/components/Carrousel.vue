<template>
    <div class="carousel-container">
      <div class="carousel" ref="carousel">
        <img v-for="(image, index) in images" :src="image" :key="index" alt="Carousel Image" class="carousel-image">
        <img >
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
        "../sets/vue.svg",
        "../assets/carru.jpg",
        "../assets/carru.jpg"
        ],
        currentIndex: 0,
        intervalId: null
      };
    },
    mounted() {
      this.startCarousel();
    },
    methods: {
      startCarousel() {
        this.intervalId = setInterval(() => {
          this.currentIndex = (this.currentIndex + 1) % this.images.length;
          this.scrollCarousel();
        }, 3000);
      },
      scrollCarousel() {
        const carousel = this.$refs.carousel;
        carousel.scrollTo({
          left: carousel.offsetWidth * this.currentIndex,
          behavior: "smooth"
        });
      },
      stopCarousel() {
        clearInterval(this.intervalId);
      }
    },
    beforeDestroy() {
      this.stopCarousel();
    }
  };
  </script>
  
  <style scoped>
  .carousel-container {
    overflow: hidden;
  }
  
  .carousel {
    display: flex;
  }
  
  .carousel-image {
    width: 40%;
    flex-shrink: 0;
  }
  </style>
  