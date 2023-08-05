import React from "react";
import  Usuario from "../../components/Usuario/Usuario"
export default function VerUsuariosCadastrados() {
    return(
        <div>
            <h1 className="text-center">Usuários Cadastrados</h1>
            <Usuario />
        </div>
    );
}