import React, { useState } from "react";
import "./login.css";
import LoginImg from "../../images/loginImg.png";

export default function (props) {
    const [cpf, setCpf] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState(""); // Estado para armazenar mensagem de erro

    const handleSubmit = (event) => {
        event.preventDefault();

        // Cria um objeto JSON com os dados do formulário
        const formData = {
            cpf: cpf,
            password: password,
        };

        // Imprime o JSON no console para fins de teste
        console.log(formData);

        fetch("http://192.168.5.184:5066/api/login", {
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
                if (data.msg === "Invalid Credentials") {
                    // Se as credenciais forem inválidas, define a mensagem de erro
                    
                } else {
                    localStorage.setItem("username", data.Username);
                    localStorage.setItem("roleName", data.RoleName);
                    localStorage.setItem("roleName", data.RoleName);
                    localStorage.setItem('userCpf', data.Cpf);
                    window.location.reload();
                }
            })
            .catch(error => {
                // Lida com erros da solicitação aqui
                console.error('Erro:', error);
                // Define a mensagem de erro genérica para problemas de conexão com a API
                setErrorMessage("Ocorreu um erro ao se conectar à API. Por favor, tente novamente mais tarde.");
            });

        // Limpa os campos do formulário após o envio
        setCpf("");
        setPassword("");
    };

    return (
        <div className="Auth-form-container">
            <div className="image-container">
                <img src={LoginImg} alt="" className="login--img" />
            </div>
            <form className="Auth-form" onSubmit={handleSubmit}>
                <div className="Auth-form-content">
                    <h1 className="Auth-form-title">Entrar</h1>
                    {errorMessage && (
                        <div className="error-message">{errorMessage}</div>
                    )}
                    <div className="form-group mt-3">
                        <label>CPF</label>
                        <input
                            type="text"
                            className="form-control mt-1"
                            placeholder="Digite o cpf"
                            value={cpf}
                            onChange={(e) => setCpf(e.target.value)}
                        />
                    </div>
                    <div className="form-group mt-3">
                        <label>Senha</label>
                        <input
                            type="password"
                            className="form-control mt-1"
                            placeholder="Digite a senha"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <div className="d-grid gap-2 mt-3">
                        <button type="submit" className="btn btn-primary">
                            Enviar
                        </button>
                    </div>
                </div>
            </form>
        </div>
    );
}
