import React from "react";
import {
    createContext,
    useEffect,
    useState,
} from "react"

export const AuthContext = createContext({})

export function AuthProvider({ children }) {
    function getStoredUserInfo() {
        const username = localStorage.getItem("username");
        const roleName = localStorage.getItem("roleName");
        return { username, roleName };
    }

    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const { username, roleName } = getStoredUserInfo();

    function logout() {
        // Remove os dados do usuário do localStorage
        localStorage.removeItem("username");
        localStorage.removeItem("roleName");
        // Atualiza o estado de isLoggedIn para indicar que o usuário não está mais logado
        location.reload()
        setIsLoggedIn(false);
    }

    useEffect(() => {
        document.body.style.paddingTop = `${document.querySelector('.navbar').offsetHeight}px`;
        // Verifica se o usuário está logado (se o username e roleName estão definidos)
        setIsLoggedIn(!!username && !!roleName);
    }, [username, roleName]);
    console.log("Loged: " + isLoggedIn)

    return (
        <AuthContext.Provider value = {{isLoggedIn, logout}}>
            {children}
        </AuthContext.Provider>
    );
}