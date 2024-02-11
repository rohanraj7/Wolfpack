
import { BrowserRouter as Router,Route,Routes } from 'react-router-dom';

import { AuthProvider } from "./Context/AuthContext";
import Loginn from "./components/Login";
import Signup from "./components/Signup";
import PrivateRouter from "./utils/PrivateRouter";
import Home from './Pages/HomePage/Home';

function App() {
  return (
    <>
      <Router>
      <AuthProvider>
        <Routes>
          <Route element={<PrivateRouter />}>
            <Route path="/" element={<Home />} exact />
          </Route>
          <Route path='/login' element={<Loginn />} />
          <Route path='/signup' element={<Signup />} />
        </Routes>
      </AuthProvider>
    </Router>
    </>
  );
}

export default App;
