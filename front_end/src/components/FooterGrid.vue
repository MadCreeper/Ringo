
<template>
  <el-row justify="space-between">

    <div class="left">

        <button :href="href" @click="redirectLeft" class="footer_button" role="button">他人求助🙏</button>

    </div>

    <div class="center">
     
        <button :href="href" @click="redirectMid" class="button-mid" role="button">+</button>

    </div>


    <div class="right">
     
        <button :href="href" @click="redirectRight" class="footer_button" role="button">我的提供👍</button>

    </div>

  </el-row>
</template>
<script>
export default {
  inject: ['messageFooLeft', 'messageFooRight', 'messageFooMid'],
  props: {
    ButtonLeft: String,
    ButtonRight: String,
  },
  methods: {
    redirectLeft() {
      this.$router.push(this.messageFooLeft)
    },
    redirectRight() {
      this.$router.push(this.messageFooRight)
    },
    redirectMid() {
      this.$router.push(this.messageFooMid)
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
.grid-content {
  border-radius: 4px;
  min-height: 100px;
  justify-content: center;
  display: flex;
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
.left {
  display: flex;
  justify-content: flex-start;
}
.center {
  display: flex;
  justify-content: center;
}
.right {
  display: flex;
  justify-content: flex-end;
}
/* CSS */
.footer_button {
  align-items: center;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: .75rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui, -apple-system, system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
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
  width: 35vw;
  white-space: nowrap;
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

/* CSS */
.button-mid {
  align-items: center;
  background-color: #a4ffb8;
  border: 0;
  border-radius: 50%;
  box-sizing: border-box;
  color: #000000;
  cursor: pointer;
  display: inline-flex;
  font-family: -apple-system, system-ui, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell, "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif;
  font-size: 30px;
  font-weight: 1000;
  justify-content: center;
  line-height: 20px;
  max-width: 50px;
  min-height: 40px;
  min-width: 0px;
  overflow: hidden;
  padding: 0px;
  padding-left: 15px;
  padding-right: 15px;
  text-align: center;
  touch-action: manipulation;
  transition: background-color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, box-shadow 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
}

.button-mid:hover,
.button-mid:focus { 
  background-color: #16437E;
  color: #ffffff;
}

.button-mid:active {
  background: #09223b;
  color: rgb(255, 255, 255, .7);
}

.button-mid:disabled { 
  cursor: not-allowed;
  background: rgba(0, 0, 0, .08);
  color: rgba(0, 0, 0, .3);
}
</style>

