// Third Party
import { BrowserRouter, Routes, Route } from "react-router-dom";
// Local modules
import LandingPage from "../pages/LandingPage.jsx";
import CreateAccount from "../pages/CreateAccount.jsx";
import DashBoard from "../pages/DashBoard.jsx";

function AppRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/signUp" element={<CreateAccount />} />
                <Route path="/dashboard" element={<DashBoard />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRoutes;
