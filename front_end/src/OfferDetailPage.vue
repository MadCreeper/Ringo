<template>
<body>
    <div class="profile-container">
    <div class="img-container">
            <img :src=this.info.avatar @click="redirect" alt="profile image">
        </div>
    <p class="info full-name"> {{ this.item.user }}</p>
        <p class="info role">
        <i class="fas fa-star"></i>
    {{ item_type[this.item.property_type] + ": " + this.item.name }}
    </p>
    <p class="info role">
    <i class="fas fa-star" v-if="this.item.category">
<el-tag class="ml-2" type="success">{{ this.item.category.name }}</el-tag>
</i>
</p>
<p class="info place" v-if="this.item.goods_brief">
    <i class="fas fa-star">
</i>物品简介:
{{ this.item.goods_brief }}
</p>
<p class="info place" v-if="this.item.goods_desc">
    <i class="fas fa-map-marker-alt"></i>
   <img :src="`${this.item.goods_desc}`" class="img-display" />
</p>

<p class="info place">
    <i class="fas fa-star">
</i><el-icon>
    <House />
</el-icon> {{ "地址: " + item.address }}
</p>

    <p class="info place" v-if="this.item.add_time && this.item.expected_end_time">
    <i class="fas fa-map-marker-alt"></i>
    {{ formatDateTime(this.item.add_time) }} ~ {{ formatDateTime(this.item.expected_end_time) }}
</p>
   <button class="action message" type="primary" circle @click="deletesn(this.$route.query.id)">删除</button>
<button class="action" type="primary" circle @click="goback()">返回</button>
 </div>
 </body>
</template>

<script>
/* eslint-disable */
import { onMounted } from 'vue'

import { getOfferingDetail } from '../api/api';
import { emergency_levels, item_type } from './dataTypes'
import { formatDateTime } from './utils'
import { reactive } from 'vue'
import {getUserDetail} from '../api/api.js'
import {delOffering } from '../api/api.js'
export default {
    data() {
        return {
            whether:false,
            itemId: -1,
            ButtonLeft: "求助",
            ButtonRight: "我的提供",
            item: {},
             info:reactive({
                owner:"",
                nickname:"",
                avater:"",
                address:"",
                signature:""
        }),
            item_test: {
                name: '矿泉水喝完了',
                tags: ['饮用品', '水', '较紧急'],
                desc: "饮水机坏了，被封着快没水了。",
                address: "东3"
            },
            emergency_levels: emergency_levels,
            item_type: item_type
        }
    },
    methods: {
        getItemById(item_id) {
            getOfferingDetail(item_id).then(response => {
                console.log(response.data)
                this.item = response.data
                console.log(this.item.category.name)
            })
        },
        deletesn(item_id){
            console.log(item_id)
            delOffering(item_id).then(response =>{
                console.log(response.data)
                this.$router.push('/offer')
            }).catch(err => {
                this.$router.push('/offer')
            })
        },
        loadinfo() {
      getUserDetail().then(response => {
        this.info = response.data;
        this.info.avatar="http://127.0.0.1:8000"+response.data.avatar;
        console.log("info:")
        console.log(this.info.avatar)
      })
      .catch(
        err => {
          console.log(err)
          this.$router.push('/login')
        }
      )
    },
    goback(){
            this.$router.push('/offer')
        },
        formatDateTime,
    },
    created() {
        onMounted(() => {
            console.log("detail page")
            this.getItemById(this.$route.query.id)
            console.log(emergency_levels)
            this.loadinfo()
            // console.log(this.$route.query.id)
        })
    },
    provide() {
        return {
            message: '/info',
            messageFooLeft: '/request',
            messageFooRight: '/offer'
        }
    },
}
</script>
<style scoped>
.el-container {
    height: 100vh;
}

.body {
    line-height: 3ch;
    text-indent: 2ch;
}

.item-title {
    /* align-self: flex-end; */
    font-size: xx-large;
    /* background-color: lightgrey; */
    display: flex;
    flex-direction: row;
}

