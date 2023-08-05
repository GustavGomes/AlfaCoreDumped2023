import React, { useState } from "react";
import "./formOcorrencia.css";

function FormOcorrencia() {
    const [occurrence, setOccurrence] = useState({
        reporterName: "",
        costCenter: "",
        description: "",
        operationField: "",
        location: ""
    });
    const [occurrences, setOccurrences] = useState([]);

    const handleChange = (e) => {
        const name = e.target.name;
        const value = e.target.value;

        setOccurrence({ ...occurrence, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (
            occurrence.reporterName &&
            occurrence.costCenter &&
            occurrence.description &&
            occurrence.operationField &&
            occurrence.location
        ) {
            const newOccurrence = {
                ...occurrence,
                id: new Date().getTime().toString()
            };
            setOccurrences([...occurrences, newOccurrence]);
            setOccurrence({
                reporterName: "",
                costCenter: "",
                description: "",
                operationField: "",
                location: ""
            });
        }
    };

    return (
        <section className="form-container">
            <h1 className="text-center">Envie uma ocorrência</h1>
            <form className="form">
                <div className="form-control">
                    <label htmlFor="reporterName">Nome: </label>
                    <input
                        type="text"
                        name="reporterName"
                        value={occurrence.reporterName}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-control">
                    <label htmlFor="costCenter">Centro de Custo: </label>
                    <input
                        type="text"
                        name="costCenter"
                        value={occurrence.costCenter}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-control">
                    <label htmlFor="operationField">Área de Atuação: </label>
                    <input
                        type="text"
                        name="operationField"
                        value={occurrence.operationField}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-control">
                    <label htmlFor="description">Descrição : </label>
                    <input
                        type="text"
                        name="description"
                        value={occurrence.description}
                        onChange={handleChange}
                    />
                </div>
                <button className='btn' type="submit" onClick={handleSubmit}>
                    Enviar Ocorrência
                </button>
            </form>

            <div className="items">
                {occurrences.map((item) => {
                    const {
                        id,
                        reporterName,
                        costCenter,
                        description,
                        operationField,
                        location
                    } = item;
                    return (
                        <div className="item" key={id}>
                            <h4>{reporterName}</h4>
                            <p>Cost Center: {costCenter}</p>
                            <p>Description: {description}</p>
                            <p>Operation Field: {operationField}</p>
                            <p>Location: {location}</p>
                        </div>
                    );
                })}
            </div>
        </section>
    );
}

export default FormOcorrencia;
