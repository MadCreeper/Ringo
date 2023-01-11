import axios from 'axios';

let local_host = 'http://127.0.0.1:8000'
//获取物品类别信息
export const queryCategorygoods = () => { return axios.get(`${local_host}/apis/indexgoods/`) }

//获取物品类别信息
export const getCategory = params => {
  if('id' in params){
    return axios.get(`${local_host}/apis/category/`+params.id+'/');
  }
  else {
    return axios.get(`${local_host}/apis/category/`, params);
  }
};


//获取需求列表(all)
export const getGoods = params => { return axios.get(`${local_host}/apis/goods/`, { params: params }) }

//物品详情
export const getGoodsDetail = goodId => { return axios.get(`${local_host}/apis/goods/${goodId}`+'/') }


//登录
export const login = params => {
  return axios.post(`${local_host}/apis/login/login`, params)
}

//注册

export const register = params => { return axios.post(`${local_host}/apis/login/register`,params) }

//修改密码（忘记密码）
export const changecode = params => { return axios.post(`${local_host}/apis/login/forget_password`,params) }

// 重设密码
export const resetcode = params => { return axios.post(`${local_host}/apis/login/reset_password`,params) }

//短信
export const getMessage = params => { return axios.post(`${local_host}/code/`, params) }

//获取用户信息
export const getUserDetail = () => { return axios.get(`${local_host}/apis/user_profile`) }


//修改信息
export const updateUserInfo = params => { return axios.post(`${local_host}/apis/user_profile`, params) }

//添加需求
export const addNeeds = params => {return axios.post(`${local_host}/apis/need/`, params)}

//删除需求
export const delNeeds  = addressId => {return axios.delete(`${local_host}/apis/need/`+addressId+'/')}

//修改需求
export const updateNeeds  = (addressId, params) => {return axios.patch(`${local_host}/apis/need/`+addressId+'/', params)}

//获取需求
export const getNeeds  = () => {return axios.get(`${local_host}/apis/need/`)}

//添加提供
export const addOffering = params => {return axios.post(`${local_host}/apis/offering/`, params)}

//删除需求
export const delOffering = addressId => {return axios.delete(`${local_host}/apis/offering/`+addressId+'/')}

//修改需求
export const updateOffering = (addressId, params) => {return axios.patch(`${local_host}/apis/offering/`+addressId+'/', params)}

//获取需求
export const getOffering = () => {return axios.get(`${local_host}/apis/offering/`)}

export const getOfferingDetail = itemId => {return axios.get(`${local_host}/apis/offering/${itemId}`+'/')}

//建立连接/断开连接时清空未读消息,需要认证
export const resetUnreadMsg = params => {return axios.post(`${local_host}/chat/reset_msg`, params)}

//发送消息时将对方的未读消息加一，需要认证
export const addUnreadMsg = params => {return axios.post(`${local_host}/chat/add_msg`, params)}

//获取当前用户的所有聊天对象， 需要认证
export const getChatUsers = () => {return axios.get(`${local_host}/apis/group_user/`)}

//获取当前聊天组的历史聊天记录， 需要认证
export const getChatHistory = room_name => {return axios.get(`${local_host}/apis/history/?room=${room_name}` + '/')}