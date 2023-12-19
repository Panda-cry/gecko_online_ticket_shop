import { List } from "@mui/material";
import ArticleItem from "./ArticleItem";
import { useEffect, useState } from "react";
import { GetArticles, RefreshToken } from "../common/BackendCalls";
import { toast } from "react-toastify";

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [clicked, setClicked] = useState(true);
  useEffect(() => {
    const interval = setInterval(() => {
      GetArticles()
        .then(function (data) {
          setArticles(data);
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
    }, 1000);
    return () => clearInterval(interval);
  }, []);
  return (
    <List key={"123123"}>
      {Array.isArray(articles)
        ? articles.map((item) => (
            <ArticleItem
              clicked={setClicked}
              id={item.id}
              key={item.id}
              price={item.price}
              name={item.name}
              amount={item.amount}
              image={item.image}
            />
          ))
        : null}
    </List>
  );
}

export default ArticleList;
