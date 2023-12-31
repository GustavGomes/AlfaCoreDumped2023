import React, { useEffect, useState, useContext } from "react";
import Container from 'react-bootstrap/Container';
import { Nav, Dropdown } from 'react-bootstrap';
import Navbar from 'react-bootstrap/Navbar';
import "./header.css"
import logo from "../../images/logoWhite.png"
import { Link } from "react-router-dom"
import { AuthContext } from "../AuthContext"

export default function Header() {

    const { isLoggedIn, logout } = useContext(AuthContext)

    return (
        <Navbar expand="lg" className="navbar fixed-top navbar-expand-lg navbar-light bg-light" >
            <Container>
                <Navbar.Brand><img src={logo} className="logoAlfa"></img></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    {isLoggedIn ? (
                        <Nav className="ms-auto">
                            <Dropdown>
                                <Dropdown.Toggle as={Nav.Link} className="nav--link">
                                    VISUALIZAR
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    <Dropdown.Item as={Link} to="/verOcorrencias">Ocorrências</Dropdown.Item>
                                    <Dropdown.Item as={Link} to="/verUsuariosCadastrados">Candidatos</Dropdown.Item>
                                    <Dropdown.Item as={Link} to="/verSolicitacoes">Solicitações</Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                            <Dropdown>
                                <Dropdown.Toggle as={Nav.Link} className="nav--link">
                                    REALIZAR SOLICITAÇÃO
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    <Dropdown.Item as={Link} to="/cadastroFerias">Férias</Dropdown.Item>
                                    <Dropdown.Item as={Link} to="/cadastroRescisao">Recisão</Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                            <Nav.Link as={Link} to="/cadastroAreaEquip" className="nav--link">CADASTRO DE ÁREA/EQUIPAMENTO</Nav.Link>
                            <Nav.Link as={Link} to="/login" className="nav--link btn--sair" onClick={logout}>SAIR</Nav.Link>
                        </Nav>
                    ) : (
                        <Nav className="ms-auto">
                            <Nav.Link as={Link} to="/candidatos" className="nav--link">TRABALHE CONOSCO</Nav.Link>
                            <Nav.Link as={Link} to="/ocorrencias" className="nav--link">FAÇA UMA OCORRÊNCIA</Nav.Link>
                            <Nav.Link as={Link} to="/login" className="nav--link">LOGIN</Nav.Link>
                        </Nav>
                    )}
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}