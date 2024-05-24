import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
console.log(import.meta.env.VITE_API_URL); // Output: 'http://localhost:5173'
console.log(import.meta.env.VITE_DEBUG_MODE);

createApp(App).mount('#app')
