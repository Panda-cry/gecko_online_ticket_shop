import React from "react";
import { Button, Stack, Typography, Avatar } from "@mui/material";
import LockIcon from "@mui/icons-material/Lock";
import { Link } from "react-router-dom";

import { Field, Form, Formik } from "formik";
import * as yup from "yup";
import { LoginData } from "../common/BackendCalls";
import { MyTextInput } from "../common/InputFields";

const schema = yup.object({
  user_email: yup.string().required("Username or email is required"),
  password: yup.string().required("Password is required"),
});

function LoginForm() {
  function handleSubmitForm(data) {
    console.log(data);
    LoginData(data);
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

        <Link to="register">Don't have an account? Sign Up</Link>
      </Stack>
    </div>
  );
}

export default LoginForm;
/*

sx sluzi da se override styles 

U kontekstu Material-UI, xs, sm, md, lg, i xl su oznake koje se često koriste za definisanje odzivnosti (responsiveness) komponenata na različitim širinama ekrana. 

*/
