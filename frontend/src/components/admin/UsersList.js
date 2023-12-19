import { useEffect, useState } from "react";
import { GetUsersAdmin } from "../common/BackendCalls";
import { toast } from "react-toastify";
import UserInfo from "./UserInfo";
function UsersList({ func, option }) {
  const [users, setUsers] = useState([]);
  useEffect(function () {
    const promise = func().then(function (response) {
      setUsers(response);
    });
  }, []);
  return (
    <div>
      {users.map((item) => (
        <UserInfo
          key={item.id}
          id={item.id}
          image={item.image}
          username={item.username}
          email={item.email}
          option={option}
        />
      ))}
    </div>
  );
}

export default UsersList;
