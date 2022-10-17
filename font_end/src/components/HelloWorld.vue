<template>
  <el-row :gutter="20">
    <el-col :span="16"><div class="grid-content ep-bg-purple" >
    <div
        class="radius"
        :style="{
          borderRadius: --el-border-radius-round
        }"
      ><ButtonGrp></ButtonGrp></div>
      </div>
    </el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple">
      <ButtonGrp >{{msg}}</ButtonGrp>
      </div>
    </el-col>
  </el-row>
  <el-row :gutter="20">
    <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="8"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
  </el-row>
  <el-row :gutter="20">
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="16"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="4"><div class="grid-content ep-bg-purple" /></el-col>
  </el-row>
</template>
<script>
  import ButtonGrp from './ButtonGrp.vue'
  export default {
    data() {
      return {
        msg:"Tag"
      }
    },
    components: {ButtonGrp},
  }

</script>
<style>
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
  min-height: 36px;
}
</style>
