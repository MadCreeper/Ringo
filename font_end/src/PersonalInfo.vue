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
      <el-footer id="FooterBack" height="200px">
      <foo></foo>
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
        url:["https://pic4.zhimg.com/80/v2-5d767d334ab6090faee137ab9c21513f_qhd.jpg","https://th.bing.com/th/id/OIP.qfyS8vjj2wHeOoHJ6sznUgHaKY?pid=ImgDet&rs=1"]
      }
    },
    components: {Navigator,foo,car},
    provide() {
      return {
        message:'/'
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