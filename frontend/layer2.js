import './style.css';

function Layout(){
    
    return (
        <div>
            <div className="container-fluid bg-secondary mb-5">
                <div className="d-flex flex-column align-items-center justify-content-center brand_banner">
                    <h1 className="font-weight-semi-bold text-uppercase mb-3">APPLE</h1>
                    <div className="d-inline-flex">
                        <p className="m-0"><a href="layer1.html">Home</a></p>
                    </div>
                </div>
            </div>

            <div class="container-fluid pt-5">
                <div class="row px-xl-5">
                    <div className="col-lg-3 col-md-12">

                        <div className="border-bottom mb-4 pb-4">
                            <h5 className="font-weight-semi-bold mb-4">容量</h5>
                            <form>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="price-all">所有容量</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="price-1">64GB</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="price-2">128GB</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="price-3">256GB</label>
                                </div>
                            </form>
                        </div>

                        <div className="mb-5">
                            <h5 className="font-weight-semi-bold mb-4">手機尺寸</h5>
                            <form>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-all">所有尺寸</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-1">5~6吋</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-2">6~7吋</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-3">7吋以上</label>
                                </div>
                            </form>
                        </div>

                        <div className="mb-5">
                            <h5 className="font-weight-semi-bold mb-4">其他</h5>
                            <form>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-all">所有</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-1">快充</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-2">無線充電</label>
                                </div>
                                <div className="custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3">

                                    <label className="custom-control-label" for="size-3">防水</label>
                                </div>
                            </form>
                        </div>
                    </div>

                    <div className="col-lg-9 col-md-12">
                        <div className="row pb-3">
                            <div className="col-12 pb-1">
                                <div className="d-flex align-items-center justify-content-between mb-4">
                                    <form action="">
                                        <div className="input-group">

                                            <div className="input-group-append">
                                                <span className="input-group-text bg-transparent text-primary">
                                                    <i className="fa fa-search"></i>
                                                </span>
                                            </div>
                                        </div>
                                    </form>
                                    <div className="dropdown ml-4">
                                        <button className="btn border dropdown-toggle" type="button" id="triggerId" data-toggle="dropdown" aria-haspopup="true"
                                                aria-expanded="false">
                                                    Sort by
                                        </button>
                                        <div className="dropdown-menu dropdown-menu-right" aria-labelledby="triggerId">

                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="col-lg-4 col-md-6 col-sm-12 pb-1">
                                <div className="card product-item border-0 mb-4">
                                    <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-0">
                                        <a href="layer3.html">

                                        </a>
                                    </div>
                                    <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                                        <h6 className="text-truncate mb-3">iPhone13 pro</h6>
                                    </div>
                                </div>
                            </div>
                            <div className="col-lg-4 col-md-6 col-sm-12 pb-1">
                                <div className="card product-item border-0 mb-4">
                                    <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-0">

                                    </div>
                                    <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                                        <h6 className="text-truncate mb-3">iPhone13 pro</h6>
                                    </div>
                                </div>
                            </div>
                            <div className="col-lg-4 col-md-6 col-sm-12 pb-1">
                                <div className="card product-item border-0 mb-4">
                                    <div className="card-header product-img position-relative overflow-hidden bg-transparent border p-0">

                                    </div>
                                    <div className="card-body border-left border-right text-center p-0 pt-4 pb-3">
                                        <h6 className="text-truncate mb-3">iPhone13 pro</h6>
                                    </div>
                                </div>
                            </div>

                            <div className="col-12 pb-1">
                                <nav aria-label="Page navigation">
                                    <ul className="pagination justify-content-center mb-3">
                                        <li className="page-item disabled">

                                        </li>
                                        <li className="page-item active"></li>
                                        <li className="page-item"></li>
                                        <li className="page-item"></li>
                                        <li className="page-item">

                                        </li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Layout;