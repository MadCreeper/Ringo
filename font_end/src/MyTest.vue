<template>
  <el-container>
    <el-header>
      header
    </el-header>
  <el-main>
          <el-card>
            <div v-snip:js="3">
              {{long_str_cn}}
            </div>
            
          </el-card>
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
      long_str: "Pippa Passes, verse drama in four parts by Robert Browning, published in 1841. The poem’s sections—Morning, Noon, Evening, and Night—are linked by episodes that either comment on the preceding scene or presage the scene to follow. On New Year’s morning, her only holiday for the entire year, Pippa, an impoverished young silk-winder, sings as she wanders aimlessly. In each section of the poem, people who are at critical points in their lives make significant and far-reaching decisions when they hear Pippa sing as she passes by.",
      long_str_cn: "噫吁嚱，危乎高哉！蜀道之难，难于上青天！蚕丛及鱼凫，开国何茫然！尔来四万八千岁，不与秦塞通人烟。西当太白有鸟道，可以横绝峨眉巅。地崩山摧壮士死，然后天梯石栈相钩连。上有六龙回日之高标，下有冲波逆折之回川。黄鹤之飞尚不得过，猿猱欲度愁攀援。青泥何盘盘，百步九折萦岩峦。扪参历井仰胁息，以手抚膺坐长叹。",
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
