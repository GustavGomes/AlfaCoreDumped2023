import React from "react";
import FormFerias from "../../components/FormFerias/FormFerias"
import FormRecisao from "../../components/FormRecisao/FormRecisao"
import Accordion from 'react-bootstrap/Accordion';

export default function () {
    return (
        <div>
            <h1 className="text-center">Realizar uma Solicitação</h1>
            <Accordion defaultActiveKey="0">
                <Accordion.Item eventKey="0">
                    <Accordion.Header>Solicitação de Férias</Accordion.Header>
                    <Accordion.Body>
                        <FormFerias />
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="1">
                    <Accordion.Header>Solicitação de Recisão</Accordion.Header>
                    <Accordion.Body>
                        <FormRecisao />
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
        </div>
    );
}