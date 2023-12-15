import { Avatar, Button, Stack } from "@mui/material";
import { MyTextInput } from "../common/InputFields";
import { Field, Form, Formik } from "formik";
import * as yup from "yup";
import { useDispatch, useSelector } from "react-redux";
import { chartActions } from "../../store";
import { PostOrder } from "../common/BackendCalls";

const schema = yup.object({
  address: yup.string().required("Address is required").min(7),
  amount: yup
    .number()
    .min(1, "Must order something")
    .max(100, "We don't believe you"),
  comment: yup.string(),
});

function OrderForm() {
  const dispach = useDispatch();
  const cartValue = useSelector((state) => state.chart.chart);
  function handleSubmitForm(data, actions) {
    if (cartValue.length === 1) {
      data.article_id = cartValue[0].id;
      PostOrder(data).catch(function (error) {
        console.log(error.response);
        alert(error.response.data.message);
      });

      dispach(chartActions.remove());
    }
    actions.resetForm({
      values: { address: "", amount: 0, comment: "" },
      // you can also set the other form states here
    });
  }
  return (
    <Stack spacing={1}>
      <Formik
        initialValues={{ address: "", amount: 0, comment: "" }}
        validationSchema={schema}
        onSubmit={handleSubmitForm}
      >
        <Form>
          <Field
            fullWidth
            variant="filled"
            name="address"
            label="Address"
            type="text"
            component={MyTextInput}
          />
          <Field
            name="amount"
            label="Amount"
            type="number"
            component={MyTextInput}
          />
          <Field
            name="comment"
            label="Comment"
            type="text"
            component={MyTextInput}
          />

          <Button type="submit">Add new order</Button>
        </Form>
      </Formik>
    </Stack>
  );
}

export default OrderForm;
