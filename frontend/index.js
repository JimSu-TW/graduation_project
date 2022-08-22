import 'bootstrap/dist/css/bootstrap.min.css';
import * as React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import NavbarMenu from "./components/Navbar"; //載入component
import Introduction from "./components/introduction";
import Layout from './layer1';
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter } from "react-router-dom";
import banner from "./images/banner.jpg"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <NavbarMenu/>  
        <BrowserRouter>
        <img src={banner} alt="banner" className="img_banner"></img>
            <Layout/>
        </BrowserRouter>
        <Introduction/>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals