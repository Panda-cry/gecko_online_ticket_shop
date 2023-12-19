import { Stack, Button } from "@mui/material";
import { Field, Form, Formik } from "formik";
import { MyTextInput } from "../common/InputFields";

import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import { useState } from "react";
import * as yup from "yup";
import { ArticlePOST, UploadImage } from "../common/BackendCalls";

const schema = yup.object({
  name: yup.string().required().min(5),
  amount: yup.number().required().min(10),
  price: yup.number().required().min(1),
  descrption: yup.string(),
});

function ArticleForm() {
  const [file, setFile] = useState(null);

  function handleSubmitForm(data, actions) {
    if (file) {
      UploadImage(file);
      data.image = file.name;
    } else {
      delete data.image;
    }
    ArticlePOST(data);
    actions.resetForm();
    setFile(null);
  }
  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }
  return (
    <Stack
      spacing={1}
      justifyContent="center"
      justifyItems="center"
      alignContent="center"
      alignItems="center"
    >
      <Formik
        initialValues={{
          name: "",
          amount: 10,
          price: 1,
          description: "",
          image: "",
        }}
        validationSchema={schema}
        onSubmit={handleSubmitForm}
      >
        <Form>
          <Stack spacing={2}>
            <Field
              fullWidth
              name="name"
              label="Name"
              type="text"
              component={MyTextInput}
            />
            <Field
              fullWidth
              name="amount"
              label="Amount"
              type="number"
              component={MyTextInput}
            />
            <Field
              fullWidth
              name="price"
              label="Price"
              type="text"
              component={MyTextInput}
            />
            <Field
              fullWidth
              name="description"
              label="Description"
              type="text"
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
            <Button type="submit">Add article</Button>
          </Stack>
        </Form>
      </Formik>
    </Stack>
  );
}

export default ArticleForm;
