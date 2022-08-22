import React from "react";

export default function Introduction(){
    return(
        <div className="container-fluid bg-secondary text-dark mt-5 pt-5">
            <div className='row px-xl-5 pt-5'>
                <div className='col-lg-4 col-md-12 mb-5 pr-3 pr-xl-5'>
                    <p>優秀的「關於我們」頁面，必然是從閱聽眾的角度出發，思考訪客會對哪些內容感興趣，或者對某些資訊有所需求？而不是只考量自己想要說什麼，或者急於推銷商品。</p>
                    <p class="mb-2"><i class="fa fa-envelope text-primary "></i>mis@gmail.com</p>
                    <p class="mb-0"><i class="fa fa-phone-alt text-primary "></i>+07 2567890</p>
                </div>
                <div className="col-lg-8 col-md-12">
                    <div className="row">
                        <div className="col-md-4 mb-5">
                            <h5 class="font-weight-bold text-dark mb-4">參考網站</h5>
                            
                            <div class="d-flex flex-column justify-content-start">
                                <a class="text-dark mb-2" href="https://term.ptt.cc/"><i class="fa fa-angle-right "></i>批踢踢實業坊</a>
                                <a class="text-dark mb-2" href="https://www.mobile01.com/"><i class="fa fa-angle-right "></i>mobile01</a>
                                <a class="text-dark mb-2" href="https://www.dcfever.com/"><i class="fa fa-angle-right "></i>DCfever</a>
                                <a class="text-dark mb-2" href="https://chinese.engadget.com/"><i class="fa fa-angle-right "></i>Engadget</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </div>

    );

}