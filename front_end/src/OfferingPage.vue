<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
       <el-row>
        <el-col :span=6>
          <div>   
          <img src="http://127.0.0.1:8000/media_url/ringo_new.png" width="90" />
        </div>
        </el-col>
        <el-col :span=16>
        </el-col>
        <el-col :span=2>
       <div class="container">
        <div class="sunny"></div>
        </div>
        </el-col>
        </el-row>
        <div class="header-bottom force-bottom">
          <el-row :gutter="20" type="flex">
            <el-col :span="1" :offset="21" type="flex">
              <div class="x-right">
              <el-avatar class="avater" size=80 :src=this.info.avatar @click="redirect"></el-avatar>
            </div>
            </el-col>

          </el-row>
        </div>
      </el-header>
      <el-main id="MainBack">
        <div>
          <el-space :fill="fill" wrap :size=30>
            <el-card @click="gotoDetails(offering.goods_sn)" v-bind:class="{ 'box-card': fill, 'box-card-fold': !fill }"
              v-for="offering in offerings" :key="offering">
              <template #header>
                <div v-bind:class="{ 'card-header': fill, 'card-header-fold': !fill }">
                  <!-- switch styles for fill or not fill -->
                  <div class="name">
                    <span>{{ offering.name }}</span>
                  </div>
                  <div class="line-break"></div>

                  <div class="tags">
                    <el-tag class="ml-2" type="success" v-if="offering.category">{{ offering.category.name }}</el-tag>
                  </div>

                  <div class="line-break"></div>


                  <!-- <div class="tags">
                    <div v-for="tag in offering.tags" :key="tag">
                      <el-tag class="ml-2" type="success">{{ tag }}</el-tag>
                    </div>
                  </div> -->

                </div>
                <div class="username-display">
                  <!-- 用户：{{ offering.user }} -->
                </div>
              </template>
              <!-- user name -->
              <div>

              </div>

              <!-- 简介 -->
              <div v-snip:js="5">
                简介：{{ offering.goods_brief }}
              </div>
              <div>
                <el-icon>
                  <House />
                </el-icon> {{ "地址: " + offering.address }}
              </div>
              <div class="image" v-if="offering.goods_desc">
                <!-- {{offering.goods_desc}} -->
                <!-- <img :src="`${offering.goods_desc}`" class="img-display" /> -->
                <!-- <img src="https://th.bing.com/th/id/OIP.4JFkvRdf4hqfBMwSarhqSgHaE8?pid=ImgDet&rs=1" class="img-display" /> -->
              </div>

              <div class="submit-time">
                {{ formatDateTime(offering.add_time) }}
              </div>


            </el-card>
          </el-space>
        </div>
      </el-main>
      <el-footer id="FooterBack">
        <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight"></foo>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
// import car from './components/MsgCard.vue'
// import Navigator from './components/NavigationBar.vue'
import foo from './components/FooterGrid.vue'
import { getOffering } from '../api/api';
import { formatDateTime } from './utils'
import {getUserDetail} from '../api/api.js'
import { reactive } from 'vue'
export default {
  data() {
    return {
      offerings: [],
      url: ["https://th.bing.com/th/id/R.d6d3aae7006611f68786a47e377c39ea?rik=7IrzMCwE5z2KgQ&riu=http%3a%2f%2fpic.ntimg.cn%2f20131028%2f13984383_171843651115_2.jpg&ehk=4SCA2042hzkkZofnLUSML2WgVzwz9RMXyKkXwc2zHG0%3d&risl=&pid=ImgRaw&r=0", "https://th.bing.com/th/id/R.0dd6c1000fa35050a64655170c58f883?rik=mK5hurvwok%2bA8g&pid=ImgRaw&r=0"],
      ButtonLeft: "HomePage",
      ButtonRight: "管理",
      info:reactive({
                owner:"",
                nickname:"",
                avater:"",
                address:"",
                signature:""
        }),
    }
  },
  components: { foo },
  mounted: function () {
    this.loadOfferings();
    this.loadinfo();
  },
  methods: {
    redirect(){
      this.$router.push('/info')
    },
    loadOfferings() {
      getOffering().then(response => {
        this.offerings = response.data.results;
        console.log("offerings:")
        console.log(this.offerings)
        // if (this.offering.goods_desc===""){
        //     this.offering.goods_desc="https://th.bing.com/th/id/OIP.4JFkvRdf4hqfBMwSarhqSgHaE8?pid=ImgDet&rs=1"
        // }
      })
        .catch(
          err => {
            console.log(err)
            this.$router.push('/login')
          }
        )
    },
    loadinfo() {
      getUserDetail().then(response => {
        this.info = response.data;
        this.info.avatar="http://127.0.0.1:8000"+response.data.avatar;
        console.log("info:")
        console.log(this.info.avatar)
      })
      .catch(
        err => {
          console.log(err)
          this.$router.push('/login')
        }
      )
    },
    gotoDetails(item_id) {
      setTimeout(()=>{this.$router.push({
        path: '/offerdetails',
        query: {
          id: item_id
        }
      })},600)
      console.log("test details")
    },
    formatDateTime,
  },
  provide() {
    return {
      message: '/info',
      messageFooLeft: '/',
      messageFooRight: '/offer',
      messageFooMid: '/submitoffer'
    }
  },

}
</script>
<style scoped>
.el-header {
  display: flex;
  flex-direction: column;
}

