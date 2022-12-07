<!-- This is for ManagePage -->
<template>
    <div class="common-layout">
      <el-container>
        <el-header id="headerBack" height="200px">
          <Navigator :msg="redirect" />
        </el-header>
        <el-main id="MainBack">
          test
          {{need_test.name}}
        </el-main>
        <el-footer id="FooterBack">
        test
        </el-footer>
      </el-container>
    </div>
  </template>
  <script setup>
//   import { ref } from 'vue'
  
  </script>
  <script>
//   import foo from './components/FooterGrid.vue'
  import Navigator from './components//NavigationBar.vue'
  import { getNeeds } from '../api/index';
  export default {
    components: {Navigator },
    data() {
      return {
        ButtonLeft: "求助",
        ButtonRight: "我的提供",
        needs : [
        ],
        need_test : {
          name: '矿泉水喝完了',
          tags: ['饮用品', '水', '较紧急'],
          desc: "饮水机坏了，被封着快没水了。",
          address: "东3"
        }
        
      }
    },
    methods: {
      loadNeeds () {
        getNeeds().then(response => {
          this.needs = response.data
          console.log(this.needs)
        })
      }
    },
    created: function () {
      console.log("hello")
      this.loadNeeds()
    },
    provide() {
      return {
        message: '/info',
        messageFooLeft: '/request',
        messageFooRight: '/offer'
      }
    }
  }
  </script>
  <style scoped>
  .el-container {
    height: 100vh;
  }
  .box-card{
    width: 80vw;
    text-overflow:ellipsis;
  }
  .box-card-fold{
    width: 40vw;
    height: 200px;
    text-overflow:ellipsis;
  }
  .card-header{
    display: flex;
    flex-direction: row;
  }
  .card-header .name {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
  
  .card-header .tags {
    display: flex;
    margin-left: auto;
    align-items: center;
    gap: 10px;
  }
  .card-header-fold{
    display: flex;
    flex-direction: column;
  }
  .card-header-fold .name {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
  
  .card-header-fold .tags {
    width: 100%;
    display: flex;
    margin-left: auto;
    align-items: flex-start;
    gap: 5px;
  }
  
  
  #headerBack {
    margin-bottom: 20px;
    background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
    background-size: cover;
  }
  
  #MainBack {
    /* background: linear-gradient(120deg, yellow 0%, silver 100%); */
    background-size: cover;
  }
  
  #FooterBack {
    background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat;
    background-size: cover;
  }
  </style>