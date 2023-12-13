import {
  ListItemAvatar,
  ListItem,
  Typography,
  Avatar,
  ListItemText,
  Button,
} from "@mui/material";
import React from "react";
import AddShoppingCartIcon from "@mui/icons-material/AddShoppingCart";
import { useDispatch, useSelector } from "react-redux";
import { chartActions } from "../../store";

function OrderItem(props) {
  return (
    <ListItem alignItems="flex-start" key={props.id} id={Math.random(199)}>
      <ListItemText
        primary={props.name}
        secondary={
          <React.Fragment>
            <Typography
              sx={{ display: "inline" }}
              component="span"
              variant="body2"
              color="text.primary"
            >
              {props.address}
            </Typography>
            <br></br>
            Amount : {props.amount}
            <br />
            {props.comment ? "Comment : " + props.comment : null}
          </React.Fragment>
        }
      />
    </ListItem>
  );
}

export default OrderItem;
