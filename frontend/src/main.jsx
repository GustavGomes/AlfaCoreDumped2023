import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider, useRoutes, Navigate } from 'react-router-dom';

// CONFIGURANDO ROUTER
import Home from "./routes/Home/Home";
import CadastroOcorrencias from "./routes/CadastroOcorrencia/CadastroOcorrencia";
import CadastroCandidatos from "./routes/CadastroCandidatos/CadastroCandidatos.jsx";
import Login from "./routes/Login/Login";
import CadastroSolicitacao from './routes/CadastroSolicitacao/CadastroSolicitacao';
import CadastroAreaEquip from './routes/CadastroAreaEquip/CadastroAreaEquip';
import VerUsuariosCadastrados from './routes/VerUsuariosCadastrados/VerUsuariosCadastrados';
import VerRelatorios from './routes/VerRelatorios/VerRelatorios';
import App from './App';

//VERIFICAR SE LOGADO --> PERMISSOES
function isAuthenticated() {
  const username = localStorage.getItem("username");
  const roleName = localStorage.getItem("roleName");
  return !!username && !!roleName;
}



const routes = [
  {
    path: "/", 
    element: <App />,
    children: [
      {
        path: "/", 
        element: <Home />
      },
      {
        path: "/ocorrencias", 
        element: <CadastroOcorrencias />
      },
      {
        path: "/candidatos", 
        element: <CadastroCandidatos />
      },
      {
        path: "/login", 
        element: isAuthenticated() ? <Navigate to="/" /> : <Login /> 
      },
      {
        path: "/cadastroSolicitacao",
        element: isAuthenticated() ? <CadastroSolicitacao /> : <Navigate to="/login" />
      },
      {
        path: "/cadastroAreaEquip",
        element: isAuthenticated() ? <CadastroAreaEquip /> : <Navigate to="/login" />
      },
      {
        path: "/relatorios",
        element: isAuthenticated() ? <VerRelatorios /> : <Navigate to="/login" />
      },
      {
        path: "/usuariosCadastrados",
        element: isAuthenticated() ? <VerUsuariosCadastrados /> : <Navigate to="/login" />
      }
    ]
  },
];

const router = createBrowserRouter(routes);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);