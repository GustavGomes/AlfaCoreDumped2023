import Header from './components/Header/Header'
import "./app.css"
import Footer from './components/Footer/Footer'
// reaproveitamento de estrutura
import { Outlet } from "react-router-dom"
import { AuthProvider } from "./components/AuthContext"

export default function App() {
  return (
    <div >
      <AuthProvider>
        <Header />
        <div className='container-content'>
          <Outlet />
        </div>
        <Footer />
      </AuthProvider>
    </div>
  )
}