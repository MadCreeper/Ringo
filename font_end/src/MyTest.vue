<template>
  <el-container>
    <el-header>
      header
    </el-header>
  <el-main>
    <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>急需N95口罩</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">医疗</el-tag>
                  <el-tag class="ml-2" type="warning">口罩</el-tag>
                  <el-tag class="ml-2" type="danger">非常紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              口罩用完了，需要口罩，谢谢！<br>
              地址：东上院123
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>有没有薯片</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">食品</el-tag>
                  <el-tag class="ml-2" type="warning">零食</el-tag>
                  <el-tag class="ml-2" type="danger">普通</el-tag>
                </div>
              </div>
            </template>
            <div>
              被封了无聊，想吃薯片🤤 <br>
              地址：西11
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>矿泉水喝完了</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">饮用品</el-tag>
                  <el-tag class="ml-2" type="warning">水</el-tag>
                  <el-tag class="ml-2" type="danger">较紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              饮水机坏了，被封着快没水了。<br>
              地址：东3
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>矿泉水喝完了</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">饮用品</el-tag>
                  <el-tag class="ml-2" type="warning">水</el-tag>
                  <el-tag class="ml-2" type="danger">较紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              饮水机坏了，被封着快没水了。<br>
              地址：东3
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>矿泉水喝完了</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">饮用品</el-tag>
                  <el-tag class="ml-2" type="warning">水</el-tag>
                  <el-tag class="ml-2" type="danger">较紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              饮水机坏了，被封着快没水了。<br>
              地址：东3
            </div>
          </el-card>
        </el-row>

        <el-row>
          <el-card class="box-card">
            <template #header>
              <div class="flex-container">
                <div class="card-header-title">
                  <span>矿泉水喝完了</span>
                </div>
                <div class="card-header-tags">
                  <el-tag class="ml-2" type="success">饮用品</el-tag>
                  <el-tag class="ml-2" type="warning">水</el-tag>
                  <el-tag class="ml-2" type="danger">较紧急</el-tag>
                </div>
              </div>
            </template>
            <div>
              饮水机坏了，被封着快没水了。<br>
              地址：东3
            </div>
          </el-card>
        </el-row>
  </el-main>
  <el-footer>
  <el-row justify="space-between">
    
      <div class="left">
        <button class="footer_button" role="button">他人求助🙏</button>
      </div>      

      <div class="center">
        <button class="footer_button" role="button">➕</button>
      </div>

      <div class="right">
          <button class="footer_button" role="button">我的提供👍</button>
      </div>
    
  </el-row>
</el-footer>
</el-container>
</template>
<script>
export default {
  data() {
    return {
      msg: "Tag",
    }
  },
}

</script>
<style scoped>
.el-container{
  height: 100vh;
}
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  display : flex;
  border-radius: 4px;
}
.flex-container {
  display: flex;
}
.card-header-title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.card-header-tags {
  display: flex;
  margin-left: auto;
  align-items: center;
  gap: 10px;
}
.text {
  font-size: 14px;
}
.item {
  margin-bottom: 18px;
}
.grid-content {
  border-radius: 4px;
  min-height: 100px;
  justify-content: center;
  display: flex;
}

.image {
  width: 100%;
  display: block;

}
.left{
      display:flex;
      justify-content:flex-start;
}

.center{
      display:flex;
      justify-content:center;
}

.right{
      display:flex;
      justify-content:flex-end;
}
/* CSS */
.footer_button {
  align-items: center;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 20px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 3rem;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
  
}
.footer_button:hover,
.footer_button:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.footer_button:hover {
  transform: translateY(-1px);
}

.footer_button:active {
  background-color: #F0F0F1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}


#child {
  font-size: 24px;
  align-items: center;
}
</style>
