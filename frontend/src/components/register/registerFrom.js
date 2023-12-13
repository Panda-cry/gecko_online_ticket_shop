import React, { useState } from "react";
import { Button, Stack, Avatar, Typography } from "@mui/material";
import LockIcon from "@mui/icons-material/Lock";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import { Link } from "react-router-dom";
import { API_ENDPOINTS } from "../../api";
import axios from "axios";
import { Field, Form, Formik } from "formik";
import { MySelectInput, MyTextInput } from "../common/InputFields";
import * as yup from "yup";
import { RegisterUser, UploadImage } from "../common/BackendCalls";

const schema = yup.object({
  username: yup
    .string()
    .required("Username is required")
    .min(5, "Minimum 5 caracters"),
  password: yup
    .string()
    .required("Password is required")
    .min(6, "Minimum lenght is 6"),
  email: yup.string().email().required("Email is required"),
  image: yup.mixed(),
});

function RegisterForm() {
  const [file, setFile] = useState(null);

  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }
  function handleFormSubmit(data) {
    if (file) {
      UploadImage(file);
      data.image = file.name;
    }
    console.log(data);
    RegisterUser(data);
  }

  return (
    <Stack
      spacing={1}
      justifyContent="center"
      justifyItems="center"
      alignContent="center"
      alignItems="center"
      sx={{ width: 1, height: "100vh" }}
    >
      <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
        <LockIcon></LockIcon>
      </Avatar>
      <Typography>Sign up</Typography>
      <Formik
        initialValues={{
          username: "",
          email: "",
          password: "",
          user_type: "USER",
          image: "",
        }}
        validationSchema={schema}
        onSubmit={handleFormSubmit}
      >
        <Form>
          <Stack spacing={1}>
            <Field
              fullWidth
              variant="filled"
              name="username"
              label="Username"
              type="text"
              component={MyTextInput}
            />

            <Field
              fullWidth
              variant="filled"
              name="email"
              label="Email"
              type="email"
              component={MyTextInput}
            />
            <Field
              fullWidth
              variant="filled"
              name="password"
              label="Password"
              type="password"
              component={MyTextInput}
            />
            <Field
              name="user_type"
              label="Role"
              component={MySelectInput}
              options={[
                { value: "User", kind: "USER" },
                { value: "Seller", kind: "SELLER" },
              ]}
            />
            <Button
              component="label"
              variant="contained"
              startIcon={<CloudUploadIcon />}
            >
              Upload file
              <input
                type="file"
                name="file"
                hidden
                onChange={handleFileChange}
              />
            </Button>
            <Button type="submit">Register</Button>
          </Stack>
        </Form>
      </Formik>

      <Link to="/">Do you have an account? Log in</Link>
    </Stack>
  );
}

export default RegisterForm;
