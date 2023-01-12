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
      <el-row >
        <el-col :span="2">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="22">
          <el-form :model="this.form" label-width="100px" id="selectForm">
            <el-form-item label="头像">
            <a href="javascript:;" class="file">选择文件
               <input type="file"  @change="onchangemd" />
            </a>
              </el-form-item>
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
              <el-button type="primary" @click="onSubmit(this.form,this.formData)">Create</el-button>
              <el-button>Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-col>
      <el-col :span="11">
          <div class="grid-content ep-bg-purple" />
        </el-col>
        <el-col :span="12">
        <el-button type="primary" @click="resetcode">重置密码</el-button>
        </el-col>
      </el-row>

      <beautifulchat>
      </beautifulchat>
    </el-main>
  </el-container>

</template>
<script>

export default {
  data() {
    return {
      formData:new FormData(),
      AvaterSize: 80,
    form : reactive({
    address:'',
    avatar:'',
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
    onchangemd(e){
		console.log(e.target.files)//选中文件信息
		Array.from(e.target.files).map(item => {
         console.log(item)
         this.form.avatar=item
       })
       ElMessage("头像上传成功！")
	},
    goBack(){
        this.$router.push('/info')
    },
  resetcode(){
  this.$router.push('/resetcode')
  },
          onSubmit(params,formData){
            formData.append("address",params.address)
            formData.append("avatar",params.avatar)
            formData.append("nickname",params.nickname)
            formData.append("signature",params.signature)
            console.log(formData.get("avatar"))
            updateUserInfo(formData).then(response => {
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
import beautifulchat from './BeautifulChat.vue'
import { ElMessage } from 'element-plus'
</script>
<script setup>
import { reactive } from 'vue'
// do not use same name with ref
</script>

<style scoped>
@keyframes bganimation {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}
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
.el-form {
    height: 40vh;
    width: 100%;
    overflow: hidden;
    background-image:  lightblue;
    background-size: 100%;
    font-family: "montserrat";
    animation: bganimation 15s infinite;
}
.el-container{
  height: 100vh;
  background-image: linear-gradient(125deg,lightblue, white );
}
.el-form h1 {
    margin-top: 0;
    font-weight: 200;
}
.el-form-item {
    border: 3px solid #aaa;
    margin: 8px 0;
    padding: 12px 18px;
    border-radius: 10px;
    color: #fff;
    font-size: 30px;
}
.el-form-item el-input{
    width: 100%;
    background: none;
    border: none;
    outline: none;
    margin-top: 6px;
    font-size: 18px;
    color: #fff;
}
.el-form-item label{
    font-size: 100px;
}

#selectForm >>> .el-form-item__label {
  font-size: 18px;
}
.file {
    position: relative;
    display: inline-block;
    background: #D0EEFF;
    border: 1px solid #99D3F5;
    border-radius: 4px;
    padding: 4px 12px;
    overflow: hidden;
    color: #1E88C7;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
}
.file input {
    position: absolute;
    font-size: 100px;
    right: 0;
    top: 0;
    opacity: 0;
}
.file:hover {
    background: #AADFFD;
    border-color: #78C3F3;
    color: #004974;
    text-decoration: none;
}
</style>