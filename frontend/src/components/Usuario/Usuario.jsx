import React, { useState, useEffect } from "react";
import Accordion from "react-bootstrap/Accordion";
import "./usuario.css"

export default function Usuario() {
    const [candidates, setCandidates] = useState([]);

    useEffect(() => {
        fetch("http://192.168.5.184:5066/api/getCandidates")
            .then((response) => response.json())
            .then((data) => {
                setCandidates(data);
                console.log(data)
            })
            .catch((error) => {
                console.error("Erro ao obter os candidatos:", error);
            });
    }, []);

    return (
        <Accordion >
            {candidates.map((candidate, index) => (
                <Accordion.Item className="accordion-item" key={index} eventKey={index.toString()}>
                    <Accordion.Header 
                    className="nome-candidato">{candidate.CandidateName}
                    </Accordion.Header>
                    <Accordion.Body>
                        <p>CPF: {candidate.Cpf} </p>
                        <p>Data de Nascimento:{candidate.BirthDate} </p>
                        <p>Gênero: {candidate.Gender}</p>
                        <p>CEP: {candidate.Cep}</p>
                        <p>Email: {candidate.Email} </p>
                        <p className="ultimo">Telefone: {candidate.TelephoneNumber} </p>
                        <div className="d-flex justify-content-end">
                            <button className="btn accordion">aprovar</button>
                        </div>
                    </Accordion.Body>
                </Accordion.Item>
            ))}
        </Accordion>
    );
}
