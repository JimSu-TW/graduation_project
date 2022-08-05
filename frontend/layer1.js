import React, { useState, useEffect } from 'react';
import './style.css';

function Layout(){
    // 宣告hook變數
    const [phone, setPhone] = useState({
        phone1: "",
        phone2: "",
        phone3: "",
        phone4: "",
        phone5: "",
        phone6: ""
    });
    // 連結api上的json取產品名稱
    useEffect(() => {
        fetch("http://127.0.0.1:5000/phone").then((res) =>
            res.json().then((phone) => {
                setPhone({
                    phone1: phone.ph1,
                    phone2: phone.ph2,
                    phone3: phone.ph3,
                    phone4: phone.ph4,
                    phone5: phone.ph5,
                    phone6: phone.ph6
                });
            })
        );
    }, []);
    
    return (
        <div className='container-fluid pt-5'>
            <div className='text-center mb-4'>
                <header className="px-5">
                    <span className='px-2'><h2 className="rank-header">熱門手機</h2></span>
                </header>
            </div>
            <div className="row px-xl-5 pb-3 ">
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                            
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone1}</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone2}</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone3}</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone4}</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone5}</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">{phone.phone6}</h6>
                        </div>
                    </div>
                </div>
            </div>
            <div className='text-center mb-4'>
                <header className="px-5">
                    <span className='px-2'><h2 className="rank-header">熱門平板</h2></span>
                </header>
            </div>
            <div className="row px-xl-5 pb-3 ">
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                            
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini(讀資料庫)</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini(讀資料庫)</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini(讀資料庫)</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini(讀資料庫)</h6>
                        </div>
                    </div>
                </div>
                <div className="col-lg-2 col-md-6 col-sm-12 pb-1">
                    <div className="card product-item border-0 mb-4">
                        <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-100">
                        
                        </div>
                        <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 className="text-truncate mb-3">iPad mini(讀資料庫)</h6>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    );
}

export default Layout;