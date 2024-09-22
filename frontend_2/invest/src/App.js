import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './component/Login';
import PreHome from './component/PreHome';
import Homepage from './component/Homepage';
import Register from './component/Register';
import Logout from './component/Logout';





function App() {
  return (
    <div className="App">
       <Router>
        <Routes>
          {/* Define routes for different components */}
          <Route path="/" element={<PreHome />} /> {/* Assuming PreHome is your landing page */}
          <Route path="/home" element={<Homepage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
