import App from "./App.vue";
import "./assets/css/tailwind.css";

import Vue from "vue";
import Router from "vue-router";
import router from "./router";

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");

Vue.use(Router);
