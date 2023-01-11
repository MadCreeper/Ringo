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
          <InputForm></InputForm>
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
          <el-form :model="this.form" label-width="120px">
            <el-form-item label="昵称">
              <el-input v-model=this.form.nickname />
            </el-form-item>
            <el-form-item label="个性签名">
                <el-input v-model=this.form.signature />
            </el-form-item>
            <el-form-item label="地址">
            <el-input v-model=this.form.address />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit(this.form)">Create</el-button>
              <el-button>Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      

      <beautifulchat>
      </beautifulchat>
    </el-main>
  </el-container>

</template>
<script>
export default {
  components: { AvaterUsr, InputForm, Uploader },
  data() {
    return {
      AvaterSize: 80,
    form : reactive({
    nickname: '',
    signature:'',
})
    }
  },
  provide() {
    return {
      message: '/info'
    }
  },
  methods:{
    goBack(){
        this.$router.push('/info')
    },
  resetcode(){
  this.$router.push('/resetcode')
  },
          onSubmit(params){
            console.log(params)
            updateUserInfo(params).then(response => {
               console.log(response)
               this.$router.push('/info')
        }).catch(
        err => {
          console.log(err)
          this.$router.push('/login')
        }
      )
        }
  }
}
// import {
//   Back,
// } from '@element-plus/icons-vue'
import {updateUserInfo} from '../api/api.js'
import AvaterUsr from './components/AvaterUser.vue'
import InputForm from './components/InputForm.vue'
import Uploader from './components/UploadImg.vue'
import beautifulchat from './BeautifulChat.vue'
</script>
<script setup>
import { reactive } from 'vue'
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
</style>