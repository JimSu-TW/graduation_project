import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import '../style.css';
import banner from "../Page/images/banner.jpg"

const API_GetAppleProduct = "http://127.0.0.1:5000/api/applepop";
const API_GetGoogleProduct = "http://127.0.0.1:5000/api/googlepop";

function ProductList1() {
    const [product, setProduct] = useState([]);
    useEffect(() => {
        fetch(API_GetAppleProduct)
            .then(res => res.json())
            .then(product => setProduct(product))
            .catch(console.error);
        
    }, []);

    return (
        <div className="container-fluid pb-5">
            <div className="row px-xl-4 pb-3">
                {product.map(product => (
                    <div className="col-lg-2 col-md-6 col-sm-12 pb-1" key={product.product_id}>
                        <div className="card product-item border-0 mb-4" >
                            <Link to={"/"+product.name.replace(/\s*/g,"")}>
                                <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-0">
                                    <img 
                                        src={require("./images/popularph/"+ product.name +".jpg")}
                                        alt="phone"
                                        className="img_banner">    
                                    </img>
                                </div>
                                <div className="card-body border-left border-right border-bottom text-center p-0 pt-4 pb-3">
                                    <h6 className="text-truncate mb-3">{product.name}</h6>
                                </div>
                            </Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

function ProductList2() {
    const [product, setProduct] = useState([]);
    useEffect(() => {
        fetch(API_GetGoogleProduct)
            .then(res => res.json())
            .then(product => setProduct(product))
            .catch(console.error);
    }, []);

    return (
        <div className="container-fluid pb-5">
            <div className="row px-xl-4 pb-3">
                {product.map(product => (
                    <div className="col-lg-2 col-md-6 col-sm-12 pb-1" key={product.product_id}>
                        <div className="card product-item border-0 mb-4">
                        <Link to ={"/iPhoneSE3"}>
                            <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-0">
                                <img 
                                    src={require("./images/popularph/"+ product.name +".jpg")}
                                    alt="phone"
                                    className="img_banner">    
                                </img>
                            </div>
                            <div className="card-body border-left border-right border-bottom text-center p-0 pt-4 pb-3">
                                <h6 className="text-truncate mb-3">{product.name}</h6>
                            </div>
                        </Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default function Page1 () {
    return(
        <div className="p-0 m-0">
            <img src={banner} className="img_banner p-0 m-0 " alt='banner'></img>
            <div className="text-center mb-4 container-fluid pt-5">
                <header className="px-5 section-title">
                    <span className="px-2"><h2 className="rank-header">熱門手機</h2></span>
                </header>
            </div>
            <ProductList1 />
            
        </div>
    );
}
