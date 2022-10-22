<!-- This is for HomePage -->
<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px" >
      <Navigator :msg="redirect"/>
      </el-header>
      <el-main>
      <container_2></container_2>
      </el-main>
      <el-footer id="FooterBack" height="200px"> <foo :ButtomLeft="ButtomLeft" :ButtomRight="ButtomRight" ></foo></el-footer>
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
      ButtomLeft:"求助",
      ButtomRight:"我的提供"  
      }
    },
    provide() {
      return {
        message:'/info'
      }
    }
  }
</script>
<style>
#headerBack{
  margin-bottom: 20px;
  background: #fff url("https://img.acgncyw.xyz/i/2022/06/10/62a260a28440c.jpg") no-repeat;
  background-size: cover;
}
#MainBack{
  background: #fff url("https://img01.vgtime.com/game/cover/2017/09/05/170905151615583.jpg") no-repeat;
  background-size: cover;
}
#FooterBack{
  background: #fff url("https://th.bing.com/th/id/R.d81c802b864899b019683c1b359e44fb?rik=D%2bEDqLxJgOxclA&riu=http%3a%2f%2fi0.hdslb.com%2fbfs%2farchive%2f69df8e0c73301dadbb4fd7c511312a1b81fb3746.jpg&ehk=OvjNiaQ1tIVT2likwAi5cn%2fkvem3yvud4oBOxd4QZGI%3d&risl=&pid=ImgRaw&r=0") no-repeat;
  background-size: cover;
}
</style>