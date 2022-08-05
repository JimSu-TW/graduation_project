// Navbar.jsx
import React from "react"; //要載入react，JSX才能被編譯
import { Navbar, Nav, NavDropdown, Form, FormControl, Button, Container } from "react-bootstrap";

export default function NavbarMenu() {
    return (
        <Navbar collapseOnSelect bg="dark" expand="lg"  variant="dark" sticky="top" >
            <Container>
                <Navbar.Brand href="#home">logo</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse  id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <NavDropdown title="手機" id="basic-nav-dropdown">
                            <NavDropdown.Item href="#">Apple</NavDropdown.Item>
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
                    <Form  className="d-flex">
                        <FormControl type="text" placeholder="Search" className="me-2" />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Container>
            
        </Navbar>
    );
}
