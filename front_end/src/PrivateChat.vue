<template>
    <el-container>
        <el-page-header @back="goBack">
            <template #content>
                <span class="text-large font-600 mr-3"> Chat with 张三 </span>
            </template>
        </el-page-header>
        <el-main>
            <el-row class="row-bg" justify="end" gutter="50">
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="success" round>大家好啊，我是说的道理</el-button>
                    </div>
                </el-col>
                <el-col :span="4" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
            </el-row>

            <el-row class="row-bg" justify="end" gutter="50">
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="success" round>今天来点大家想看的东西啊</el-button>
                    </div>
                </el-col>
                <el-col :span="4" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
            </el-row>

            <el-row class="row-bg">
                <el-col :span="1" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="primary" round>义！乌！</el-button>
                    </div>
                </el-col>
            </el-row>

            <el-row class="row-bg" justify="end" gutter="50">
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="success" round>哥们在这给你说唱🐴</el-button>
                    </div>
                </el-col>
                <el-col :span="4" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
            </el-row>

            <el-row class="row-bg">
                <el-col :span="1" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="primary" round>L T C</el-button>
                    </div>
                </el-col>
            </el-row>

            <el-row class="row-bg">
                <el-col :span="1" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="primary" round>理塘丁真!</el-button>
                    </div>
                </el-col>
            </el-row>

            <el-row class="row-bg">
                <el-col :span="1" :offset="1">
                    <el-avatar class="avater" :size="large" :src="circleUrl" @click="redirect"></el-avatar>
                </el-col>
                <el-col :span="6">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="primary" round>
                            哥们名叫丁真 Smokin' 'round, e-cigarettes new 我的小马名字叫珍珠
                        </el-button>
                    </div>
                </el-col>
            </el-row>

            <el-row>
                <bubble-chat :position="chatPosition" :messages="messagesList" :text-field="'message'"
                    :sender-name-field="'username'" :avatar-link-field="'iconUrl'">
                </bubble-chat>
            </el-row>

        </el-main>
        <!-- Footer -->
        <el-footer>
            <el-row class="row-bg" justify="end">
                <el-col :span="20" :offset="1">
                    <el-input v-model="input" placeholder="Please input" />
                </el-col>
                <el-col :span="3">
                    <div class="grid-content ep-bg-purple">
                        <el-button type="primary" round>发送</el-button>
                    </div>
                </el-col>
            </el-row>
        </el-footer>
    </el-container>
</template>

<script setup>

import { reactive, toRefs } from 'vue'

const state = reactive({
    circleUrl:
        'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
})
const { circleUrl } = toRefs(state);



</script>

<style scoped>
.el-container {
    min-height: 100vh;
}

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 50px;
}
</style>