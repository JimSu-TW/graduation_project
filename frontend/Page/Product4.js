import React, { useState, useEffect } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import { FixedSizeList as List } from 'react-window';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';

import '../style.css';
import dcfever from "./images/sourcepic/dcfever.png";
import engadget from "./images/sourcepic/engadget.jpg";
import mobile01 from "./images/sourcepic/mobile01.jpg";
import ptt from "./images/sourcepic/ptt.png";

const API_Post = "http://127.0.0.1:5000/api/iphone13pro/phonepost";
const API_FtBudget = "http://127.0.0.1:5000/api/iphone13pro/feature/budget";
const API_FtWafer = "http://127.0.0.1:5000/api/iphone13pro/feature/wafer";
const API_FtScreen = "http://127.0.0.1:5000/api/iphone13pro/feature/screen";
const API_FtBattery = "http://127.0.0.1:5000/api/iphone13pro/feature/battery";
const API_FtLens = "http://127.0.0.1:5000/api/iphone13pro/feature/lens";
const API_FtCapacity = "http://127.0.0.1:5000/api/iphone13pro/feature/capacity";

function SrcImg(props) {
    const srcImg = props.srcImg;
    if(srcImg === 1) {
        return ( <img src={dcfever} alt="dcfever" className="img_source"></img> );
    } else if(srcImg === 2 ) {
        return ( <img src={engadget} alt="engadget" className="img_source"></img> );
    } else if(srcImg === 3) {
        return ( <img src={mobile01} alt="mobile01" className="img_source"></img> );
    } else if(srcImg === 4) {
        return ( <img src={ptt} alt="ptt" className="img_source"></img> );
    }
}

function ScrollPost() {
    const [post, setPost] = useState([]);
    useEffect(() => {
        fetch(API_Post)
            .then(res => res.json())
            .then(post => setPost(post))
            .catch(console.error);
    }, []);

    const ScrollPart = ({ item }) => {
        const PostItem = item.map((post) =>
            <li className="media post-text-ul-style py-1" key={post.post_id}>
                <SrcImg srcImg={post.src_id} />
                <div>
                    <a href={post.link} >{post.title}</a><small><i> 日期: {post.date}</i></small>
                </div>
            </li>
        );
    
        const PostPart = ({ style }) => (
            <div style={style}>
                {PostItem}
            </div>
        );
    
        const ScrollItem = () => (
            <List
                innerElementType="ul"
                itemCount={1}
                itemSize={20}
                height={240}
                width={560}
            >
                {PostPart}
            </List>
        );

        return <ScrollItem />;
    }

    // 下拉式選單
    const DropdownBtns = ({ filterItem, setSrcItem }) => {
        return (
            <DropdownButton className="btn" id="dropdown-basic-button" title="Select">
                <Dropdown.Item onClick={() => setSrcItem(post)}>all</Dropdown.Item>
                <Dropdown.Item onClick={() => filterItem(4)}>ptt</Dropdown.Item>
                <Dropdown.Item onClick={() => filterItem(3)}>mobile01</Dropdown.Item>
                <Dropdown.Item onClick={() => filterItem(2)}>engadget</Dropdown.Item>
                <Dropdown.Item onClick={() => filterItem(1)}>dcfever</Dropdown.Item>
            </DropdownButton>
        );
    };

    const SelectSrc = () => {
        const [srcItem, setSrcItem] = useState(post);
        const filterItem = (curSrc) => {
            const newItem = post.filter((newPost) => {
                return newPost.src_id === curSrc;
            }); 
            setSrcItem(newItem);
        };
        return (
            <div>
                <div className="dropdown-pg3">
                    <DropdownBtns
                        filterItem={filterItem}
                        setSrcItem={setSrcItem}
                    />
                </div>
                <ScrollPart item={srcItem} />
            </div>
        );
    };

    return <SelectSrc />;
}

function GetFtBudget() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtBudget)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow ">
            <div className="card-body">
                <div className="row no-gutters align-items-center">
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary">
                            <p className="key-text-size">預算</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800 feature_card">
                            <ul className="key-text-ul-style " key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

