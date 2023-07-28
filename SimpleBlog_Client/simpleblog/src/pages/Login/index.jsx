import { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import "./styles.css";
import pic from "../../assets/graphic-design-trends.png";

const Login = () => {
  const [data, setData] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const handleChange = ({ currentTarget: input }) => {
    setData({ ...data, [input.name]: input.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const url = "http://127.0.0.1:8000/login/";
      const { data: res } = await axios.post(url, data);
      localStorage.setItem("token", res.token);
      localStorage.setItem("user", JSON.stringify(res.data));
      navigate("/");
    } catch (error) {
      if (
        error.response &&
        error.response.status >= 400 &&
        error.response.status <= 500
      ) {
        setError(error.response.data.message);
      }
    }
  };

  return (
    <div className="signup_container">
      <div className="signup_form_container">
        <div className="left">
          <img src={pic} alt="mypic" />
        </div>
        <div className="right">
          <form className="form_container" onSubmit={handleSubmit}>
            <h1>Login</h1>

            <div className="input_box">
              <input
                type="username"
                placeholder="Username"
                name="username"
                onChange={handleChange}
                value={data.username}
                required
                className="input"
              />
            </div>
            <div className="input_box">
              <input
                type="password"
                placeholder="Password"
                name="password"
                onChange={handleChange}
                value={data.password}
                required
                className="input"
              />
            </div>
            {error && <div className="error_msg">{error}</div>}
            <button type="submit" className="green_btn">
              Login
            </button>
            <h5>
              Don't have an account?{" "}
              <Link className="linkStyle" to="/register">
                SignUp
              </Link>
            </h5>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
