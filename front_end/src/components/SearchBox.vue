<template>
<div class="mt-4">
    <el-input
      v-model="input"
      placeholder="Please input"
      class="input-with-select">
      <template #append>
        <el-button :icon="Search" />
      </template>
    </el-input>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
const input = ref('')
</script>

<style>
.input-with-select .el-input-group__prepend {
  background-color: var(--el-fill-color-blank);
}
</style>