import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    referred_by_code: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/user/register/', formData, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((response) => {
      console.log('User registered:', response.data);
    })
    .catch((error) => {
      if (error.response) {
        console.error('There was an error!', error.response.data);
      } else {
        console.error('Error:', error.message);
      }
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
      <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
      <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
      <input type="text" name="referred_by_code" placeholder="Referral Code (optional)" onChange={handleChange} />
      <button type="submit">Register</button>
    </form>
  );
};

export default Register;
