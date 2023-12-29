// csrf.js

import axios from 'axios';
import Cookies from 'js-cookie';

// Django CSRFトークンを取得する関数
export const getCSRFToken = () => {
  return Cookies.get('csrftoken');
};

// Axiosのデフォルト設定
axios.defaults.baseURL = 'http://localhost:8000'; // DjangoサーバーのURLに合わせて変更
axios.defaults.withCredentials = true;

// リクエストインターセプターでCSRFトークンをヘッダーに設定
axios.interceptors.request.use(
  (config) => {
    const csrfToken = getCSRFToken();
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 例: リクエストの送信
axios.get('/api/stops/')
  .then(response => {
    // 成功時の処理
    console.log(response.data);
  })
  .catch(error => {
    // エラー時の処理
    console.error('Error fetching data:', error);
  });
