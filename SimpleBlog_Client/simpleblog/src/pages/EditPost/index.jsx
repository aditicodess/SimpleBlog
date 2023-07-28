import "react-quill/dist/quill.snow.css";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Editor from "./Editor";
import axios from "axios";
import { useParams } from "react-router";

export default function CreatePost() {
  // const [post, setPost] = useState({
  //   title: "",
  //   content: "",
  //   description: "",
  //   image: "",
  //   CategoryName: "",
  // });
  const { id } = useParams();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [content, setContent] = useState("");
  const [image, setImage] = useState("");
  const [categoryList, setCategoryList] = useState([]);
  const [CategoryName, setCategoryName] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const url = `http://127.0.0.1:8000/post/${id}`;
      const { data: res } = await axios.get(url);
      const newData = res.data;
      if (newData) {
        setTitle(newData.title);
        setDescription(newData.description);
        setContent(newData.content);
        setImage(newData.image[0]);
        // setCategoryName(newData.cat);
      }
      console.log(newData);
    };
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
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

  async function editPost(e) {
    try {
      const token = localStorage.getItem("token");
      if (token) {
        const data = new FormData();
        data.append("title", title);
        data.append("description", description);
        data.append("content", content);
        data.append("image", image[0]);
        data.append("cat", CategoryName);
        e.preventDefault();
        console.log(data);
        const config = {
          headers: { "content-type": "multipart/form-data" },
        };
        await axios.patch(`http://127.0.0.1:8000/post/${id}`, data, config);

        // navigate("/");
      }
    } catch (err) {
      navigate("/");
    }
  }

  return (
    <form onSubmit={editPost}>
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
        <option value="">Select Category</option>
        {categoryList.map((category) => (
          <option value={category.id} key={category.id}>
            {category.title}
          </option>
        ))}
      </select>
      <button style={{ marginTop: "5px" }}>Edit post</button>
    </form>
  );
}
