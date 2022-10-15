import { createApp } from "vue";
import { createPinia } from "pinia";
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from "./App.vue";
import router from "./router";
axios.create({
    baseURL: "127.0.0.1:5000"
})
import "./assets/main.css";
const app = createApp(App);
app.use(VueAxios, axios) // 👈
app.use(createPinia());
app.use(router);

app.mount("#app");
