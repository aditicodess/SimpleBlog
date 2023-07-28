import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
// import Logo from "../img/logo.png";
import "./styles.css";

const Navbar = () => {
  const [categoryList, setCategoryList] = useState([]);
  const [categoryName, setCategoryName] = useState("");
  const currentUser = localStorage.getItem("user");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const url = "http://127.0.0.1:8000/categories";
      const { data: res } = await axios.get(url);
      const newData = res.data;
      setCategoryList(newData);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleChange = (event) => {
    setCategoryName(event.target.value);
    navigate(`/category/${event.target.value}`);
    console.log(event.target.value);
  };

  const handleLogOut = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <div className="navbar">
      <div className="container">
        <div className="logo">
          <Link to="/">
            {/* <img src={Logo} alt="" /> */}
            <h1>SimpleBlog</h1>
          </Link>
        </div>
        <div className="links">
          <select
            className="form-control"
            value={categoryName}
            onChange={handleChange}
          >
            <option value="">Choose Category Name</option>
            {categoryList.map((category) => (
              // <Link className="link" to={`/category/${category.id}`}>
              <option value={category.id} key={category.id}>
                {category.title}
              </option>
              // </Link>
            ))}
          </select>
          <span>{currentUser?.username}</span>
          {currentUser ? (
            <span onClick={handleLogOut}>Logout</span>
          ) : (
            <Link className="link" to="/login">
              Login
            </Link>
          )}
          <span className="write">
            <Link className="link" to="/createBlog">
              Write
            </Link>
          </span>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
