<template>
  
  <el-row>
  </el-row>
  <el-row>
  </el-row>
    <el-row :gutter="20">
    <el-col :span="6" :offset="6"
      ><div class="grid-content ep-bg-purple"
    /></el-col>
    <el-col :span="6" :offset="6"
      ><div class="grid-content ep-bg-purple"
    /></el-col>
  </el-row>
  <el-row :gutter="24">
    <el-col :span="8">
      <div class="grid-content ep-bg-purple">
        <DropDown></DropDown>
      </div>
    </el-col>
    <el-col :span="12">
      <div class="grid-content ep-bg-purple">
        <SearchBox></SearchBox>
      </div>
    </el-col>
    <el-col :span="2">
      <div>
        <AvaterUsr></AvaterUsr>
      </div>
    </el-col>
  </el-row>
  
</template>
<script>
import DropDown from './DropDown.vue'
import SearchBox from './SearchBox.vue'
import AvaterUsr from './AvaterUser.vue'
export default {
  data() {
    return {
      msg: "Tag",
    }
  },
  components: { DropDown, SearchBox, AvaterUsr },
}

</script>
<style scoped>
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
}
</style>
