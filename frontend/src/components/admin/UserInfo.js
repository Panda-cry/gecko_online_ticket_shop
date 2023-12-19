import { Avatar, Button, Stack, Typography } from "@mui/material";
import { AdminDeleteUser, AdminVerifyUser } from "../common/BackendCalls";

function UserInfo({ key, id, image, username, email, option }) {
  function handleClickVerifyButton() {
    AdminVerifyUser(id).then(function (response) {
      alert(response.message);
    });
  }

  function handleClickDeleteButton() {
    AdminDeleteUser(id).then(function (response) {
      alert(response.message);
    });
  }
  return (
    <Stack key={key}>
      <Avatar src={image}></Avatar>
      <Typography
        sx={{ display: "inline" }}
        component="span"
        variant="body2"
        color="text.primary"
      >
        {username}
      </Typography>
      <Typography
        sx={{ display: "inline" }}
        component="span"
        variant="body2"
        color="text.primary"
      >
        {email}
      </Typography>
      {option === "INFO" ? (
        <Button onClick={handleClickVerifyButton}>Verify</Button>
      ) : (
        <Button onClick={handleClickDeleteButton}>Delete</Button>
      )}
    </Stack>
  );
}

export default UserInfo;
