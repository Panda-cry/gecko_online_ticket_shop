import { Button } from "@mui/material";

function AccountPage() {
  function onclicl() {
    window.location.href = "home";
  }
  return (
    <div>
      Account
      <Button onClick={onclicl}>Submit</Button>
    </div>
  );
}
export default AccountPage;
