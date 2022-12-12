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
          <AvaterUsr :AvaterSize="AvaterSize"></AvaterUsr>
          <div class="grid-content ep-bg-purple-light" />
        </el-col>
        <el-col :span="14">
        <span class="text-large font-600 mr-3">个性签名</span>
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="8">
          <Uploader></Uploader>
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
  components: { AvaterUsr, Uploader },
  data() {
    return {
      AvaterSize: 80,
      need :reactive({
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
  loadinfo() {
      getUserDetail().then(response => {
        this.needs = response.data;
        console.log("needs:")
        console.log(this.needs);
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
import AvaterUsr from './components/AvaterUser.vue'
import Uploader from './components/UploadImg.vue'
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