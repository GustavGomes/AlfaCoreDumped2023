import React, { useState } from "react";
import "./formOcorrencia.css";

function FormOcorrencia() {
    const [occurrence, setOccurrence] = useState({
        reporter_name: "",
        cost_center: "",
        description: "",
        operation_field: "",
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
            occurrence.reporter_name &&
            occurrence.cost_center &&
            occurrence.description &&
            occurrence.operation_field &&
            occurrence.location
        ) {
            const newOccurrence = {
                ...occurrence,
                id: new Date().getTime().toString()
            };
            setOccurrences([...occurrences, newOccurrence]);
            setOccurrence({
                reporter_name: "",
                cost_center: "",
                description: "",
                operation_field: "",
                location: ""
            });
        }
    };

    return (
        <div className="form-container">
            <div className="row">
                <div className="col-12">
                    <h1 className="text-center">Envie uma ocorrência</h1>
                </div>
            </div>

            <form className="form">
                <div className="row">
                    <div className="col-12">
                        <div className="form-control">
                            <label htmlFor="reporter_name">Nome: </label>
                            <input
                                type="text"
                                name="reporter_name"
                                value={occurrence.reporter_name}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-6">
                        <div className="form-control">
                            <label htmlFor="operation_field">Área de Atuação: </label>
                            <input
                                type="text"
                                name="operation_field"
                                value={occurrence.operation_field}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="form-control">
                            <label htmlFor="cost_center">Centro de Custo: </label>
                            <input
                                type="text"
                                name="cost_center"
                                value={occurrence.cost_center}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                </div>
                <div className="col-12">
                    <div className="form-control">
                        <label htmlFor="description">Descrição : </label>
                        <textarea
                            name="description"
                            value={occurrence.description}
                            onChange={handleChange}
                            className="input--form"
                        />
                    </div>
                </div>
                <div className="text-center">
                    <button className='btn' type="submit" onClick={handleSubmit}>
                        Enviar Ocorrência
                    </button>
                </div>
            </form>

            <div className="items">
                {occurrences.map((item) => {
                    const {
                        id,
                        reporter_name,
                        cost_center,
                        description,
                        operation_field,
                        location
                    } = item;
                    return (
                        <div className="item" key={id}>
                            <h4>{reporter_name}</h4>
                            <p>Cost Center: {cost_center}</p>
                            <p>Description: {description}</p>
                            <p>Operation Field: {operation_field}</p>
                            <p>Location: {location}</p>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}

export default FormOcorrencia;
