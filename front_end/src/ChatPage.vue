<template>

    <!-- {{ this.roomid }}
    <el-button type="primary" @click="sendWebsocketMsg('hello')">Primary</el-button> -->
    <div>
        <beautiful-chat :participants="participants" :titleImageUrl="titleImageUrl" :onMessageWasSent="onMessageWasSent"
            :messageList="messageList" :newMessagesCount="newMessagesCount" :isOpen="isChatOpen" :close="closeChat"
            :icons="icons" :open="openChat" :showEmoji="true" :showFile="true" :showEdition="true" :showDeletion="true"
            :showTypingIndicator="showTypingIndicator" :showLauncher="true" :showCloseButton="true" :colors="colors"
            :alwaysScrollToBottom="alwaysScrollToBottom" :disableUserListToggle="false" :messageStyling="messageStyling"
            @onType="handleOnType" @edit="editMessage" />
    </div>
</template>
<script>


import { getChatHistory, getByUrl, resetUnreadMsg, addUnreadMsg, getUserPhoto} from '../api/api'



const wss_protocol = (window.location.protocol == 'https:') ? 'wss://' : 'ws://';


export default {
    data() {
        return {
            roomid: "",
            from: "",
            to: "",
            chatSocket: null,
            participants: [

            ], // the list of all the participant of the conversation. `name` is the user name, `id` is used to establish the author of a message, `imageUrl` is supposed to be the user avatar.
            titleImageUrl: 'https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png',
            messageList: [

            ], // the list of the messages to show, can be paginated and adjusted dynamically
            newMessagesCount: 0,
            isChatOpen: true, // to determine whether the chat window should be open or closed
            showTypingIndicator: '', // when set to a value matching the participant.id it shows the typing indicator for the specific user
            colors: {
                header: {
                    bg: '#4e8cff',
                    text: '#ffffff'
                },
                launcher: {
                    bg: '#4e8cff'
                },
                messageList: {
                    bg: '#ffffff'
                },
                sentMessage: {
                    bg: '#4e8cff',
                    text: '#ffffff'
                },
                receivedMessage: {
                    bg: '#eaeaea',
                    text: '#222222'
                },
                userInput: {
                    bg: '#f4f7f9',
                    text: '#565867'
                }
            }, // specifies the color scheme for the component
            alwaysScrollToBottom: false, // when set to true always scrolls the chat to the bottom when new events are in (new message, user starts typing...)
            messageStyling: true // enables *bold* /emph/ _underline_ and such (more info at github.com/mattezza/msgdown)
        };
    },
    created() {

    },
    mounted: async function () {
        this.roomid = this.$route.query.roomid
        this.from = this.$route.query.from
        this.to = this.$route.query.to
        console.log(this.roomid)
        console.log(this.from, this.to)
        this.participants.push({
            id: this.to,
            name: this.to,
            imageUrl: 'http://127.0.0.1:8000' + await (await getUserPhoto(this.to)).data.avatar
        })
        console.log(this.participants)
        // load history messages
        const history = await this.getHistory(this.roomid)
        console.log("history:", history)
        this.loadHistoryMsg(history)
        console.log(this.messageList)

        const websocketUrl = wss_protocol + 'localhost:8000' + '/ws/chat/' + this.roomid + '/';
        console.log("正在连接...")
        console.log(websocketUrl)
        var ref = this
        this.chatSocket = new WebSocket(websocketUrl);
        this.chatSocket.onopen = function () {
            resetUnreadMsg({chat_user : ref.to})
            console.log("连接成功啦...")
        }

        // createSocket(websocketUrl)
        // websocket连接断开时触发此方法
        this.chatSocket.onclose = function () {
            resetUnreadMsg({chat_user : ref.to})
            console.log('Chat socket closed.');
        };
        this.chatSocket.onmessage = function (e) {

            const recv_data = JSON.parse(e.data);
            const to = ref.getIdPair()[1];
            console.log("receive msg from " + recv_data.from_user + ", cur target: " + to)
            console.log(recv_data)
            if (recv_data.from_user == to) {
                ref.onMessageWasSent({ author: to, type: 'text', data: { text: recv_data.message } })
            }
        };

    },
    beforeUnmount() {
        this.chatSocket.close();
        this.chatSocket = null; // to prevent memory leacking
        console.log("Closing connection to WebSocket Server")
    },
    methods: {
        sendWebsocketMsg(message, from, to) {
            this.chatSocket.send(JSON.stringify({
                'message': message,
                'from_user': from,
                'to_user': to,
                'room': this.roomid,
                'time': 0
            }));
        },
        // sendMessage(text) {
        //     if (text.length > 0) {
        //         this.newMessagesCount = this.isChatOpen ? this.newMessagesCount : this.newMessagesCount + 1
        //         console.log("send!")
        //         this.sendWebsocketMsg(text)
        //         this.onMessageWasSent({ author: 'support', type: 'text', data: { text } })
        //     }
        // },
        getHistory(roomid) {
            return getChatHistory(roomid).then(async response => {
                var history = []
                // console.log(response.data)
                history = history.concat(response.data.results)
                while (response.data.next) {
                    response = await getByUrl(response.data.next)
                    history = history.concat(response.data.results)
                    // console.log(response.data)
                }
                // console.log(history)
                return history
            })
                .catch(
                    err => {
                        console.log(err)
                        this.$router.push('/login')
                    }
                )
        },
        loadHistoryMsg(history) {
            for (const msg of history) {
                console.log(msg)
                this.messageList.push({
                    author: msg.from_user == this.from ? 'me' : msg.from_user,
                    type: 'text',
                    data: { text: msg.content }
                })
            }
        },
        onMessageWasSent(message) {
            // called when the user sends a message
            console.log("got message..")
            console.log(message)
            if (message.author == 'me') {
                console.log(this.from)
                console.log(this.to)
                this.sendWebsocketMsg(message.data.text, this.from, this.to)
                addUnreadMsg({chat_user : this.to})
            }
            this.messageList = [...this.messageList, message]
        },
        openChat() {
            // called when the user clicks on the fab button to open the chat
            this.isChatOpen = true
            this.newMessagesCount = 0
        },
        closeChat() {
            // called when the user clicks on the botton to close the chat
            // this.isChatOpen = false
            this.$router.back()
        },
        handleScrollToTop() {
            // called when the user scrolls message list to top
            // leverage pagination for loading another page of messages
        },
        handleOnType() {
            console.log('Emit typing event')
        },
        editMessage(message) {
            const m = this.messageList.find(m => m.id === message.id);
            m.isEdited = true;
            m.data.text = message.data.text;
        },
        getIdPair: function () {
            return [this.from, this.to];
        }
    }

};
</script>
