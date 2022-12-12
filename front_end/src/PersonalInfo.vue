<template>
  <el-container>
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
      </el-row>

      <beautifulchat>
      </beautifulchat>
    </el-main>
  </el-container>

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
  resetcode(){
  this.$router.push('/resetcode')
  },
  changeinfo(){
  this.$router.push('/changeinfo')
  },
  loadinfo() {
      getUserDetail().then(response => {
        this.info = response.data;
        console.log("needs:")
        console.log(this.info);
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
const goBack = () => {
    history.back();
}
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
</style>