<template>
    <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px" >
      <Navigator></Navigator>
      </el-header>
      <el-main id="MainBack">
      <el-row>
        <el-col
          v-for="(o, index) in 2"
          :key="o"
          :span="8"
          :offset="index > -1 ? 3 : 0"
        >
        <car :imageurl="url[0]" />
        </el-col>
      </el-row>
      <el-row>
        <el-col
          v-for="(o, index) in 2"
          :key="o"
          :span="8"
          :offset="index > -1 ? 3 : 0"
        >
        <car :imageurl="url[1]" />
        </el-col>
      </el-row>
      </el-main>
      <el-footer id="FooterBack">
      <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight"></foo>
      </el-footer>
    </el-container>
  </div>
</template>
<script>
  import car from './components/MsgCard.vue'
  import Navigator from './components/NavigationBar.vue'
  import foo from './components/FooterGrid.vue'
  export default {
    data() {
      return {
        url:["https://th.bing.com/th/id/R.d6d3aae7006611f68786a47e377c39ea?rik=7IrzMCwE5z2KgQ&riu=http%3a%2f%2fpic.ntimg.cn%2f20131028%2f13984383_171843651115_2.jpg&ehk=4SCA2042hzkkZofnLUSML2WgVzwz9RMXyKkXwc2zHG0%3d&risl=&pid=ImgRaw&r=0","https://th.bing.com/th/id/R.0dd6c1000fa35050a64655170c58f883?rik=mK5hurvwok%2bA8g&pid=ImgRaw&r=0"],
        ButtonLeft:"HomePage",
        ButtonRight:"管理"
      }
    },
    components: {Navigator,foo,car},
    provide() {
      return {
        message:'/info',
        messageFooLeft:'/',
        messageFooRight:'/Manage'
      }
    }
  }

</script>
<style scoped>
.el-container{
    height: 100vh;
}
#headerBack{
   margin-bottom: 20px;
   background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;

    background-size: cover;
}
#MainBack{
   background:linear-gradient(120deg, yellow 0%, silver 100%);
   background-size: cover;
}
#FooterBack{
  background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat;
  background-size: cover;
}
</style>