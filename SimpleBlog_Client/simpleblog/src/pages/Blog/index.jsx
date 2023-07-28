import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
// import { blogList } from "../../config/data";
import Chip from "../../components/Common/Chip";
import EmptyList from "../../components/Common/EmptyList";
import "./styles.css";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

const Blog = () => {
  let user = localStorage.getItem("user");
  user = user.slice(1, user.length - 1);
  const token = localStorage.getItem("token");
  const { id } = useParams();
  const [blog, setBlog] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const url = `http://127.0.0.1:8000/post/${id}`;
      const { data: res } = await axios.get(url);
      const newData = res.data;
      if (newData) {
        setBlog(newData);
      }
      console.log(newData);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const deleteNote = async (blogUserName, blogId) => {
    try {
      console.log("user: ", user, "userName: ", blogUserName);
      console.log("token: ", token);

      if (user === blogUserName) {
        await axios.delete(`http://127.0.0.1:8000/post/${blogId}`, {
          headers: { Authorization: token },
        });
      }
    } catch (error) {
      navigate("/");
    }
  };

  return (
    <>
      {user === blog?.author ? (
        <div className="head">
          <div>
            <Link className="blog-goBack" to="/">
              <span> &#8592;</span> <span>Go Back</span>
            </Link>
          </div>
          <div>
            <Link className="edit" to={`edit`}>
              <img src="/assets/images/edit26.svg" alt="edit icon" />
            </Link>
            <Link className="delete">
              <img
                src="/assets/images/trashcan.svg"
                onClick={() => deleteNote(blog.author, blog.id)}
                alt="delete icon"
              />
            </Link>
          </div>
        </div>
      ) : (
        <div className="head">
          <Link className="blog-goBack" to="/">
            <span> &#8592;</span> <span>Go Back</span>
          </Link>
          <span className="write">
            <Link className="link" to="/createBlog">
              Write
            </Link>
          </span>
        </div>
      )}
      {blog ? (
        <div className="blog-wrap">
          <header>
            <p className="blog-date">Published {blog.date_posted}</p>
            <h1 className="blog-title">{blog.title}</h1>
            <div className="blog-subCategory">
              <Chip label={blog.cat} />
            </div>
          </header>
          <img
            className="blogItem-cover"
            src={`data:image/png;base64, ${blog.base64_image}`}
            alt="cover"
          />
          <p className="blog-desc">{blog.description}</p>
        </div>
      ) : (
        <EmptyList />
      )}
    </>
  );
};

export default Blog;
