<template>
    <el-container>
        <!-- <el-header id="headerBack" height="200px" >
      <Navigator :msg="redirect"/>
      </el-header> -->
        <el-main id="MainBack" height="200px">
            <div class="box">
                <div class="left"></div>
                <div class="right">
                    <h4>登陆</h4>
                    <form action="" method="post" class="word">
                        <input v-model="this.sendform.username" class="acc" name="user" type="text"
                            placeholder="用户名或邮箱">
                        <input v-model="this.sendform.password" class="acc" name="password" type="password"
                            placeholder="密码">
                        <input class="submit" type="button" :value=flag @click="this.onSubmit(this.sendform)">
                    </form>
                    <div class="fn">
                        <a @click="register">注册账号</a>
                        <a @click="changecode">修改密码</a>
                    </div>
                </div>
            </div>
        </el-main>
        <!-- <el-footer id="FooterBack" height="200px"> <foo :ButtonLeft="ButtonLeft" :ButtonRight="ButtonRight" ></foo></el-footer> -->
    </el-container>
</template>
<script>
// const reciveform = reactive({
//     errcode:0,
//     username:"",
//     password:"",
//     email:"",
//     veriCode:""
// })
import { reactive } from 'vue'

import { login } from '../api/api.js'

export default {
    data() {
        return {
            flag: "提交",
            check: false,
            sendform: reactive({
                username: "",
                password: "",
            }),
            reciveform: reactive({
                token: "",
                username: "",
                password: "",
                email: "",
                veriCode: ""
            }),
        }
    },
    methods: {
        register() {
            this.$router.push('/register')
        },
        changecode() {
            this.$router.push('/changecode')
        },
        onSubmit(params) {

            login(params).then(response => {
                console.log(response.status)
                this.reciveform = response.data
                window.localStorage["token"] = response.data.token;
                this.$router.push('/')
            }).catch(
                err => {
                    console.log(err.code)
                    alert("用户密码不匹配,验证未通过")
                    window.localStorage.removeItem("token")
                    this.$router.go(0)

                }
            )
        }

    }
}

</script>


<style scoped>
.el-container {
    height: 100vh;
}

#headerBack {
    margin-bottom: 20px;
    background: #fff url("https://uploadfile.bizhizu.cn/up/cc/d0/87/ccd08766b03deca06263f0d8e0013dec.jpg") no-repeat;

    background-size: cover;
}

#MainBack {
    background: linear-gradient(120deg, yellow 0%, silver 100%);
    background-size: cover;
}

#FooterBack {
    background: #fff url("https://th.bing.com/th/id/OIP.Oc9mYdpG25SBa-pRljEXwAHaEK?pid=ImgDet&w=1500&h=844&rs=1") no-repeat;
    background-size: cover;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


::selection {
    color: #fff;
    background-color: rgb(144, 129, 241);

}

.box {
    display: flex;
    overflow: hidden;
    width: 100%;
    height: 45rem;
    background-color: rgba(255, 255, 255, 60%);
    border-radius: 1.5rem;
    margin: 20% auto;
    box-shadow: 0 0 1rem 0.2rem rgb(0 0 0 / 10%);
}

.box .left {
    position: relative;
    width: 35%;
    height: 100%;
    background-color: skyblue;
}

.box .left::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url('https://pic1.zhimg.com/v2-28f5d10308b566daab63c3b6774fc5f5_r.jpg?source=1940ef5c');
    background-size: cover;
    opacity: 80%;
}

.box .right {
    display: flex;
    width: 65%;
    flex-direction: column;
    align-items: center;
}

.box .right h4 {
    color: #8ec5fc;
    font-size: 3rem;
    margin-top: 5rem;
}

.box .right form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.box .right form .acc {
    outline: none;
    width: 80%;
    height: 3rem;
    font-size: 1.6rem;
    margin-top: 3rem;
    padding: 1rem 0 0 1.6rem;
    border: none;
    border-bottom: 1px solid rgb(144, 129, 241);
    color: rgb(144, 129, 241);
    background-color: rgba(0, 0, 0, 0);
}

.right form .acc:focus {
    outline: none;
    color: rgb(144, 129, 241);
    padding: 1rem 0 0 1.6rem;
}

.right .submit {
    width: 60%;
    height: 5rem;
    color: black;
    background-image: linear-gradient(120deg, yellow 0%, Gold 100%);
    font-size: 1.4rem;
    border: none;
    border-radius: 0.5rem;
    margin: 6rem 0 0 50%;
    transform: translateX(-50%);
}

.right .submit:hover {
    box-shadow: 0 0 2rem -0.5rem rgb(0 0 0 / 15%);
}

.right .fn {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
    width: 70%;
}

.right .fn a {
    font-size: 1.3rem;
    margin-top: 5rem;
    padding: 1rem 2rem;
    color: #666;
}

.right .fn a:hover {
    color: rgb(144, 129, 241);
}

.toptop {
    content: '';
    width: 100%;
    height: 100%;
    position: fixed;
    z-index: 1;
    background: linear-gradient(120deg, yellow, Aquamarine 40%, Gold);
    background-image: url('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fztd00.photos.bdimg.com%2Fztd%2Fw%3D700%3Bq%3D50%2Fsign%3D5d7ecfed741ed21b79c92ce59d55acf9%2Feaf81a4c510fd9f90dc00b762c2dd42a2934a4de.jpg&refer=http%3A%2F%2Fztd00.photos.bdimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1637930535&t=11bd372b5beab1f7c62c2210cf917749');
}

.top {
    width: 100px;
    height: 200px;
    background-image: url('https://proxy-jp1.pixivel.moe/img-original/img/2021/10/25/17/58/36/93677700_p0.jpg');
    background-size: cover;
    opacity: 80%;
    position: absolute;
    left: 100px;
    top: 700px;
    animation: mymove 10s infinite;
    -webkit-animation: mymove 10s infinite;
    /*Safari and Chrome*/
}
</style>