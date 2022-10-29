<template>
  <div class="demo-image">
    <div  class="block">
      <el-image style="width: 1400px; height: 130px" :z-index=4 :src=url :fit=fit />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    url:String,
    fit:String
  }
}
</script>

<style scoped>
.demo-image .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 20%;
  box-sizing: border-box;
  vertical-align: top;
}
.demo-image .block:last-child {
  border-right: none;
}
.demo-image .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}
</style>