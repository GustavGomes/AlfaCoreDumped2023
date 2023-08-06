import React, { useState } from "react";
import "./formRecisao.css";

function FormRecisao() {
    // ---- Recisao ----
    const [recission, setRecission] = useState({
        username: "",
        creator_id: 0,
        target_id: 0,
        status: "",
        rank: 0,
        reason: "",
        description: "",
        creation_date: "",
        start_date: "",
        end_date: "",
        user_id: "",
    });
    // HANDLE FORM + CONEXAO API-------
    const handleChange = (e) => {
        const { name, value } = e.target;

        setRecission({ ...recission, [name]: value });
    };



    const handleSubmit = (event) => {
        event.preventDefault();

        // Cria um objeto JSON com os dados do formulário
        const formData = {};

        // Imprime o JSON no console para fins de teste
        console.log(formData);

        // setar dados: creator_id, target_id -------------
        recission.creator_id = localStorage.getItem("userCpf");
        recission.target_id = 0;
        recission.status = "pendente";
        recission.creation_date = new Date();
        recission.start_date = new Date();;
        recission.end_date = new Date();;
        recission.user_id = recission.creator_id;
        console.log(recission);
        // conexao a api
        fetch("http://192.168.5.184:5066/api/insertRescissionSolicitation", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(recission),
        })
            .then((response) => response.json())
            .then((data) => {
                // Manipula a resposta da API aqui 
                console.log(data);
                // Limpa os campos do formulário após o envio
                setRecission({});
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
                    <h1 className="text-center">Solicitação de Recisão</h1>
                </div>
            </div>



            <form className="form">
            <div className="row">
                    <div className="col-12">
                    <label htmlFor="">Nome de Usuario: </label>
                            <input
                                type="text"
                                name="username"
                                value={recission.username}
                                onChange={handleChange}
                                className="input--form"
                            />
                    </div>
                </div>
                <div className="row">
                    <div className="col-12">
                        <p className="form--text">Qual o motivo da rescisão?:</p>
                        <label>
                            <select name="reason" value={recission.reason} onChange={handleChange}>
                                <option value="" disabled>
                                    Escolha
                                </option>
                                <option value="reducao efetivo">Redução de Efetivo</option>
                                <option value="desempenho">Demissão por Desempenho</option>
                                <option value="justa causa">Demissão por Justa Causa</option>
                                <option value="pedido de demissao">Pedido de Demissão</option>
                                <option value="acordo lega">Acordo Legal</option>
                            </select>
                        </label>
                    </div>

                </div>

                <div className="row">
                    <div className="col-12">
                        <div className="form-control">
                            <label htmlFor="description">Descrição: </label>
                            <textarea
                                name="description"
                                value={recission.description}
                                onChange={handleChange}
                                className="input--form"
                            />
                        </div>
                    </div>
                </div>

                <div className="row">
                    <div className="col-12">
                        <p className="form--text">De 1 a 5, quanto você recomendaria esse profissional?:</p>
                        <label>
                            <select name="rank" value={recission.rank} onChange={handleChange}>
                                <option value="0" disabled>0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                            </select>
                        </label>
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

export default FormRecisao;
