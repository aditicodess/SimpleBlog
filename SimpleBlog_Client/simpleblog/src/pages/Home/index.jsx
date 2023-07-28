import React, { useState, useEffect } from "react";
import EmptyList from "../../components/Common/EmptyList";
import BlogList from "../../components/Home/BlogList";
// import Header from "../../components/Home/Header";
import SearchBar from "../../components/Home/SearchBar";
import Navbar from "../../components/Common/Navbar";
import axios from "axios";

const Home = () => {
  const [blogs, setBlogs] = useState([]);
  const [searchKey, setSearchKey] = useState("");
  const [flag, setflag] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const url = "http://127.0.0.1:8000";
      const { data: res } = await axios.get(url);
      const newData = res.data;
      console.log(newData.blogs);
      setBlogs(newData.blogs);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [flag]);

  // Search submit
  const handleSearchBar = (e) => {
    e.preventDefault();
    handleSearchResults();
  };

  // Search for blog by category
  const handleSearchResults = () => {
    const allBlogs = blogs;
    const filteredBlogs = allBlogs.filter((blog) =>
      blog.cat.toLowerCase().includes(searchKey.toLowerCase().trim())
    );
    setBlogs(filteredBlogs);
  };

  // Clear search and show all blogs
  const handleClearSearch = () => {
    setflag(true);
    setBlogs(blogs);
    setSearchKey("");
  };

  return (
    <div>
      {/* Page Header */}
      {/* <Header /> */}
      <Navbar />

      {/* Search Bar */}
      <SearchBar
        value={searchKey}
        clearSearch={handleClearSearch}
        formSubmit={handleSearchBar}
        handleSearchKey={(e) => setSearchKey(e.target.value)}
      />

      {/* Blog List & Empty View */}
      {!blogs.length ? <EmptyList /> : <BlogList blogs={blogs} />}
    </div>
  );
};

export default Home;