.el-container {
  height: 100vh;
}

.box-card {
  width: 80vw;
  text-overflow: ellipsis;
}

.box-card-fold {
  width: 35vw;
  height: fit-content;
  text-overflow: ellipsis;
}

.card-header {
  display: flex;
  flex-direction: row;
}

.card-header .name {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header .tags {
  display: flex;
  margin-left: auto;
  align-items: center;
  gap: 10px;
}

.card-header-fold {
  display: flex;
  flex-direction: column;
}

.card-header-fold .name {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header-fold .tags {
  width: 100%;
  display: flex;
  margin-left: auto;
  align-items: flex-start;
  gap: 5px;
}

.username-display {
  font-size: small;
  color: dimgray;
}

.submit-time {
  text-align: right;
  font-size: smaller;
  color: dimgray;
}

.img-display {
  width: 80%;
  height: 80%;
}

#headerBack {
  margin-bottom: 5px;
  background: #a1d9ea url("https://i.328888.xyz/2022/12/29/UPVpL.png") center center no-repeat;
  background-position: center;
  background-size: cover;
  background-size: auto 100%;
}

#MainBack {
  background: linear-gradient(0deg, rgb(213, 255, 216) 0%, rgb(240, 240, 240) 100%);
  background-size: cover;
}

#FooterBack {
  /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
  background-size: cover;
}
.el-card ::v-deep .el-card__header {
  padding: 10px 10px;
  background-color: rgb(189, 246, 200);
}

.el-card ::v-deep .el-card__body {
  padding: 10px;
  background-color: white;

}

.card-header-fold {
  display: flex;
  flex-direction: column;
}

.card-header-fold .name {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.card-header-fold .tags {
  width: 100%;
  display: flex;
  margin-left: auto;
  align-items: flex-start;
  gap: 5px;
}

.username-display {
  font-size: small;
  color: dimgray;
}

.submit-time {
  text-align: right;
  font-size: smaller;
  color: dimgray;
}

.el-card {
  position: relative;
    /*子溢出父元素隐藏 这样hover子元素的时候 不算hover父元素*/
  overflow: hidden;
}
.el-card::after{
    content: "";
    position: absolute;
    /*首先隐藏子元素*/
    left: -100%;
    top: 0;
    /*设置和父元素一样大*/
    width: 100%;
    height: 100%;
    /*添加从左往右的渐变 即模仿光照效果*/
    background-image: -webkit-linear-gradient(0deg,hsla(0,0%,100%,0),hsla(0,0%,100%,.5),hsla(0,0%,100%,0));
    background-image: linear-gradient(to right,hsla(0,0%,100%,0),hsla(0,0%,100%,.5),hsla(0,0%,100%,0));
    /*光照是斜着的更好看*/
    -o-transform: skewx(-25deg);
    -moz-transform: skewx(-25deg);
    -webkit-transform: skewx(-25deg);
    transform: skewx(-25deg);
    /*添加动画效果*/
    transition: all .3s ease;
    &:active {
      left: 100%;
    }
}
.el-card:active{
  -moz-transform: translateY(-6px);
  -webkit-transform: translateY(-6px);
  transform: translateY(-6px);
  /*添加一个淡一点的阴影*/
  -moz-box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
  -webkit-box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
  box-shadow: 0 26px 40px -24px rgba(0,36,100,.5);
}
.el-card:hover::after {
    /*鼠标放在父元素上 移动子元素*/
    left: 100%;
}


#headerBack {
  margin-bottom: 5px;
  background: #a1d9ea url("https://i.328888.xyz/2022/12/29/UPVpL.png") center center no-repeat;
  background-position: center;
  background-size: cover;
  background-size: auto 100%;
}

#MainBack {
  background: rgb(229, 250, 231);
  background-size: cover;
}

#FooterBack {
  /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
  background: rgb(229, 250, 231);
  background-size: cover;
}

.container{
    width: 40px;
    height: 40px;
}
.sunny{
    width: 10px;
    height: 70px;
    position: absolute;
    background: -webkit-linear-gradient(top, rgba(255,255,255,0) 0%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 100%);
    animation: sunny 15s linear infinite;
}

@keyframes sunny {
    0%{
        transform: rotate(0deg);
    }
    100%{
        transform: rotate(360deg);
    }
}
.sunny::before{
    content: '';
    width: 10px;
    height: 70px;
    position: absolute;
    bottom: 0;
    left: 0;
    background: -webkit-linear-gradient(top, rgba(255,255,255,0) 0%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0) 100%);
    transform: rotate(90deg)
}
.sunny::after{
    content: '';
    width: 40px;
    height: 40px;
    position: absolute;
    top: 15px;
    left: -15px;
    background: #ffee44;
    border-radius: 50%;
    box-shadow: rgba(255,255,0,0.2) 0 0 0 15px;
}
.image{
  align:auto;
}
</style>



<style src="./css/header.css"  lang="css" scoped />