import React from "react";
import { getIn } from "formik";
import {
  MenuItem,
  Select,
  TextField,
  FormControl,
  InputLabel,
} from "@mui/material";

export const MyTextInput = function MyTextInput({ field, form, ...props }) {
  const textFieldError =
    getIn(form.touched, field.name) && getIn(form.errors, field.name);
  const error = getIn(form.errors, field.name);
  return (
    <TextField
      fullWidth
      margin="normal"
      error={!!textFieldError}
      helperText={textFieldError}
      {...field}
      {...props}
    />
  );
};

export const MySelectInput = function MySelectInput({
  field,
  form,
  options,
  label,
  ...props
}) {
  return (
    <FormControl fullWidth>
      <Select {...field} {...props}>
        {options.map((op) => (
          <MenuItem key={op.value} value={op.kind}>
            {op.value}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};
