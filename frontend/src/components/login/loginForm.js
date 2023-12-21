import React from "react";
import { Button, Stack, Typography, Avatar, Grid } from "@mui/material";
import LockIcon from "@mui/icons-material/Lock";
import { Link } from "react-router-dom";

import { Field, Form, Formik } from "formik";
import * as yup from "yup";
import { LoginData, LoginViaApi } from "../common/BackendCalls";
import { MyTextInput } from "../common/InputFields";
import { ToastContainer, toast } from "react-toastify";
import { jwtDecode } from "jwt-decode";

import {
  LoginSocialGoogle,
  LoginSocialAmazon,
  LoginSocialFacebook,
  LoginSocialGithub,
  LoginSocialInstagram,
  LoginSocialLinkedin,
  LoginSocialMicrosoft,
  LoginSocialPinterest,
  LoginSocialTwitter,
  LoginSocialApple,
  IResolveParams,
} from "reactjs-social-login";

import {
  FacebookLoginButton,
  GoogleLoginButton,
  GithubLoginButton,
  AmazonLoginButton,
  InstagramLoginButton,
  LinkedInLoginButton,
  MicrosoftLoginButton,
  TwitterLoginButton,
  AppleLoginButton,
} from "react-social-login-buttons";

const schema = yup.object({
  user_email: yup.string().required("Username or email is required"),
  password: yup.string().required("Password is required"),
});

function LoginForm() {
  function handleSubmitForm(data) {
    LoginData(data)
      .then(function (response) {
        localStorage.setItem("access_token", response.access_token);
        localStorage.setItem("refresh_token", response.refresh_token);
        window.location.href = "/home";
        toast.success("Logged in");
      })
      .catch(function (error) {});
  }

  function handleApi({ provider, data }) {
    console.log(data);
    LoginViaApi(data.email)
      .then(function (response) {
        console.log(response);
        localStorage.setItem("access_token", response.access_token);
        localStorage.setItem("refresh_token", response.refresh_token);
        window.location.href = "/home";
        toast.success("Logged in");
      })
      .catch(function (error) {
        toast.error(error.response.data.message);
      });
  }
  return (
    <div>
      <Stack
        spacing={2}
        container
        justifyContent="center"
        alignItems="center"
        sx={{ width: 1, height: "100vh" }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockIcon></LockIcon>
        </Avatar>
        <Typography>Sign in</Typography>
        <Formik
          initialValues={{ user_email: "", password: "" }}
          validationSchema={schema}
          onSubmit={handleSubmitForm}
        >
          <Form>
            <Stack spacing={1}>
              <Field
                component={MyTextInput}
                name="user_email"
                type="text"
                required
                label="Username or email"
              />
              <Field
                component={MyTextInput}
                name="password"
                type="password"
                required
                label="Password"
              />{" "}
              <Button type="submit">Log in</Button>
            </Stack>
          </Form>
        </Formik>
        <Grid container width={200}>
          <Grid item>
            <LoginSocialGoogle
              client_id={
                "7458987117-o4n8lj3cf681f8qmi3ach73o5vp52d3f.apps.googleusercontent.com"
              }
              onResolve={handleApi}
              onReject={(err) => {
                toast.error(err);
              }}
            >
              <GoogleLoginButton text="" />
            </LoginSocialGoogle>
          </Grid>
          <Grid item>
            <LoginSocialFacebook
              appId={"6634093910033589"}
              scope="email"
              fieldsProfile="email"
              onResolve={handleApi}
              onReject={(err) => {
                toast.error(err);
              }}
            >
              <FacebookLoginButton text="" />
            </LoginSocialFacebook>
          </Grid>
        </Grid>

        <Link to="register">Don't have an account? Sign Up</Link>
      </Stack>
      <ToastContainer />
    </div>
  );
}

export default LoginForm;
/*

sx sluzi da se override styles 

U kontekstu Material-UI, xs, sm, md, lg, i xl su oznake koje se često koriste za definisanje odzivnosti (responsiveness) komponenata na različitim širinama ekrana. 

*/