function GetFtWafer() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtWafer)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow">
            <div className="card-body feature_div">
                <div className="row no-gutters align-items-center">
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary">
                            <p className="key-text-size">晶片</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800  ">
                            <ul className="key-text-ul-style" key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

function GetFtScreen() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtScreen)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow">
            <div className="card-body">
                <div className="row no-gutters align-items-center">
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary">
                            <p className="key-text-size">螢幕</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800 ">
                            <ul className="key-text-ul-style" key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

function GetFtBattery() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtBattery)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow mt-3">
            <div className="card-body">
                <div className="row no-gutters align-items-center feature_div" >
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary ">
                            <p className="key-text-size">電池</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                            <ul className="key-text-ul-style" key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

function GetFtLens() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtLens)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow mt-3">
            <div className="card-body">
                <div className="row no-gutters align-items-center">
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary">
                            <p className="key-text-size">鏡頭</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                            <ul className="key-text-ul-style" key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

function GetFtCapacity() {
    const [feature, setFeature] = useState([]);
    useEffect(() => {
        fetch(API_FtCapacity)
            .then(res => res.json())
            .then(feature => setFeature(feature))
            .catch(console.error);
    }, []);

    return (
        <div className="key-card shadow mt-3">
            <div className="card-body">
                <div className="row no-gutters align-items-center">
                    <div className="col mr-2">
                        <div className="font-weight-bold text-primary">
                            <p className="key-text-size">容量</p>
                        </div>
                        <div className="h4 mb-0 text-center font-weight-bold text-gray-800">
                            <ul className="key-text-ul-style" key={feature.label_id}>
                                {feature.map(feature => (
                                    <li>{feature.content}</li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default function Pd4() {
    return (
        <div className="container-fluid py-3">
            <div className="row px-xl-5 py-xl-3">
                <div className="col-lg-5 pb-5">
                    <div className="border mt-5">
                        <div className="active mx-5 my-5 ">
                            <img src={require("./images/popularph/ph4.jpg")} alt="ph1" className="img_banner w-100 h-100"></img>
                        </div>
                    </div>
                </div>
                <div className="col-lg-7 pb-2">
                    <header className="px-5">
                        <span className="px-2"><h2 className="font-weight-semi-bold mb-1 text-center">iPhone 13 Pro</h2></span>
                    </header>
                    <div className="row px-xl-5">
                        <div className="col">
                            <Tabs
                                defaultActiveKey="tab-pane-1"
                                transition={true}
                                id="tab-details"
                                className="nav nav-tabs justify-content-center border-secondary mb-3"
                            >
                                <Tab eventKey="tab-pane-1" title="產品介紹">
                                    <div className="tab-pane show" id="tab-pane-1">
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
                                                    <td><p>A15</p></td>
                                                </tr>
                                                <tr>
                                                    <th><p>ROM 容量</p></th>
                                                    <td><p>128GB / 256GB / 512GB/1TB ROM</p></td>
                                                </tr>
                                                <tr>
                                                    <th><p>螢幕尺寸</p></th>
                                                    <td><p>6.1 吋</p></td>
                                                </tr>
                                                <tr>
                                                    <th><p>機身顏色</p></th>
                                                    <td><p>石墨、金、銀及天峰藍色</p></td>
                                                </tr>
                                                </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </Tab>
                                <Tab eventKey="tab-pane-2" title="產品特色">
                                    <div className="tab-pane show" id="tab-pane-2">
                                        <div className="row" >
                                            <div className="col-md-4"><GetFtBudget /></div>
                                            <div className="col-md-4"><GetFtWafer /></div>
                                            <div className="col-md-4"><GetFtScreen /></div>
                                            <div className="col-md-4"><GetFtBattery /></div>
                                            <div className="col-md-4"><GetFtLens /></div>
                                            <div className="col-md-4"><GetFtCapacity /></div>
                                        </div>
                                    </div>
                                </Tab>
                                <Tab eventKey="tab-pane-3" title="產品評論">
                                    <div className="tab-pane show" id="tab-pane-3">
                                        <div className="row">
                                            <div className="col-md-12">
                                                <ScrollPost />
                                            </div>
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