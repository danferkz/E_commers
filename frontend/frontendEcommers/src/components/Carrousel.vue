<template>
  <div class="carousel">
    <div class="carousel-inner">
      <div class="carousel-item" v-for="(item, index) in items" :key="index">
        <img :src="item.src" :alt="item.alt">
      </div>
    </div>
    <a class="carousel-control-prev" @click="prevSlide">&#10094;</a>
    <a class="carousel-control-next" @click="nextSlide">&#10095;</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { src: 'https://via.placeholder.com/800x400?text=Slide+1', alt: 'Slide 1' },
        { src: 'https://via.placeholder.com/800x400?text=Slide+2', alt: 'Slide 2' },
        { src: 'https://via.placeholder.com/800x400?text=Slide+3', alt: 'Slide 3' }
      ],
      currentIndex: 0
    };
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.items.length;
      this.updateSlide();
    },
    prevSlide() {
      this.currentIndex = (this.currentIndex - 1 + this.items.length) % this.items.length;
      this.updateSlide();
    },
    updateSlide() {
      const carouselInner = this.$el.querySelector('.carousel-inner');
      const width = this.$el.clientWidth;
      carouselInner.style.transform = `translateX(-${this.currentIndex * width}px)`;
    }
  },
  mounted() {
    this.updateSlide();
    window.addEventListener('resize', this.updateSlide);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateSlide);
  }
};
</script>

<style scoped>
.carousel {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.carousel-inner {
  display: flex;
  transition: transform 0.5s ease-in-out;
}

.carousel-item {
  min-width: 100%;
  box-sizing: border-box;
}

.carousel-item img {
  width: 100%;
  display: block;
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 10px;
  cursor: pointer;
  user-select: none;
}

.carousel-control-prev {
  left: 10px;
}

.carousel-control-next {
  right: 10px;
}
</style>