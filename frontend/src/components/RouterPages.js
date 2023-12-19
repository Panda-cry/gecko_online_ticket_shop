import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginForm from "./login/loginForm";
import RegisterForm from "./register/registerFrom";
import MyApp from "./appLogic.js/MyApp";
import AccountPage from "./common/AccountPage";
import { jwtDecode } from "jwt-decode";

function ShopRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<LoginForm />} />
        <Route path="register" element={<RegisterForm />} />
        <Route path="home" element={<MyApp />} />
        <Route path="/account" element={<AccountPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default ShopRouter;
