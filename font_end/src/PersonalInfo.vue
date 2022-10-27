<template>
<div class="common-layout">
<el-container>
<el-main>
<el-row>
    <el-col :span="1"><el-icon><Back /></el-icon><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="8" @click="redirect">Back<div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="15"><div class="grid-content ep-bg-purple" /></el-col>
</el-row>
<el-row>
    <el-col :span="8"><AvaterUsr :AvaterSize="AvaterSize"></AvaterUsr><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="14"><InputForm></InputForm><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="2"><div class="grid-content ep-bg-purple" /></el-col>
</el-row>
<el-row>
    <el-col :span="2"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="8"><Uploader></Uploader><div class="grid-content ep-bg-purple-light" /></el-col>
    <el-col :span="10"><div class="grid-content ep-bg-purple" /></el-col>
</el-row>
</el-main>
</el-container>
</div>
<div class="common-layout">
<el-container>
<el-row>
<el-col :span="2"><div class="grid-content ep-bg-purple" /></el-col>
 <el-col :span="22"> 
<el-form :model="form" label-width="120px">
    <el-form-item label="Activity name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Activity zone">
      <el-select v-model="form.region" placeholder="please select your zone">
        <el-option label="Zone one" value="shanghai" />
        <el-option label="Zone two" value="beijing" />
      </el-select>
    </el-form-item>
    <el-form-item label="Activity time">
      <el-col :span="11">
        <el-date-picker
          v-model="form.date1"
          type="date"
          placeholder="Pick a date"
          style="width: 100%"
        />
      </el-col>
      <el-col :span="2" class="text-center">
        <span class="text-gray-500">-</span>
      </el-col>
      <el-col :span="11">
        <el-time-picker
          v-model="form.date2"
          placeholder="Pick a time"
          style="width: 100%"
        />
      </el-col>
    </el-form-item>
    <el-form-item label="Setting 1 ">
      <el-switch v-model="form.delivery" />
    </el-form-item>
    <el-form-item label="Setting 2">
      <el-switch v-model="form.delivery2" />
    </el-form-item>
    <el-form-item label="Setting 3">
      <el-switch v-model="form.delivery3" />
    </el-form-item>
    <el-form-item label="Activity type">
      <el-checkbox-group v-model="form.type">
        <el-checkbox label="Online activities" name="type" />
        <el-checkbox label="Promotion activities" name="type" />
        <el-checkbox label="Offline activities" name="type" />
        <el-checkbox label="Simple brand exposure" name="type" />
      </el-checkbox-group>
    </el-form-item>
    <el-form-item label="Resources">
      <el-radio-group v-model="form.resource">
        <el-radio label="Sponsor" />
        <el-radio label="Venue" />
      </el-radio-group>
    </el-form-item>
    <el-form-item label="Activity form">
      <el-input v-model="form.desc" type="textarea" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
  </el-col>
</el-row>
</el-container>
</div>
</template>
<script>
  export default {
  components: {Back,AvaterUsr,InputForm,Uploader},
  data() {
    return {
      AvaterSize:100,
    }
  },
  methods:{
    redirect(){
      this.$router.push('/')
    },
  },
  provide() {
    return {
      message:'/info'
    }
  }
  }
  import {
  Back,
} from '@element-plus/icons-vue'
  import AvaterUsr from './components/AvaterUser.vue'
  import InputForm from './components/InputForm.vue'
  import Uploader from './components/UploadImg.vue'
</script>
<script setup>
import { reactive } from 'vue'
// do not use same name with ref
const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,

  delivery2:false,
  delivery3:false,
  type: [],
  resource: '',
  desc: '',
})

const onSubmit = () => {
  console.log('submit!')
}
</script>
<style>
#Head{
  border: 1px solid;
}
#Avater{
  height:200px;
}
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

