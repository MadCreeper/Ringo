import axios from 'axios'

axios.defaults.timeout = 50000

axios.interceptors.request.use(config => {
  // ...
  return config
}, error => {
  return Promise.error(error)
})

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