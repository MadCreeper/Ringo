<template>
  <el-row :gutter="24">
    <el-col :span="9">
    <el-card :body-style="{ padding: '0px' }">
      <div class="grid-content" style="padding: 50px">
          <div id="child">求助</div>
      </div>
    </el-card>
    </el-col>
    <el-col :span="6">
    <el-card :body-style="{ padding: '0px' }">
    <div class="grid-content">
    <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path fill="currentColor" d="M352 480h320a32 32 0 1 1 0 64H352a32 32 0 0 1 0-64z"></path><path fill="currentColor" d="M480 672V352a32 32 0 1 1 64 0v320a32 32 0 0 1-64 0z"></path><path fill="currentColor" d="M512 896a384 384 0 1 0 0-768 384 384 0 0 0 0 768zm0 64a448 448 0 1 1 0-896 448 448 0 0 1 0 896z"></path></svg>
    </div>
    </el-card>
    </el-col>

    <el-col :span="9">
    <el-card :body-style="{ padding: '0px' }">
    <div class="grid-content" style="padding: 50px">
      <div id="child">我的提供</div>
    </div>
    </el-card>
    </el-col>
  </el-row>
</template>
<script>
  export default {
    data() {
      return {
        msg:"Tag",
      }
    },
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
  min-height: 100px;
  justify-content: center;
  display:flex;
}

.image {
  width: 100%;
  display: block;
  
}
#child{

  font-size:24px;
  align-items: center;
}
</style>
