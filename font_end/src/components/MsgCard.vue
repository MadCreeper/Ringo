<template>
<el-card :body-style="{ padding: '0px' }">
<img
    :src=imageurl
    class="image"
/>
<div style="padding: 14px">
    <span>WhiteAblum2</span>
    <div class="bottom">
    <time class="time">{{ currentDate }}</time>
    <el-button text class="button">Operating</el-button>
    </div>
</div>
</el-card>
</template>

<script setup>
import { ref } from 'vue'

const currentDate = ref(new Date())
</script>
<script>
export default {
    props:{
        imageurl:String
    }
}
</script>
<style>

.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
</style>