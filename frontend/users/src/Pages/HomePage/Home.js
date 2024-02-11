import Landingpage from "../../components/Landingpage";
import { useEffect } from 'react'
import { useContext } from 'react'
import { useNavigate } from "react-router-dom";
import AuthContext from "../../Context/AuthContext";



function Home () {
    const {user} = useContext(AuthContext)
    const navigate = useNavigate()

    useEffect(()=>{
        if(user){
            navigate('/')
        }
    },[])
    return(
        <>
            <Landingpage/>
        </>
    )
}

export default Home