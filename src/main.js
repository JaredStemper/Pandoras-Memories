import { createApp } from "vue";
import { createPinia } from "pinia";
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { 
  faPlay, 
  faPause, 
  faForward, 
  faBackward,
  faStop
} from '@fortawesome/free-solid-svg-icons';

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);

// Add the icons to the library
library.add(faPlay, faPause, faForward, faBackward, faStop);

app.component('font-awesome-icon', FontAwesomeIcon);

app.mount("#app");
