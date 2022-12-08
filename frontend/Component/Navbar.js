// Navbar.js
import React from "react"; //要載入react，JSX才能被編譯
import { Navbar, Nav, NavDropdown, Container } from "react-bootstrap";
import{ BrowserRouter as Router,Route,Routes,Link} from "react-router-dom";
import Page1 from '../Page/Layer1';
import Page2 from '../Page/Layer2'; 
import Page3 from '../Page/Layer3';
import Pd2 from '../Page/Product2';
import Pd3 from '../Page/Product3';
import Pd4 from '../Page/Product4';
import Pd5 from '../Page/Product5';
import Pd6 from '../Page/Product6';
export default function NavbarMenu(){

    return(
        <Router>
            <Navbar   expand="lg" sticky="top"  className="py-2  navbar_menu navbar-light bg-light "   >
                <Container>
                    <Navbar.Brand href="#home"><Link to ="/home">EZrater</Link></Navbar.Brand>

                    
                    <Navbar.Collapse  id="basic-navbar-nav">
                        <Nav  >
                            <NavDropdown title="手機" id="basic-nav-dropdown" >
                                <NavDropdown.Item href="#"><Link to="/apple">Apple</Link></NavDropdown.Item>
                                <NavDropdown.Item href="#">Oppa</NavDropdown.Item>
                                <NavDropdown.Item href="#">ASUS</NavDropdown.Item>
                                <NavDropdown.Item href="#">Vivo</NavDropdown.Item>
                                <NavDropdown.Item href="#">Sony</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="平板" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#">Apple</NavDropdown.Item>
                                <NavDropdown.Item href="#">Samsung</NavDropdown.Item>
                                <NavDropdown.Item href="#">ASUS</NavDropdown.Item>
                                <NavDropdown.Item href="#">Sony</NavDropdown.Item>
                                <NavDropdown.Item href="#">Lenovo</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="電腦" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#">Apple</NavDropdown.Item>
                                <NavDropdown.Item href="#">Acer</NavDropdown.Item>
                                <NavDropdown.Item href="#">ASUS</NavDropdown.Item>
                                <NavDropdown.Item href="#">HP</NavDropdown.Item>
                                <NavDropdown.Item href="#">Lenovo</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="數位相機/類單" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#">CASIO</NavDropdown.Item>
                                <NavDropdown.Item href="#">Canon</NavDropdown.Item>
                                <NavDropdown.Item href="#">Sony</NavDropdown.Item>
                                <NavDropdown.Item href="#">Nikon</NavDropdown.Item>
                                <NavDropdown.Item href="#">Fujifilm</NavDropdown.Item>
                            </NavDropdown>
                            <NavDropdown title="單眼相機" id="basic-nav-dropdown">
                                <NavDropdown.Item href="#">CASIO</NavDropdown.Item>
                                <NavDropdown.Item href="#">Canon</NavDropdown.Item>
                                <NavDropdown.Item href="#">Sony</NavDropdown.Item>
                                <NavDropdown.Item href="#">Nikon</NavDropdown.Item>
                                <NavDropdown.Item href="#">Fujifilm</NavDropdown.Item>
                            </NavDropdown>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>    
            <Routes>
                <Route exact path="/" element={<Page1/>} ></Route>
                <Route path="/home" element={<Page1/>} ></Route>
                <Route path="/apple" element={<Page2/>}></Route>
                
                <Route path="/iPhoneSE3" element={<Page3/>}></Route>
                <Route path="/iPhone13mini" element={<Pd2/>}></Route>
                <Route path="/iPhone13" element={<Pd3/>}></Route>
                <Route path="/iPhone13Pro" element={<Pd4/>}></Route>
                <Route path="/iPhone13ProMax" element={<Pd5/>}></Route>
                <Route path="/iPhone12mini" element={<Pd6/>}></Route>

            </Routes>            
        </Router>
    );
}