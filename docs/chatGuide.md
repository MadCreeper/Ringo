# 环境：

channels                  4.0.0                 
channels-redis            4.0.0                    

daphne                    4.0.0 
uvicorn                   0.20.0
django-redis              4.12.1 

搜索安装Memurai(作为Redis的Windows替代品，数据通道和缓存) 



# 私聊组号

需求详情界面，获取到该需求所属用户ID A，和当前登录用户ID B 组合成A_B(字典序,小的在前), 作为这两个用户的聊天组号(roomName)

# 聊天记录

进入私聊界面时，通过GET /apis/history/?room= xxx  获取该组号的历史聊天记录，为按时间从前到后的列表。格式为：

```
{
"from_user": "",
"to_user": "",
"room": "",
"content": "",
"create_time": "2022-12-25T09:15:58.999915Z"
}
```

from_user是这条信息的发送者。

# WebSocket操作

* 初始化：

  ```javascript
    const chatSocket = new WebSocket(
   wss_protocol + window.location.host + '/ws/chat/'  + roomName + '/'
   );
  ```

* 发送信息：chatSocket.send()
* 接收信息：chatSocket.onmessage

还有连接成功时、连接断开时等等，参考 RingoBackend\templates\chat\room.html