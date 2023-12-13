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
import { GetSum } from "./BackendCalls";
function NavBar() {
  function handleClick() {
    localStorage.clear();
    window.location.href = "/";
  }
  const [sum, setSum] = useState(0);
  useEffect(() => {
    GetSum().then(function (response) {
      setSum(response["Sum is :"]);
    });
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
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Delivery cost : {sum}
          </Typography>
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
    </Box>
  );
}

export default NavBar;
