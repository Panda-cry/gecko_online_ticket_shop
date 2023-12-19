import { Grid } from "@mui/material";
import ArticleForm from "./ArticleFrom";
import { useEffect, useState } from "react";
import { GetOrders, GetUser } from "../common/BackendCalls";
import ArticleList from "../user/ArticlesList";
import { Provider } from "react-redux";
import store from "../../store";
import OrderForm from "../user/OrderForm";
import OrdersList from "../user/OrdersList";

function ConditionRedner({ verified }) {
  if (verified) {
    return <ArticleForm />;
  } else {
    return "You don't have premission to create article";
  }
}

function SellerPage() {
  const [user, setUser] = useState("");
  useEffect(function () {
    GetUser().then(function (response) {
      setUser(response);
    });
  }, []);

  return (
    <Provider store={store}>
      <Grid container>
        {" "}
        <Grid item xs={3}>
          <ArticleList />
        </Grid>
        <Grid item xs={3}>
          <OrderForm />
        </Grid>
        <Grid item xs={3}>
          <OrdersList func={GetOrders} />
        </Grid>
        <Grid item xs={3}>
          <ConditionRedner verified={user.is_verified} />
        </Grid>
      </Grid>
    </Provider>
  );
}

export default SellerPage;
