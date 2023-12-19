import { Grid } from "@mui/material";
import UsersList from "./UsersList";
import OrdersList from "../user/OrdersList";
import {
  AdminAllUsers,
  AdminOrders,
  GetUsersAdmin,
} from "../common/BackendCalls";

function AdminPage() {
  return (
    <Grid container>
      <Grid xs={4} item>
        <UsersList func={GetUsersAdmin} option={"INFO"} />
      </Grid>
      <Grid xs={4} item>
        <OrdersList func={AdminOrders} />
      </Grid>
      <Grid xs={4} item>
        <UsersList func={AdminAllUsers} option={"DELETE"} />
      </Grid>
    </Grid>
  );
}

export default AdminPage;
