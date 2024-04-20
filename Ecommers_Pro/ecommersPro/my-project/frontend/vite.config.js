import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Replace with your Django backend URL
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    outDir: '../backend/service1/app1/static', // Replace with the static files directory of your Django app
    assetsDir: '',
    rollupOptions: {
      input: 'src/main.js'
    }
  }
})