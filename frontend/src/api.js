// api.js

const BASE_URL = "http://localhost:8001";
export const API_ENDPOINTS = {
  LOGIN: `${BASE_URL}/api/login`,
  REGISTER: `${BASE_URL}/api/register`,
  USER_PUT: `${BASE_URL}/api/users`,
  USER_PATCH: `${BASE_URL}/api/users`,
  IMAGE: `${BASE_URL}/api/image`,
  ARTICLES: `${BASE_URL}/api/articles`,
  ORDER: `${BASE_URL}/api/users/orders`,
  SUM: `${BASE_URL}/api/users/orders/price_sum`,
};
