import React, { useState, useEffect } from "react";
import Accordion from "react-bootstrap/Accordion";
import "../Usuario/usuario.css"

export default function VisualizacaoOcorrencia() {
    const [occurrences, setOcurrences] = useState([]);

    useEffect(() => {
        fetch("http://192.168.5.184:5066/api/getReports")
            .then((response) => response.json())
            .then((data) => {
                setOcurrences(data);
                console.log(data)
            })
            .catch((error) => {
                console.error("Erro ao obter as ocorrencias:", error);
            });
    }, []);

    return (
        
        <Accordion >
            {occurrences.map((ocurrence, index) => (
                <Accordion.Item className="accordion-item" key={index} eventKey={index.toString()}>
                    <Accordion.Header 
                    className="cost_center header-acc">Relatório {ocurrence.Id}
                    </Accordion.Header>
                    <Accordion.Body>
                        <p>Nome de quem reportou: {ocurrence.ReporterName} </p>
                        <p>Centro de Custo: {ocurrence.CostCenter} </p>
                        <p>Descrição:{ocurrence.Description} </p>
                        <p>Área de Operação: {ocurrence.Operation_Field}</p>
                        <p>Localização: {ocurrence.Location} </p>
                    </Accordion.Body>
                </Accordion.Item>
            ))}
        </Accordion>
    );
}
