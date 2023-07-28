import { Route, Routes } from "react-router-dom";
import React from "react";
import "./App.css";
import Home from "./pages/Home";
import Blog from "./pages/Blog";
import CreatePost from "./pages/CreatePost";
import EditPost from "./pages/EditPost";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Category from "./pages/Category";

const App = () => {
  return (
    <div className="container">
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/createBlog" exact element={<CreatePost />} />
        <Route path="/blog/:id/edit" exact element={<EditPost />} />
        <Route path="/login" exact element={<Login />} />
        <Route path="/register" exact element={<Register />} />
        <Route path="/blog/:id" element={<Blog />} />
        <Route path="/category/:id" element={<Category />} />
      </Routes>
    </div>
  );
};

export default App;
