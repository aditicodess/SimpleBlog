import "react-quill/dist/quill.snow.css";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Editor from "./Editor";
import axios from "axios";

export default function CreatePost() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [content, setContent] = useState("");
  const [image, setImage] = useState("");
  const [categoryList, setCategoryList] = useState([]);
  const [CategoryName, setCategoryName] = useState("");
  const [redirect, setRedirect] = useState(false);
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
    console.log(event.target.value);
  };

  async function createNewPost(ev) {
    const data = new FormData();
    let postAuth = localStorage.getItem("user");
    postAuth = postAuth.slice(1, postAuth.length - 1);
    console.log(postAuth);
    data.append("title", title);
    data.append("description", description);
    data.append("content", content);
    data.append("image", image[0]);
    data.append("author", postAuth);
    data.append("cat", CategoryName);
    ev.preventDefault();
    console.log(data);
    const config = {
      headers: { "content-type": "multipart/form-data" },
    };

    const url = "http://127.0.0.1:8000/add_post";
    const { data: res } = await axios.post(url, data, config);
    if (res.ok) {
      setRedirect(true);
    }
  }

  if (redirect) {
    navigate("/");
  }
  return (
    <form onSubmit={createNewPost}>
      <input
        type="title"
        placeholder={"Title"}
        value={title}
        onChange={(ev) => setTitle(ev.target.value)}
      />
      <input
        type="content"
        placeholder={"Content"}
        value={content}
        onChange={(ev) => setContent(ev.target.value)}
      />
      <input type="file" onChange={(ev) => setImage(ev.target.files)} />
      <Editor value={description} onChange={setDescription} />
      <select
        className="form-control"
        value={CategoryName}
        onChange={handleChange}
      >
        <option value="">Choose Category Name</option>
        {categoryList.map((category) => (
          <option value={category.id} key={category.id}>
            {category.title}
          </option>
        ))}
      </select>
      <button style={{ marginTop: "5px" }}>Create post</button>
    </form>
  );
}
