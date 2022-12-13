<template>
  <el-input
    v-model="textarea"
    :rows="4"
    type="textarea"
    placeholder="Something"
  />
</template>

<script setup>
import { ref } from 'vue'
const textarea = ref('')
</script>