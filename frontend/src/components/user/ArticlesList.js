import { List } from "@mui/material";
import ArticleItem from "./ArticleItem";
import { useEffect, useState } from "react";
import { GetArticles } from "../common/BackendCalls";

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [clicked, setClicked] = useState(true);
  useEffect(() => {
    var items = GetArticles().then(function (data) {
      setArticles(data);
      setClicked(false);
    });
  }, [clicked]);
  return (
    <List key={Math.random(100)}>
      {Array.isArray(articles)
        ? articles.map((item) => (
            <ArticleItem
              clicked={clicked}
              id={item.id}
              key={Math.random(100)}
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
