// api.js

const BASE_URL = "http://localhost:8001";
export const API_ENDPOINTS = {
  LOGIN: `${BASE_URL}/api/login`,
  LOGIN_CODE: `${BASE_URL}/api/login/code`,
  REGISTER: `${BASE_URL}/api/register`,
  USER_PUT: `${BASE_URL}/api/users`,
  USER_PATCH: `${BASE_URL}/api/users`,
  IMAGE: `${BASE_URL}/api/image`,
  ARTICLES: `${BASE_URL}/api/articles`,
  ORDER: `${BASE_URL}/api/users/orders`,
  SUM: `${BASE_URL}/api/users/orders/price_sum`,
  USER: `${BASE_URL}/api/users`,
  ARTICLE: `${BASE_URL}/api/articles`,
  USERS: `${BASE_URL}/api/admin/users`,
  VERIFY: `${BASE_URL}/api/users`,
  ALL_ORDERS: `${BASE_URL}/api/admin/orders`,
  ALL_USERS: `${BASE_URL}/api/admin/users/all`,
  REFRESH: `${BASE_URL}/api/refresh`,
  LOG_VIA_API: `${BASE_URL}/api/login/third_api`,
};
