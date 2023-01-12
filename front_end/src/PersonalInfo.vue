<template>
  <!-- <el-container>
    <el-main>
      <el-row>
        <el-page-header @back="goBack">
            <template #content>
                <span class="text-large font-600 mr-3"> 个人信息 </span>
            </template>
        </el-page-header>
        <el-col :span="15">
          <div class="grid-content ep-bg-purple" />
        </el-col>
      </el-row>
      
      <el-row>
        <el-col :span="5" :offset="2">
           <div class="demo-basic--circle">
    <div class="block">
        <el-avatar class="avater" :size="AvaterSize" :src=this.info.avatar @click="redirect"></el-avatar>
    </div>
    <div>
    </div>
    </div>
          <div class="grid-content ep-bg-purple-light" />
        </el-col>
        <el-col :span="16"></el-col>
        <el-col :span="2"></el-col>
        <el-col :span="2">
        <span class="text-large font-600 mr-3">用户:{{ this.info.owner}}</span>
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="4"></el-col>
       <el-col :span="13">
        <span class="text-large font-600 mr-3">昵称:{{ this.info.nickname}}</span>
        </el-col>
        <el-col :span="4"></el-col>
       <el-col :span="14">
       <span class="text-large font-600 mr-3">个性签名:{{ this.info.signature }}</span>
        </el-col>
        <el-col :span="4"></el-col>
        <el-col :span="4"></el-col>
        <el-col :span="14">
       <span class="text-large font-600 mr-3">地址:{{ this.info.address }}</span>
        </el-col>
        <el-col :span="14">
          <div class="grid-content ep-bg-purple" />
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="8">
          <div class="grid-content ep-bg-purple-light" />
        </el-col>
        <el-col :span="10">
          <div class="grid-content ep-bg-purple" />
        </el-col>
      </el-row>
      
      <el-row>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="22">
        <el-button type="primary" @click="resetcode">重置密码</el-button>
        </el-col>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="22">
        <el-button type="primary" @click="changeinfo">修改个人信息</el-button>
        </el-col>
         <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="22">
        <el-button type="primary" @click="quit">退出登陆</el-button>
        </el-col>
      </el-row>

      <beautifulchat>
      </beautifulchat>
    </el-main>
  </el-container> -->
<el-page-header @back="goBack">
  <template #content>
      <span class="text-large font-600 mr-3"> 个人信息 </span>
  </template>
</el-page-header>
<body>
<div class="profile-container">
        <div class="img-container">
            <img :src=this.info.avatar @click="redirect" alt="profile image">
        </div>
        <p class="info full-name">{{ this.info.owner}}</p>
        <p class="info role">
            <i class="fas fa-star"></i>
            昵称:{{ this.info.nickname}}
        </p>
        <p class="info place">
            <i class="fas fa-map-marker-alt"></i>
            地址:{{ this.info.address }}
        </p>

         <p class="info place">
            <i class="fas fa-map-marker-alt"></i>
            个人签名:{{ this.info.signature }}
        </p>
        <button class="action" @click="resetcode">重置密码</button>
        <button class="action message1" @click="changeinfo">修改个人信息</button>
        <button class="action message" @click="quit">退出登陆</button>
    </div>

    <beautifulchat>
    </beautifulchat>
</body>
</template>
<script>
import {getUserDetail} from '../api/api.js'
import { reactive } from 'vue'
export default {
  data() {
    return {
      AvaterSize: 80,
      info:reactive({
                owner:"",
                nickname:"",
                avater:"",
                address:"",
                signature:""
        }),
    }
  },
  provide() {
    return {
      message: '/info'
    }
  },
    mounted: function (){
    this.loadinfo()
  },
  methods:{
    goBack(){
        this.$router.push('/')
    },
  resetcode(){
  this.$router.push('/resetcode')
  },
  quit(){
  this.$router.push('/login')
  window.localStorage.removeItem("token")
  },
  changeinfo(){
  this.$router.push('/changeinfo')
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
  },
  
}
// import {
//   Back,
// } from '@element-plus/icons-vue'
import beautifulchat from './BeautifulChat.vue'
</script>
<script setup>
// do not use same name with ref
</script>

<style scoped>
#Head{
  border: 1px solid;
}
#Avater {
  height: 200px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 20px;
}
.el-page-header{
  background-image: lightblue;
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