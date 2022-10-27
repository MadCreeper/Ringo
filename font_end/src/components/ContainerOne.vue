<!-- This is for HomePage -->
<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
        <Navigator :msg="redirect" />
      </el-header>

      <el-main>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>急需N95口罩</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">医疗</el-tag>
                  <el-tag class="ml-2" type="warning">口罩</el-tag>
                  <el-tag class="ml-2" type="danger">非常紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              口罩用完了，需要口罩，谢谢！<br>
              地址：东上院123
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>有没有薯片</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">食品</el-tag>
                  <el-tag class="ml-2" type="warning">零食</el-tag>
                  <el-tag class="ml-2" type="danger">普通</el-tag>
                </div>
              </div>
            </template>
            <div>
              被封了无聊，想吃薯片🤤 <br>
              地址：西11
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>矿泉水喝完了</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">饮用品</el-tag>
                  <el-tag class="ml-2" type="warning">水</el-tag>
                  <el-tag class="ml-2" type="danger">较紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              饮水机坏了，被封着快没水了。<br>
              地址：东3
            </div>
          </el-card>
        </el-row>
      </el-main>

      <el-footer id="FooterBack">
        <foo></foo>
      </el-footer>
    </el-container>
  </div>
</template>
<script>
import foo from './FooterGrid.vue'
import Navigator from './NavigationBar.vue'
export default {
  components: { foo, Navigator },
  provide() {
    return {
      message: '/info'
    }
  }
}
</script>
<style scoped>
#headerBack {
  margin-bottom: 20px;
  background: #fff url("https://img.acgncyw.xyz/i/2022/06/10/62a260a28440c.jpg") no-repeat;
  background-size: cover;
}

#MainBack {
  background: #fff url("https://img01.vgtime.com/game/cover/2017/09/05/170905151615583.jpg") no-repeat;
  background-size: cover;
}

#FooterBack {
  background: #fff;
  background-size: cover;
}

.el-container {
  min-height: 100vh;
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
  justify-content: flex-end;
  align-items: center;
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