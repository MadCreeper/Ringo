import axios from 'axios'

axios.defaults.timeout = 50000

axios.interceptors.request.use(config => {
  // ...
  return config
}, error => {
  return Promise.error(error)
})

function getBooks() {
    return axios.get(`http://localhost:8000/api/books/`)
}

function postBooks (bookName,bookAuthor) {
    return axios.post(`http://localhost:8000/api/books/`,{'name': bookName, 'author': bookAuthor})
}

export {
    getBooks,
    postBooks
}