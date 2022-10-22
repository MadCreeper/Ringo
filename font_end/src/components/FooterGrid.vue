<template>
  <el-row :gutter="24">
    <el-col :span="9">
    <el-card id="card" :body-style="{ padding: '0px'}"> 
      <div id="footer" style="padding: 50px">
          <div>{{ButtomLeft }}</div>
      </div>
    </el-card>
    </el-col>
    <el-col :span="6">
    <el-card id="card" :body-style="{ padding: '0px' }">
    <div class="midbutton" >
    <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa=""><path fill="currentColor" d="M352 480h320a32 32 0 1 1 0 64H352a32 32 0 0 1 0-64z"></path><path fill="currentColor" d="M480 672V352a32 32 0 1 1 64 0v320a32 32 0 0 1-64 0z"></path><path fill="currentColor" d="M512 896a384 384 0 1 0 0-768 384 384 0 0 0 0 768zm0 64a448 448 0 1 1 0-896 448 448 0 0 1 0 896z"></path></svg>
    </div>
    </el-card>
    </el-col>
    <el-col :span="9">
    <el-card id="card" :body-style="{ padding: '0px' }">
    <div  id="footer" style="padding: 50px">
      <div id="child">{{ButtomRight}}</div>
    </div>
    </el-card>
    </el-col>
  </el-row>
</template>
<script>
  export default {
    props:{
      ButtomLeft:String,
      ButtomRight:String
    },
    data() {
      return {
        msg:"Tag",
      }
    },
  }

</script>
<style>
#card{
  background-color: transparent;
  border-radius: 12px;
  min-height: 120px;
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

#footer{
  min-height: 20px;
  border: 1px solid;
	background-color: transparent;
	text-transform: uppercase;
  font-size: 16px;
	padding: 10px 20px;
	font-weight: 300;
  color: #4cc9f0;
}

#card:hover{
  color: white;
	border: 0;
}
#footer:hover {
  color: white;
	border: 0;
  background-color: #4cc9f0;
	-webkit-box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
	-moz-box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
	box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
}

.midbutton:hover {
  color: white;
	border: 0;
  background-color: #b9e769;
  -webkit-box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
  -moz-box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
  box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
}
.image {
  width: 100%;
  display: block;
  
}
.midbutton{
  border-radius: 12px;
  min-height: 100px;
  border-radius: 4px;
  min-height: 100px;
  justify-content: center;
  color: #b9e769; 
  background-color: transparent;
  display:flex;
}
</style>
