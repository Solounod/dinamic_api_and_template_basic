import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.css'
import { MainPage } from "./containers/pages/MainPage";
import { RegisterPage } from "./containers/pages/RegisterPage";
import { LoginPage } from "./containers/pages/LoginPage";


function App() {

  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="/Register" element={<RegisterPage/>}/>
        <Route path="/Login" element={<LoginPage/>}/>
      </Routes>
    </BrowserRouter>
  )
  
}

export default App
