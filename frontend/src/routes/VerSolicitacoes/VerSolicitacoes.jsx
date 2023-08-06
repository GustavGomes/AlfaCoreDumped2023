import React from "react";
import Solicitacoes from "../../components/VisualizacaoSolicitacoes/VisualizacaoSolicitacoes"
export default function VerSolicitacoes() {
    return(
        <>
        <h1 className="text-center">Solicitações Cadastradas</h1>
        <Solicitacoes />
        </>
        
    );
}