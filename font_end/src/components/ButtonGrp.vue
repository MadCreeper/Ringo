<template>
    <el-button type="primary" :icon="ArrowLeft"><slot>Previous Page</slot></el-button>
    <el-button type="primary">
      Next Page<el-icon class="el-icon--right"><ArrowRight /></el-icon>
    </el-button>
</template>
<script setup>

import {
  ArrowLeft,
  ArrowRight,
} from '@element-plus/icons-vue'
</script>