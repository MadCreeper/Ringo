import axios from 'axios'
axios.defaults.timeout = 50000

axios.interceptors.request.use(
  config => {
  let url = config.url;
  console.log(url)
  if (url==="http://127.0.0.1:8000/apis/login/register"){
    return config
  }
  else if (localStorage.token) { //判断token是否存在
    config.headers.Authorization ="JWT "+localStorage.token;  //将token设置成请求头
  }
  else{
    config.headers.Authorization ="JWT "+"sdadasd";
  }
  return config
}, error => {
  return Promise.error(error)
})

axios.interceptors.request.use(
  response => {
  return response
}, error => {
  console.log(error)
  if (error.response.status===401){
  window.location.href("/login")
}})

function getNeeds () {
    return axios.get(`http://localhost:8000/api/needs/`)
}

function postNeed (needTitle, needAuthor) {
    return axios.post(`http://localhost:8000/api/needs/`, {'title': needTitle, 'author': needAuthor})
}

export {
    getNeeds,
    postNeed
}