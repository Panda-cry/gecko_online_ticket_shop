import { Grid } from "@mui/material";
import ArticleList from "./ArticlesList";
import OrderForm from "./OrderForm";
import { Provider } from "react-redux";
import store from "../../store";
import OrdersList from "./OrdersList";

function UserPage() {
  return (
    <Provider store={store}>
      <Grid container>
        <Grid item xs={4}>
          <ArticleList></ArticleList>
        </Grid>
        <Grid item xs={4}>
          <OrderForm></OrderForm>{" "}
        </Grid>
        <Grid item xs={4}>
          <OrdersList></OrdersList>
        </Grid>
      </Grid>
    </Provider>
  );
}

export default UserPage;
