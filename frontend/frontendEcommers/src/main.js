import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';
import store from './store';
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'


console.log(import.meta.env.VITE_API_URL); // Output: 'http://localhost:5173'
console.log(import.meta.env.VITE_DEBUG_MODE);

createApp(App).use(store).use(router).mount('#app')
