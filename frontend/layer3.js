import React, { useState, useEffect } from 'react';
import './style.css';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import ph1 from "./images/popularph/ph1.jpg";
import dcfever from "./images/sourcepic/dcfever.png";
import engadget from "./images/sourcepic/engadget.jpg";
import mobile01 from "./images/sourcepic/mobile01.jpg";
import ptt from "./images/sourcepic/ptt.png";

const API_Post = "http://127.0.0.1:5000/api/phonepost";

function Layout(){
    // 宣告hook變數
    const [post, setPost] = useState([]);
    // 連結api上的json取產品名稱
    useEffect(() => {
        fetch(API_Post)
            .then(res =>res.json())
            .then(post => setPost(post))
            .catch(console.error);
    }, []);

    console.log(post)

    // 一次處理多項留言
    const PostItems = post.map((post) =>
        <div className="tab-pane show" id="tab-pane-3">
            <div className="row">
                <ul className="col-md-12 post-text-ul-style">
                    <li className="media my-1">
                        <img src={mobile01} alt="ptt" className="img_source"></img>
                        <div key={post.post_id}>
                            <a href={post.link}>{post.title}</a><small><i> {post.date}</i></small>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    );

    return (

        <div className="container-fluid py-3">
            <div className="row px-xl-5 py-xl-3">
                <div className="col-lg-5 pb-5">
                    <div className="border">
                        <div className="active mx-5 my-5">
                            <img src={ph1} alt="ph1" className="img_banner w-100 h-100"></img>
                        </div>
                    </div>
                </div>
    
                <div className="col-lg-7 pb-2">
                    <header className="px-5">
                        <span className="px-2"><h2 className="font-weight-semi-bold mb-4 text-center">iPhone SE 3</h2></span>
                    </header>
                    <div className="row px-xl-5">
                        <div className="col">
                            <Tabs
                                defaultActiveKey="tab-pane-1"
                                transition={true}
                                id="tab-test"
                                className="nav nav-tabs justify-content-center border-secondary mb-4"
                            >
                                <Tab eventKey="tab-pane-1" title="產品介紹">
                                    <div className="tab-pane show active" id="tab-pane-1">
                                        <div className="attributesArea">
                                            <div>
                                                <table id="attributesTable" cellSpacing="0" cellPadding="5" width="100%" border="1">
                                                <tbody>
                                                    <tr>
                                                        <th><p>品牌</p></th>
                                                        <td><p>Apple</p></td>
                                                    </tr>
                                                    <tr>
                                                        <th><p>中央處理器</p></th>
                                                        <td><p>A15 Bionic</p></td>
                                                    </tr>
                                                    <tr>
                                                        <th><p>ROM 容量</p></th>
                                                        <td><p>64GB/128GB/256GB ROM</p></td>
                                                    </tr>
                                                    <tr>
                                                        <th><p>螢幕尺寸</p></th>
                                                        <td><p>4.7 吋</p></td>
                                                    </tr>
                                                    <tr>
                                                        <th><p>機身顏色</p></th>
                                                        <td><p>午夜暗色、星光色及 (PRODUCT)RED</p></td>
                                                    </tr>
                                                </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </Tab>
                                <Tab eventKey="tab-pane-2" title="產品特色">
                                    <div className="tab-pane show" id="tab-pane-2">
                                        <div className="row">
                                            <div className="col-md-4">
                                                <div className="key-card shadow h-100 py-2">
                                                    <div className="card-body">
                                                        <div className="row no-gutters align-items-center">
                                                            <div className="col mr-2">
                                                                <div className="font-weight-bold text-primary text-uppercase mb-1">
                                                                    <p className="key-text-size">CP值</p>
                                                                </div>
                                                                <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                                                                    <ul className="key-text-ul-style">
                                                                        <li>性價比高</li>
                                                                        <li>價錢合理</li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="col-md-4">
                                                <div className="key-card shadow h-100 py-2">
                                                    <div className="card-body">
                                                        <div className="row no-gutters align-items-center">
                                                            <div className="col mr-2">
                                                                <div className="font-weight-bold text-primary text-uppercase mb-1">
                                                                    <p className="key-text-size">性能</p>
                                                                </div>
                                                                <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                                                                    <ul className="key-text-ul-style">
                                                                        <li>高續航</li>
                                                                        <li>夜拍清晰</li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="col-md-4">
                                                <div className="key-card shadow h-100 py-2">
                                                    <div className="card-body">
                                                        <div className="row no-gutters align-items-center">
                                                            <div className="col mr-2">
                                                                <div className="font-weight-bold text-primary text-uppercase mb-1">
                                                                    <p className="key-text-size">外觀</p>
                                                                </div>
                                                                <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                                                                    <ul className="key-text-ul-style">
                                                                        <li>顏色多樣</li>
                                                                        <li>外表亮麗</li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </Tab>
                                <Tab eventKey="tab-pane-3" title="產品評論">
                                    <div className="tab-pane show" id="tab-pane-3">
                                        <div className="row">
                                            {PostItems}
                                        </div>
                                    </div>
                                </Tab>
                            </Tabs>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Layout;