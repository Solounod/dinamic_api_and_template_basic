import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { RegisterLoginBar } from "./RegisterLoginBar";

export function NavbarBase() {
    const navigate = useNavigate()

    const [prevScrollTop, setPrevScrollTop] = useState(0);
    const [currentScrollTop, setCurrentScrollTop] = useState(0);

    useEffect(() => {
        const handleScroll = () => {
            const scrollTop = document.body.parentNode.scrollTop;
            const headerHeight = document.querySelector('.header').offsetHeight;

            setCurrentScrollTop(scrollTop);

            if (prevScrollTop < currentScrollTop && scrollTop > headerHeight * 2) {
                document.querySelector('.header').classList.add('scrollUp');
            } else if (prevScrollTop > currentScrollTop && !(scrollTop <= headerHeight)) {
                document.querySelector('.header').classList.remove('scrollUp');
            }

            setPrevScrollTop(currentScrollTop);
        };

        window.addEventListener('scroll', handleScroll);

        //clear component
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, [prevScrollTop, currentScrollTop]);

    const handleBrandClick = (route) => {
        navigate(route)
    }

    return (
        <header className="expand-header fixed-top header">
            
            <Navbar expand="lg" className="bg-body-tertiary p-3  " >
            <RegisterLoginBar />
                <Container>
                    <Navbar.Brand onClick={() => handleBrandClick("/")}>Logo empresa</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" className="" />
                    <Navbar.Collapse id="basic-navbar-nav" className="">
                        <Nav className="ms-auto fw-bolder size-text-nav text-black">
                            <Nav.Link className="text-black px-3  hover-nav" onClick={() => handleBrandClick("/")}>Home</Nav.Link>
                            <Nav.Link className="text-black px-3  hover-nav" onClick={() => handleBrandClick("/aboutme")}>About me</Nav.Link>
                            <Nav.Link className="text-black px-3  hover-nav" onClick={() => handleBrandClick("/service")}>Services</Nav.Link>
                            <Nav.Link className="text-black px-3  hover-nav" onClick={() => handleBrandClick("/contact")}>Contact</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    )
}