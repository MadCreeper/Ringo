<!-- This is for ManagePage -->
<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
        <Navigator :msg="redirect" />
      </el-header>
      <el-main id="MainBack">
      <container_2></container_2>
      </el-main>
      <el-footer id="FooterBack" height="200px"> <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight" ></foo></el-footer>
    </el-container>
  </div>
</template>
<script>
    import foo from './FooterGrid.vue'
    import Navigator from './NavigationBar.vue'
    import container_2 from'./ContainerTwo.vue'
    export default {
    components: {foo,Navigator,container_2},
    data() {
      return {
      ButtonLeft:"HomePage",
      ButtonRight:"我的提供"  
      }
    },
    provide() {
      return {
        message:'/info',
        messageFooLeft:'/',
        messageFooRight:'/offer'
      }

    }
  }
</script>
<style  scoped>
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



.flex-container {
  display: flex;
}

.card-header-title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header-tags {
  display: flex;
  margin-left: auto;
  align-items: center;
  gap: 10px;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 100vw;
}
</style>