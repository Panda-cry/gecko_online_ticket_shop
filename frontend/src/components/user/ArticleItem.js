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
import { toast } from "react-toastify";

function ArticleItem(props) {
  const dispach = useDispatch();
  const cartValue = useSelector((state) => state.chart.chart);
  function handleAddToCart() {
    if (cartValue.length === 0) {
      dispach(chartActions.add({ id: props.id }));
      toast.info("Submit form for order now");
      return;
    }
  }
  let image = "data:image/jpeg;base64," + props.image;
  return (
    <div>
      <ListItem alignItems="flex-start" key={props.id} id={props.id}>
        <ListItemAvatar>
          <Avatar alt="Remy Sharp" src={image} />
        </ListItemAvatar>
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
                {props.desciption}
              </Typography>
              Amount : {props.amount}
              <br />
              Price : {props.price}
            </React.Fragment>
          }
        />
        <Button onClick={handleAddToCart}>
          <Avatar sx={{ background: "#5FBDFF" }}>
            <AddShoppingCartIcon />
          </Avatar>
        </Button>
      </ListItem>
    </div>
  );
}

export default ArticleItem;
