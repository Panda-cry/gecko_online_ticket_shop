import { List } from "@mui/material";
import ArticleItem from "./ArticleItem";
import { useEffect, useState } from "react";
import { GetArticles, GetOrders, RefreshToken } from "../common/BackendCalls";
import OrderItem from "./OrderItem";
import { toast } from "react-toastify";

function OrdersList(props) {
  const [orders, setOrders] = useState([]);
  useEffect(() => {
    const interval = setInterval(() => {
      props
        .func()
        .then(function (data) {
          setOrders(data);
        })

        .catch(function (error) {
          console.log(error);
          if (error.response.status === 401) {
            RefreshToken()
              .then(function (response) {
                localStorage.setItem("access_token", response.access_token);
                localStorage.setItem("refresh_token", response.refresh_token);
                toast.success("Refreshed in");
              })
              .catch(function (error) {
                toast.error("Server error porbably");
              });
          }
        });
    }, 4000);
    return () => clearInterval(interval);
  }, []);
  return (
    <List key={Math.random(100)}>
      {Array.isArray(orders)
        ? orders.map((item) => (
            <OrderItem
              key={item.id}
              amount={item.amount}
              comment={item.comment}
              address={item.address}
              id={item.id}
            />
          ))
        : null}
    </List>
  );
}

export default OrdersList;
