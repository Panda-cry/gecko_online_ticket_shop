import React from "react";
import LoginForm from "../login/loginForm";
import RegisterForm from "../register/registerFrom";
import { jwtDecode } from "jwt-decode";
import NavBar from "../common/NavBar";
import UserPage from "../user/userPage";
function MyApp() {
  const registerd = true;
  const role = jwtDecode(localStorage.getItem("access_token")).user_type;

  return (
    <React.Fragment>
      <NavBar></NavBar>
      {role === "USER" && <UserPage />}

      {role === "SELLER" && <div>MAJA</div>}
      {role === "ADMIN" && <div>MAJA</div>}
    </React.Fragment>
  );
}

export default MyApp;
