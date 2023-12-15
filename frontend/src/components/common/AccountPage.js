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
import {
  ChangeUserPATCH,
  ChangeUserPUT,
  RegisterUser,
  UploadImage,
} from "../common/BackendCalls";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

const schema = yup.object({
  username: yup.string().nullable(true).min(5),
  password: yup.string().nullable(true).min(5),
  email: yup.string().nullable(true).email(),
  image: yup.mixed().nullable(true),
});

function AccountPage() {
  const [file, setFile] = useState(null);

  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }
  function handleFormSubmit(data) {
    console.log(data);
    if (
      data.username !== "" &&
      data.username !== null &&
      data.password !== "" &&
      data.password !== null &&
      data.email !== "" &&
      data.email !== null &&
      file
    ) {
      data.image = file.name;
      ChangeUserPUT(data).then(function (response) {
        alert("User changed PUT");
        window.location.href = "/home";
      });

      return;
    }
    if (file) {
      data.image = file.name;
    } else {
      delete data.image;
    }
    if (data.username === "") {
      delete data.username;
    }
    if (data.password === "") {
      delete data.password;
    }
    if (data.email === "") {
      delete data.email;
    }
    ChangeUserPATCH(data)
      .then(function (response) {
        alert("User changed PATCH");
        window.location.href = "/home";
      })
      .catch(function (error) {
        console.log(error.response);
      });
    console.log(data);
  }
  return (
    <div>
      <Stack
        spacing={1}
        justifyContent="center"
        justifyItems="center"
        alignContent="center"
        alignItems="center"
        sx={{ width: 1, height: "100vh" }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <AccountCircleIcon />
        </Avatar>
        <Typography>Change account</Typography>
        <Formik
          initialValues={{
            username: "",
            email: "",
            password: "",
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
              <Button type="submit">Applay changes</Button>
            </Stack>
          </Form>
        </Formik>
      </Stack>
    </div>
  );
}
export default AccountPage;
