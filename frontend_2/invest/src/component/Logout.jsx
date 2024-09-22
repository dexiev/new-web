import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const Logout = () => {
    const navigate = useNavigate();

  const handleLogout = () => {
    const refreshToken = localStorage.getItem('refresh_token');

    if (!refreshToken) {
      console.error('No refresh token found.');
      return;
    }

    axios.post('http://localhost:8000/user/logout/', { refresh_token: refreshToken })
      .then(() => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        console.log('Logout successful!');
        navigate('/');  // Redirect to the homepage

      })
      .catch((error) => {
        console.error('Logout failed:', error.response?.data || error.message);
      });
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
};

export default Logout;
