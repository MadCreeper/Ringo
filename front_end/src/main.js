// npx 下载的module的地址 ~/.npm/_npx\
// npm 的全局下载路径为 /usr/local/lib/node_modules
import { createApp} from 'vue'
import {createRouter,createWebHashHistory} from 'vue-router'
import home from './HomePage.vue'
import Info from './PersonalInfo.vue'
import Login from './LoginPage.vue'
import manage from './ManagePage.vue'
import submitNeed from './SubmitNeed.vue'
import mytest from './MyTest.vue'
import Offer from './OfferingPage.vue'
import submitOffer from './SubmitOffering.vue'
import detailPage from './DetailPage.vue'
import offerDetailPage from './OfferDetailPage.vue'
import register from  './RegisterPage.vue'
import changecode from './ChangeCodePage.vue'
import resetcode from './ResetCode.vue'
import changeinfo from './ChangeInfo.vue'
import chat from './ChatPage.vue'
const routes = [
    { path: '/', component: home, meta:{index:1} },
    { path: '/info', component: Info,meta:{index:3} },
    { path: '/request', component: submitNeed,meta:{index:4}},
    { path: '/test', component: mytest,meta:{index:5}},
    { path: '/offer',component: Offer,meta:{index:2} },
    { path: '/submitoffer', component: submitOffer,meta:{index:7} },
    { path: '/login',component:Login,meta:{index:8}},
    { path: '/Manage',component:manage,meta:{index:9}},
    { path: '/details', component : detailPage,meta:{index:10}},
    { path: '/offerdetails', component: offerDetailPage,meta:{index:11}},
    { path: '/register', component : register,meta:{index:12}},
    { path: '/changecode', component : changecode,meta:{index:13}},
    { path: '/resetcode',component:resetcode,meta:{index:14}},
    { path: '/changeinfo',component:changeinfo,meta:{index:15}},
    { path: '/chat', component:chat,meta:{index:16}}
]
const router = createRouter({
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})
import Chat from 'vue3-beautiful-chat'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'element-plus/dist/index.css'
import App from './App.vue'
import VueSnip from 'vue-snip'
import locale from 'element-plus/es/locale/lang/zh-cn'
const app = createApp(App)
app.use(router)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.use(ElementPlus,{locale})
app.use(Chat)
app.use(VueSnip)
app.mount('#app')


