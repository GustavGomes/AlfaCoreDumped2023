import React, { useState } from "react";
import "./formFerias.css";

function FormFerias() {
    // ---- Ferias ----
    const [vacation, setVacation] = useState({
        id: "",
        username: "",
        creator_id: 0,
        target_id: 0,
        status: "",
        vacation_start: Date,
        vacation_end: Date,
        description: "",
        creation_date: "",
        start_date: "",
        user_id: "",
    });
    // HANDLE FORM + CONEXAO API-------
    const handleChange = (e) => {
        const name = e.target.name;
        const value = e.target.value;

        setVacation({ ...vacation, [name]: value });
    };



    const handleSubmit = (event) => {
        event.preventDefault();

        // Cria um objeto JSON com os dados do formulário
        const formData = {

        };

        // Imprime o JSON no console para fins de teste
        console.log(formData);

        // setar dados: creator_id, target_id -------------

        // conexao a api
        fetch("", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        })
            .then((response) => response.json())
            .then((data) => {
                // Manipula a resposta da API aqui 
                console.log(data);
                // Limpa os campos do formulário após o envio
                setVacation({});
            })
            .catch(error => {
                // Lida com erros da solicitação aqui
                console.error('Erro:', error);
                // Define a mensagem de erro genérica para problemas de conexão com a API
                setErrorMessage("Ocorreu um erro ao se conectar à API. Por favor, tente novamente mais tarde.");
            });

    };


    return (
        <div className="form-container">
            <div className="row">
                <div className="col-12">
                    <h1 className="text-center">Solicitação de Férias</h1>
                </div>
            </div>

            <form className="form">
                <div className="row">
                    <div className="col-12">
                        <div className="form-control">
                            <label htmlFor="">Nome de Usuario: </label>
                            <input
                                type="text"
                                name="username"
                                value={vacation.username}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                </div>

                <div className="row">
                    <div className="col-md-6">
                        <div className="form-control">
                            <label>Inicio das Férias: </label>
                            <input
                                type="date"
                                name="start_date"
                                value={vacation.start_date}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="form-control">
                            <label>Fim das Ferias: </label>
                            <input
                                type="date"
                                name="end_date"
                                value={vacation.end_date}
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
                            value={vacation.description}
                            onChange={handleChange}
                            className="input--form"
                        />
                    </div>
                </div>

                <div className="text-center">
                    <button className='btn' type="submit" onClick={handleSubmit} >
                        Enviar Solicitação
                    </button>
                </div>
            </form>
        </div>
    );
}

export default FormFerias;
