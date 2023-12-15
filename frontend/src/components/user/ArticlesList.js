import { List } from "@mui/material";
import ArticleItem from "./ArticleItem";
import { useEffect, useState } from "react";
import { GetArticles } from "../common/BackendCalls";

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [clicked, setClicked] = useState(true);
  useEffect(() => {
    const interval = setInterval(() => {
      GetArticles().then(function (data) {
        setArticles(data);
      });
      console.log("Timer");
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
