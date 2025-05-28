import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPageRegister from './pages/LoginregisterPage';
import DashboardPage from './pages/Dashboard';
import TopBar from "./components/TopBar";
import CharacterDetailPage from "./pages/CharacterDetailPage";
import CreateCharacter from "./pages/CreateCharacter";

function App() {
  return (
    <Router>
      <TopBar /> 
      <Routes>        
        <Route path="/" element={<LoginPageRegister />} />
        <Route path="/dashboard" element={<DashboardPage />} /> 
        <Route path="/characters/:id" element={<CharacterDetailPage />} />
        <Route path="/create-character" element={<CreateCharacter />} />
      </Routes>
    </Router>
  );
}

export default App;
