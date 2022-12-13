<template>
  <div class="common-layout">
    <el-container>
      <el-header id="headerBack" height="200px">
        <Navigator :msg="redirect" />
      </el-header>
      <el-main id="MainBack">
        <div>
          <!-- <div style="margin-bottom: 15px">Switch:
            <el-switch v-model="fill" />
          </div> -->
          <el-space :fill="fill" wrap>
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
                {{ offering.goods_brief }}
              </div>
              <div>
                <el-icon>
                  <House />
                </el-icon> {{ "地址: " + offering.address }}
              </div>
              <div v-if="offering.goods_desc">
                <!-- {{offering.goods_desc}} -->
                <img :src="`${offering.goods_desc}`" class="img-display" />
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
import Navigator from './components/NavigationBar.vue'
import foo from './components/FooterGrid.vue'
import { getOffering } from '../api/api';
import { formatDateTime } from './utils'
export default {
  data() {
    return {
      offerings : [],
      url: ["https://th.bing.com/th/id/R.d6d3aae7006611f68786a47e377c39ea?rik=7IrzMCwE5z2KgQ&riu=http%3a%2f%2fpic.ntimg.cn%2f20131028%2f13984383_171843651115_2.jpg&ehk=4SCA2042hzkkZofnLUSML2WgVzwz9RMXyKkXwc2zHG0%3d&risl=&pid=ImgRaw&r=0", "https://th.bing.com/th/id/R.0dd6c1000fa35050a64655170c58f883?rik=mK5hurvwok%2bA8g&pid=ImgRaw&r=0"],
      ButtonLeft: "HomePage",
      ButtonRight: "管理"
    }
  },
  components: { Navigator, foo },
  mounted: function () {
    this.loadOfferings()
  },
  methods: {
    loadOfferings() {
      getOffering().then(response => {
        this.offerings = response.data.results;
        console.log("offerings:")
        console.log(this.offerings)
      })
        .catch(
          err => {
            console.log(err)
            this.$router.push('/login')
          }
        )
    },
    gotoDetails(item_id) {
      this.$router.push({
        path: '/offerdetails',
        query: {
          id: item_id
        }
      })
      console.log("test details")
    },
    formatDateTime,
  },
  provide() {
    return {
      message: '/info',
      messageFooLeft: '/',
      messageFooRight: '/Manage',
      messageFooMid: '/submitoffer'
    }
  },
  
}
</script>
<style scoped>
.el-container {
  height: 95vh;
}
.box-card {
  width: 80vw;
  text-overflow: ellipsis;
}
.box-card-fold {
  width: 40vw;
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
  margin-bottom: 20px;
  background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;
  background-size: cover;
}
#MainBack {
  background: linear-gradient(0deg, rgb(213, 255, 216) 0%, rgb(240, 240, 240) 100%);
  background-size: cover;
}
#FooterBack {
  /* background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat; */
  background-size: cover;
}
</style>