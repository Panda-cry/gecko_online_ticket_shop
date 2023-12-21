import { Button, Grid, Stack, Typography } from "@mui/material";
import { Field, Formik, Form } from "formik";
import QRCode from "react-qr-code";
import { MyTextInput } from "../common/InputFields";
import * as yup from "yup";
import { LoginWithCode } from "../common/BackendCalls";
import { ToastContainer, toast } from "react-toastify";
const schema = yup.object({
  code: yup.number().required(),
});
function QRImage(props) {
  function handleSubmitForm(data) {
    console.log(data);
    LoginWithCode(data.code)
      .then(function (response) {
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
    <Stack
      container
      spacing={4}
      justifyContent="center"
      alignItems="center"
      sx={{ width: 1, height: "100vh" }}
    >
      <QRCode value={props.url} size={300}></QRCode>
      <Typography>Scan QR and send code</Typography>
      <Formik
        initialValues={{ code: 0 }}
        validationSchema={schema}
        onSubmit={handleSubmitForm}
      >
        <Form>
          <Field
            component={MyTextInput}
            required
            type="number"
            label="Code"
            name="code"
          />
          <Button type="submit">Check</Button>
        </Form>
      </Formik>
      <ToastContainer />
    </Stack>
  );
}

export default QRImage;