.item-title .tags {
    display: flex;
    margin-left: auto;
    align-items: center;
    gap: 10px;
}

.user-display {
    display: flex;
    flex-direction: row;
    justify-items: right;
    align-items: center;
    font-size: large;
}

.item-time {
    text-align: right;
    font-size: smaller;
    color: dimgray;
}
.img-display {
  width: 80%;
  height: 80%;
}

#headerBack {
    display: flex;
    margin-bottom: 20px;
    background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
    background-size: cover;
}

#MainBack {
    /* background: linear-gradient(120deg, yellow 0%, silver 100%); */
    background-size: cover;
}

#FooterBack {
    /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
    background-size: cover;
}
* {
    margin     : 0;
    padding    : 0;
    box-sizing : border-box;
    color      : #334e64;
    font-family: 'Montserrat', sans-serif;
}

body {
    min-height     : 100vh;
    width          : 100%;
    display        : flex;
    justify-content: center;
    align-items    : center;
    background-image: linear-gradient(125deg,lightblue, white );
}

.profile-container {
    position        : relative;
    background-color: #fff;
    width           : 550px;
    padding         : 100px 50px 40px;
    border-radius   : 12px;
    box-shadow      : 0 0 60px 5px rgba(0, 0, 0, 0.2);
    display         : flex;
    flex-direction  : column;
    justify-content : center;
    align-items     : center;
}

.img-container {
    width        : 130px;
    height       : 130px;
    overflow     : hidden;
    border       : 5px solid skyblue;
    border-radius: 50%;
    box-shadow   : 0 8px 55px lightblue;
    position     : absolute;
    top          : 0;
    left         : 50%;
    transform    : translate(-50%, -50%);
}

.img-container img {
    width    : 100%;
    max-width: 100%;
    height   :100%;
    transform: scale(1.1);
}

.info {
    margin-bottom: 12px;
}

.info i {
    margin-right: 8px;
    font-size   : 1.1em;
}

.place {
    margin-bottom: 40px;
}

.full-name {
    font-size     : 1.4em;
    font-weight   : bold;
    letter-spacing: 1px;
    color         : #b92a76;
}

.posts-info {
    width          : 100%;
    display        : flex;
    justify-content: space-around;
    align-items    : center;
    font-size      : 1.1em;
    letter-spacing : 0.5px;
    margin-bottom  : 30px;
    text-align     : center;
}

.posts-info span {
    display      : block;
    font-weight  : bold;
    margin-bottom: 4px;
}

.social-container {
    width          : 100%;
    display        : flex;
    justify-content: space-between;
    align-items    : center;
    margin-bottom  : 20px;
}

.social-container i {
    color: #fff;
}

.social-container button {
    border          : none;
    outline         : none;
    width           : 45px;
    height          : 45px;
    border-radius   : 50%;
    font-size       : 1.2em;
    cursor          : pointer;
    box-shadow      : 0px 5px 25px rgba(0, 0, 0, 0.15);
    transition      : transform 0.3s;
}

.social-container button:hover {
    transform: scale(1.1);
}

/* Social colors */

.social-container button.qq {
    background: linear-gradient(45deg, #74D2FF, #0098FF);
}

.social-container button.weixin {
    background: linear-gradient(45deg, #8BFF9A, #4EE214);
}

.social-container button.youtube {
    background: linear-gradient(45deg, #e6683ccc 25%, #dc2743 50%,
            #bc1888 100%);
}

.social-container button.github {
    background: linear-gradient(45deg, #33333388, #333333);
}

.action {
    outline: none;
    cursor: pointer;
    color: #fff;
    background-color: gold;
    border: none;
    border-radius: 50px;
    padding: 12px 20px;
    width: 80%;
    margin-top: 25px;
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.2);
    text-transform: uppercase;
    font-size: 1em;
    font-weight: bold;
    letter-spacing: 2px;
    transition: transform 0.3s, opacity 0.3s;
}

.action.message1 {
    background-color: skyblue;
}
.action.message {
    background-color: red;
}

.action:hover {
    transform: scale(1.05);
    opacity: 0.85;
}
</style>
