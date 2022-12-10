import '../style.css';
import React from 'react';
import PRODUCTS from '../ProductsJson.json';
import { Link } from "react-router-dom";

const {
    useCallback,
    useState,
} = React

const Capacity = [
    "64GB",
    "128GB",
    "256GB"
]

function ProductFilters(props) {
    const {
        categories,
        onFilterChange,
    } = props

    return (
        <div className="filters">
            <header id="filters-header">
                <h4 className="font-weight-semi-bold mb-4">容量</h4>
            </header>
            <ul className="filters-content">
                {categories.map(category => (
                    <div key={category} class="">
                        <label class="filter-label">
                            <input
                                class="filter-checkbox"
                                type="checkbox"
                                onChange={onFilterChange}
                                value={category} />
                            {category}
                        </label>
                    </div>
                ))}
            </ul>
        </div>
    )
}

function Product(props) {
    const { product } = props

    return (
        <li
            key={product.id}
            className="product">
            <Link to={"/"+product.name.replace(/\s*/g,"")}>
                <img 
                    src={require("./images/popularph/"+ product.name +".jpg")}
                    alt="phone"
                    className="img_banner">
                </img>
                <div className="product-details">
                    <header>{product.name}</header>
                </div>
            </Link>
        </li>
    )
}

function ProductsList(props) {
    const { products } = props

    return (
        <ul className="products">
            {products.map(product => (
                <Product product={product} />
            ))}
        </ul>
    )
}

function ProductList1(props) {
    const { products } = props

    return (
        <ul className="products">
            {products.map(product => (
                <li
                    key={product.id}
                    className="product">
                    <Link to={"/"+product.name.replace(/\s*/g,"")}>
                        <img 
                            src={require("./images/popularph/"+ product.name +".jpg")}
                            alt="phone"
                            className="img_banner">
                        </img>
                        <div className="product-details">
                            <header>{product.name}</header>
                        </div>
                    </Link>
                </li>
            ))}
        </ul>
    )
}

function Layout (){
    const [state, setState] = useState({
        products: PRODUCTS,
        filters: new Set(),
    })
    const handleFilterChange = useCallback(event => {
        setState(previousState => {
            let filters = new Set(previousState.filters)
            let products = PRODUCTS

            if (event.target.checked) {
                filters.add(event.target.value)
            } else {
                filters.delete(event.target.value)
            }

            if (filters.size) {
                products = products.filter(product => {
                    return filters.has(product.category)
                })
            }

            return {
                filters,
                products,
            }
        })
    }, [setState])
    
    return(
        <div>
            <div className="container-fluid bg-secondary mb-5">
                <div className="d-flex flex-column align-items-center justify-content-center brand_banner">
                    <h1 className="font-weight-semi-bold text-uppercase mb-3">APPLE</h1>
                    <div className="d-inline-flex">
                       <Link to="/home"><p> Home</p></Link>
                    </div>
                </div>
            </div>

            <div class="container-fluid pt-5">
                <div class="row px-xl-5">
                    <div className="col-lg-3 col-md-12">

                        <div className="border-bottom mb-4 pb-4">
                            <ProductFilters
                                categories={Capacity}
                                onFilterChange={handleFilterChange} />
                        </div>
                    </div>
                    <ProductList1 products={state.products} />
                </div>
            </div>
        </div>
    )
}
export default Layout;