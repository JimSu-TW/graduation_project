import React from "react";
import  '../style.css';
import logo from "../Page/images/logo.png"
export default function About(){

    return(
        <div className="row p-0 m-0 pt-5 mt-5 bg-about">
            <div className="col-lg-4 col-md-12 mb-5 pr-3 px-xl-5">
                <img src={logo} className="img_logo p-0 m-0 " alt='logo'></img>
            </div>
            
            <div className="col-lg-4 col-md-12 mb-5 mt-4 pr-3 px-xl-5">
                <p className="about"> 指在提供使用者最輕便簡潔的資訊。EZRater從科技產品著手，利用資料抓取以及資料前處理，
                    加上AI協助辨別詞性後去除繁冗的文字，留下關鍵字讓使用者可以快速了解產品特性。
                    透過網頁呈現市面上科技產品，讓使用者可以快速選擇自己所需的商品。
                </p>
            </div>
            <div className="col-md-4 mb-5 about  ">
                <h5 className="font-weight-bold text-dark mb-4">參考網站</h5>
                <div className="d-flex flex-column justify-content-start">
                    <ul className="pt-2">
                        <li><a className="text-dark mb-2" href="https://term.ptt.cc/"><i className="fa fa-angle-right mr-2"></i>批踢踢實業坊</a></li>
                        <li><a className="text-dark mb-2" href="https://www.mobile01.com/"><i className="fa fa-angle-right mr-2"></i>mobile01</a></li>
                        <li><a className="text-dark mb-2" href="https://www.dcfever.com/"><i className="fa fa-angle-right mr-2"></i>DCfever</a></li>
                        <li><a className="text-dark mb-2" href="https://chinese.engadget.com/"><i className="fa fa-angle-right mr-2"></i>Engadget</a></li>
                    </ul>
                </div>
            </div>
        </div>
    );

}

