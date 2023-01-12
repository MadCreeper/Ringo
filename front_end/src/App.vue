 <template>
    <div id="app">
        <transition :name="transitionName">
            <router-view class="router-view" />
        </transition>
    </div>
</template>
 
<script>
    export default {
        data() {
            return {
                transitionName: 'slide-left'
            }
        },
        watch: {
            //使用watch 监听$router的变化
            $route(to, from) {
                console.log(to,from)
                // 有主级到次级
                if (to.meta.index > from.meta.index) {
                    this.transitionName = 'fold-left' // 向左滑动
                } else if (to.meta.index < from.meta.index) {
                    // 由次级到主级
                    this.transitionName = 'fold-right'
                } else {
                    this.transitionName = ''   //同级无过渡效果
                }
                console.log(this.transitionName)
            }
        }
    }
</script>
 
<style>
html,body,#app {
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
  margin: 0;
  padding: 0;
  overflow: auto;
}

.fold-left-enter-active {
    animation-name: fold-left-in;
    animation-duration: .3s;
  }
  .fold-left-leave-active {
    animation-name: fold-left-out;
    animation-duration: .3s;
  }
  @keyframes fold-left-in {
    0% {
      -webkit-transform: translate3d(100%, 0, 0);
      transform: translate3d(100%, 0, 0);
      /* visibility: visible; */
    }
    /*50% {
      transform: translate3d(50%, 0, 0);
    }*/
    100% {
      -webkit-transform: translate3d(0, 0, 0);
      transform: translate3d(0, 0, 0);
    }
  }
  @keyframes fold-left-out {
    0% {
      -webkit-transform: translate3d(0, 0, 0);
      transform: translate3d(0, 0, 0);
    }
    /*50% {
      transform: translate3d(-50%, 0 , 0);
    }*/
    100% {
      -webkit-transform: translate3d(-100%, 0, 0);
      transform: translate3d(-100%, 0, 0);
      /* visibility: hidden; */
    }
  }
  .fold-right-enter-active {
    animation-name: fold-right-in;
    animation-duration: .3s;
  }
  .fold-right-leave-active {
    animation-name: fold-right-out;
    animation-duration: .3s;
  }
  @keyframes fold-right-in{
    0% {
      width: 100%;
      -webkit-transform: translate3d(-100%, 0, 0);
      transform: translate3d(-100%, 0, 0);
      /* visibility: visible; */
    }
    /*50% {
      transform: translate3d(50%, 0, 0);
    }*/
    100% {
      width: 100%;
      -webkit-transform: translate3d(0, 0, 0);
      transform: translate3d(0, 0, 0);
    }
  }
  @keyframes fold-right-out  {
    0% {
      width: 100%;
      -webkit-transform: translate3d(0, 0, 0);
      transform: translate3d(0, 0, 0);
    }
    /*50% {
      transform: translate3d(-50%, 0 , 0);
    }*/
    100% {
      width: 100%;
      -webkit-transform: translate3d(100%, 0, 0);
      transform: translate3d(100%, 0, 0);
      /* visibility: hidden; */
    }
  }
</style>