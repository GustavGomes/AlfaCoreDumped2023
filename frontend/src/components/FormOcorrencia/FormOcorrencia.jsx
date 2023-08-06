import React, { useState } from "react";
import "./formOcorrencia.css";

function FormOcorrencia() {
    // ---- OCORRENCIA ----
    const [occurrence, setOccurrence] = useState({
        id: "", 
        reporter_name: "",
        cost_center: "",
        description: "",
        operation_field: "",
        location: "",
        created_at: ""
    });
    const [occurrences, setOccurrences] = useState([]);
    
    // ------------ HANDLE FORM ----------------
    const handleChange = (e) => {
        const name = e.target.name;
        const value = e.target.value;

        setOccurrence({ ...occurrence, [name]: value });
    };

    const handleImageChange = (e) => {
        const imageFile = e.target.files[0];
        setOccurrence({ ...occurrence, image: imageFile });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (
            occurrence.reporter_name &&
            occurrence.cost_center &&
            occurrence.description &&
            occurrence.operation_field
        ) {
            // Cria uma cópia da ocorrência atual para enviar para a API
            const occurrenceToSend = { ...occurrence };
            console.log(JSON.stringify(occurrenceToSend))

            // Se a geolocalização estiver disponível, adiciona-a à ocorrência
            getLocation()
                .then((location) => {
                    occurrenceToSend.location = `${location.latitude}, ${location.longitude}`;
                })
                .catch((error) => {
                    console.error("Erro ao obter a geolocalização:", error);
                })
                .finally(() => {
                    // Envia a ocorrência (com ou sem a localização) para a API
                    fetch("http://192.168.5.184:5066/api/insertReport", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(occurrenceToSend),
                    })
                        .then((response) => response.json())
                        .then((data) => {
                            console.log("Resposta do servidor:", data);
                            
                        })
                        .catch((error) => {
                            console.error("Erro ao enviar os dados:", error);
                        });

                    // Adiciona a ocorrência enviada à lista de ocorrências
                    setOccurrences([...occurrences, occurrenceToSend]);
                    // Reseta o formulário
                    setOccurrence({
                        reporter_name: "",
                        cost_center: "",
                        description: "",
                        operation_field: "",
                        location: "",
                    });
                });
        }
    };

    // ------------ OBTER GEOLOCALIZACAO  ----------------
    const getLocation = () => {
        return new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        const latitude = position.coords.latitude;
                        const longitude = position.coords.longitude;
                        resolve({ latitude, longitude });
                    },
                    (error) => {
                        reject(error);
                    }
                );
            } else {
                reject(new Error("Geolocation is not supported by this browser."));
            }
        });
    };


    return (
        <div className="form-container">
            <div className="row">
                <div className="col-12">
                    <h1 className="text-center">Envie uma Ocorrência</h1>
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
                                required
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
                                required
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
                                required
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
                            required
                        />
                    </div>
                </div>
                <div className="form-control">
                    <label htmlFor="image">Imagem: </label>
                    <input
                        type="file"
                        name="image"
                        onChange={handleImageChange}
                        className="input--form"
                    />
                </div>

                <div className="text-center">
                    <button className='btn' type="submit" onClick={handleSubmit} >
                        Enviar Relato
                    </button>
                </div>
            </form>
        </div>
    );
}

export default FormOcorrencia;
