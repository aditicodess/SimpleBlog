import React, { useState, useEffect } from "react";
import { useParams } from "react-router";
import EmptyList from "../../components/Common/EmptyList";
import BlogList from "../../components/Home/BlogList";
import { Link } from "react-router-dom";
import "./styles.css";
import axios from "axios";

const Category = () => {
  const { id } = useParams();
  const [blogs, setBlogs] = useState([]);
  const [category, setCategory] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const url = `http://127.0.0.1:8000/category/${id}`;
      const { data: res } = await axios.get(url);
      const newData = res.data;
      console.log(newData.blogs);
      setBlogs(newData.blogs);
      setCategory(newData.category);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div>
      <Link className="blog-goBack" to="/">
        <span> &#8592;</span> <span>Go Back</span>
      </Link>

      <div className="blog-wrap">
        <header>
          <h1 className="blog-title">{category.title}</h1>
          {/* <div className="blog-subCategory">
            <Chip label={blog.cat.title} />
          </div> */}
        </header>
        <img
          className="blogItem-cover"
          src={`data:image/png;base64, ${category.base64_image}`}
          alt="cover"
        />
        <p className="blog-desc">{category.description}</p>
      </div>
      {/* Blog List & Empty View */}
      {!blogs.length ? <EmptyList /> : <BlogList blogs={blogs} />}
    </div>
  );
};

export default Category;
