import { API_ENDPOINTS } from "../../api";
import axios from "axios";
export const LoginData = async (data) => {
  try {
    // Primer poziva ka backend endpointu
    const response = await axios.post(API_ENDPOINTS.LOGIN, {
      username_email: data.user_email,
      password: data.password,
    });

    localStorage.setItem("access_token", response.data.access_token);
    localStorage.setItem("refresh_token", response.data.refresh_token);
    window.location.href = "/home";
  } catch (error) {
    alert(error.response.data.message);
  }
};

export const UploadImage = async (image) => {
  const response = await axios
    .post(
      API_ENDPOINTS.IMAGE,
      { image: image },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    )
    .then(function (response) {
      alert("Image uploaded");
    })
    .catch(function (error) {
      alert(error, "Something bad happende");
    });
};

export const RegisterUser = async (data) => {
  const response = await axios
    .post(API_ENDPOINTS.REGISTER, {
      username: data.username,
      password: data.password,
      email: data.email,
      image: data.image,
      user_type: data.user_type,
    })
    .then(function (response) {
      alert("User created");
      window.location.href = "/";
    })
    .catch(function (error) {
      alert(error, "Something bad happende");
    });
};
export const ChangeUserPUT = async (data) => {
  const response = await axios.put(
    API_ENDPOINTS.USER_PUT,
    {
      username: data.username,
      password: data.password,
      email: data.email,
      image: data.image,
    },
    {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    }
  );
};

export const ChangeUserPATCH = async (data) => {
  const response = await axios.patch(
    API_ENDPOINTS.USER_PATCH,
    {
      username: data.username,
      password: data.password,
      email: data.email,
      image: data.image,
    },
    {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("access_token"),
      },
    }
  );
};

export const GetArticles = async () => {
  const response = await axios.get(API_ENDPOINTS.ARTICLES, {
    headers: {
      Authorization: "Bearer " + localStorage.getItem("access_token"),
    },
  });
  return response.data;
};

export const PostOrder = async (data) => {
  const response = await axios.post(API_ENDPOINTS.ORDER, data, {
    headers: {
      Authorization: "Bearer " + localStorage.getItem("access_token"),
    },
  });
  return response.data;
};

export const GetOrders = async () => {
  const response = await axios.get(API_ENDPOINTS.ORDER, {
    headers: {
      Authorization: "Bearer " + localStorage.getItem("access_token"),
    },
  });
  return response.data;
};

export const GetSum = async () => {
  const response = await axios.get(API_ENDPOINTS.SUM, {
    headers: {
      Authorization: "Bearer " + localStorage.getItem("access_token"),
    },
  });
  return response.data;
};
