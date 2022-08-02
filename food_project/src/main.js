import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core';
import { faAddressCard, faHourglassHalf, faClipboardCheck, faTrashCan } from '@fortawesome/free-solid-svg-icons';
library.add(faAddressCard, faHourglassHalf, faClipboardCheck, faTrashCan);

createApp(App).use(router).mount('#app') 

