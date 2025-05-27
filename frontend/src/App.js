import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPageRegister from './pages/LoginregisterPage';
import DashboardPage from './pages/Dashboard';
import TopBar from "./components/TopBar";
import CharacterDetailPage from "./pages/CharacterDetailPage";

function App() {
  return (
    <Router>
      <TopBar /> 
      <Routes>        
        <Route path="/" element={<LoginPageRegister />} />
        <Route path="/dashboard" element={<DashboardPage />} /> 
        <Route path="/characters/:id" element={<CharacterDetailPage />} />
      </Routes>
    </Router>
  );
}

export default App;
