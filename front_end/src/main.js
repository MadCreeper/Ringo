// npx 下载的module的地址 ~/.npm/_npx\
// npm 的全局下载路径为 /usr/local/lib/node_modules
import { createApp} from 'vue'
import {createRouter,createWebHashHistory} from 'vue-router'
import home from './HomePage.vue'
import Info from './PersonalInfo.vue'
import Login from './LoginPage.vue'
import manage from './ManagePage.vue'
import chat from './PrivateChat.vue'
import chat2 from './BeautifulChat.vue'
import submitNeed from './SubmitNeed.vue'
import mytest from './MyTest.vue'
import Offer from './OfferingPage.vue'
import HelloWorld from './HelloWorld.vue'
const routes = [
    { path: '/', component: home },
    { path: '/info', component: Info },
    { path: '/chattest', component: chat},
    { path: '/chat2', component: chat2},
    { path: '/request', component: submitNeed},
    { path: '/test', component: mytest},
    { path: '/offer',component: Offer},
    { path: '/login',component:Login},
    { path: '/Manage',component:manage},
    { path: '/Hello',component:HelloWorld }
]
const router = createRouter({
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})
import Chat from 'vue3-beautiful-chat'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import VueSnip from 'vue-snip'

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.use(Chat)
app.use(VueSnip)
app.mount('#app')


