import { createApp } from 'vue'
import router from './router/index';
import './styles/styles.css'
import App from './App.vue'

const app = createApp(App)
app.use(router).mount('#app');
