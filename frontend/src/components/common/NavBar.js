import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import HomeIcon from "@mui/icons-material/Home";
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import { GetSum, GetUser, RefreshToken } from "./BackendCalls";
import "react-toastify/dist/ReactToastify.css";
import { jwtDecode } from "jwt-decode";
import { ToastContainer, toast } from "react-toastify";
function NavBar() {
  const role = jwtDecode(localStorage.getItem("access_token")).user_type;

  function handleClick() {
    localStorage.clear();
    window.location.href = "/";
  }
  const [sum, setSum] = useState(0);
  useEffect(() => {
    if (role !== "ADMIN") {
      GetSum()
        .then(function (response) {
          setSum(response["Sum is :"]);
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
    }
  }, []);
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <HomeIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Welcome
          </Typography>
          {role !== "ADMIN" ? (
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Delivery cost : {sum}
            </Typography>
          ) : null}

          <Button>
            <Link
              to="/account"
              style={{ color: "white", textDecoration: "none" }}
            >
              Account
            </Link>
          </Button>

          <Button color="inherit" onClick={handleClick}>
            Logout
          </Button>
        </Toolbar>
      </AppBar>
      <ToastContainer />
    </Box>
  );
}

export default NavBar;
