// npx 下载的module的地址 ~/.npm/_npx\
// npm 的全局下载路径为 /usr/local/lib/node_modules
import { createApp } from 'vue'
import {createRouter,createWebHashHistory} from 'vue-router'
import home from './HomePage.vue'
import Info from './PersonalInfo.vue'
const routes = [
    { path: '/', component: home },
    { path: '/info', component: Info },
]
const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')