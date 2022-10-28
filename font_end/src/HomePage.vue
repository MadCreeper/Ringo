<!-- This is for ManagePage -->
<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px" >
      <Navigator :msg="redirect"/>
      </el-header>
      <el-main id="MainBack">
      <div>
    <div style="margin-bottom: 15px">Switch: <el-switch v-model="fill" /></div>
    <el-space :fill="fill" wrap>
      <el-card v-for="i in 4" :key="i" class="box-card">
        <template #header>
          <div class="card-header">
            <span>Title</span>
            <el-button class="button" text>Tags Attached</el-button>
          </div>
        </template>
        <div v-for="o in 4" :key="o" class="text item">
          {{ 'Text content ' + o }}
        </div>
      </el-card>
    </el-space>
  </div>
      </el-main>
      <el-footer id="FooterBack" height="200px"> <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight" ></foo></el-footer>
    </el-container>
  </div>
</template>
<script setup>
import { ref } from 'vue'

const fill = ref(true)
</script>
<script>
    import foo from './components/FooterGrid.vue'
    import Navigator from './components//NavigationBar.vue'
    export default {
    components: {foo,Navigator},
    data() {
      return {
      ButtonLeft:"求助",
      ButtonRight:"我的提供"  
      }
    },
    provide() {
      return {
        message:'/info',
        messageFooLeft:'/request',
        messageFooRight:'/offer'
      }
    }
  }
</script>
<style>

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