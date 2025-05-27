import React, { useState } from 'react';
import api from '../api/axios';
import { useNavigate } from "react-router-dom";

function LoginRegisterPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const navigate = useNavigate();

  const resetForm = () => {
    setEmail('');
    setPassword('');
    setUsername('');
    setErrorMsg('');
    setSuccessMsg('');
  };

  const validateForm = () => {
    const emailRegex = /^[^@]+@[^@]+\.[^@]+$/;

    if (!emailRegex.test(email)) {
      setErrorMsg("Geçerli bir e-posta adresi girin.");
      return false;
    }

    if (!isLogin && password.length < 6) {
      setErrorMsg("Şifre en az 6 karakter olmalıdır.");
      return false;
    }

    if (!isLogin && username.length < 3) {
      setErrorMsg("Kullanıcı adı en az 3 karakter olmalıdır.");
      return false;
    }

    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMsg('');
    setSuccessMsg('');

    if (!validateForm()) return;

    try {
      if (isLogin) {
        const response = await api.post('/login', { email, password });
        const token = response.data.access_token;
        localStorage.setItem('token', token);
        navigate('/Dashboard')
      } else {
        await api.post('/register', { email, password, username });
        setSuccessMsg('Kayıt başarılı! Şimdi giriş yapabilirsin.');
        setIsLogin(true);
        resetForm();
      }
    } catch (error) {
      console.error(error);
      setErrorMsg(error.response?.data?.error || 'Bir hata oluştu');
    }
  };

  return (
    <div>
      <h2>{isLogin ? 'Giriş Yap' : 'Kayıt Ol'}</h2>
      <form onSubmit={handleSubmit}>
        {!isLogin && (
          <div>
            <input
              type="text"
              placeholder="Kullanıcı Adı"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required={!isLogin}
            /><br/>
          </div>
        )}
        <input
          type="email"
          placeholder="E-posta"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        /><br/>
        <input
          type="password"
          placeholder="Şifre"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        /><br/>
        <button type="submit">{isLogin ? 'Giriş' : 'Kayıt Ol'}</button>
      </form>

      {errorMsg && <p style={{ color: 'red' }}>{errorMsg}</p>}
      {successMsg && <p style={{ color: 'green' }}>{successMsg}</p>}

      <p>
        {isLogin
          ? "Hesabın yok mu? "
          : "Zaten hesabın var mı? "}
        <button onClick={() => { setIsLogin(!isLogin); resetForm(); }}>
          {isLogin ? "Kayıt Ol" : "Giriş Yap"}
        </button>
      </p>
    </div>
  );
}

export default LoginRegisterPage;
