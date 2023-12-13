import { List } from "@mui/material";
import ArticleItem from "./ArticleItem";
import { useEffect, useState } from "react";
import { GetArticles, GetOrders } from "../common/BackendCalls";
import OrderItem from "./OrderItem";

function OrdersList() {
  const [orders, setOrders] = useState([]);
  useEffect(() => {
    GetOrders().then(function (data) {
      setOrders(data);
    });
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
