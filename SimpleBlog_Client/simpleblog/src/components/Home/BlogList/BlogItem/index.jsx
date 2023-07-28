import React from "react";
import { Link } from "react-router-dom";
import Chip from "../../../Common/Chip";
import "./styles.css";

const BlogItem = ({
  blog: {
    description,
    title,
    date_posted,
    author,
    // authorAvatar,
    base64_image,
    cat,
    id,
  },
}) => {
  return (
    <div className="blogItem-wrap">
      <img
        className="blogItem-cover"
        src={`data:image/png;base64, ${base64_image}`}
        alt="cover"
      />
      <Chip label={cat} />
      <h3>{title}</h3>
      <p className="blogItem-desc">{description}</p>
      <footer>
        <div className="blogItem-author">
          {/* <img src={authorAvatar} alt="avatar" /> */}
          <div>
            <h6>{author}</h6>
            <p>{date_posted}</p>
          </div>
        </div>
        <Link className="blogItem-link" to={`/blog/${id}`}>
          ➝
        </Link>
      </footer>
    </div>
  );
};

export default BlogItem;
