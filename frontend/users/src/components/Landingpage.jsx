import React, { useContext, useState } from 'react'
import AuthContext from '../Context/AuthContext'
import { Link, useLocation } from 'react-router-dom'

function Landingpage(){
    let {logoutUser} = useContext(AuthContext)
    let {user} = useContext(AuthContext)
    return(
        <>
        
        <p className='text-purple-700 text-center mt-10 text-bold-400'> WELCOME TO HOME PAGE</p>
        <h1 className='text-center'>{user.username}</h1>
        <p className='text-center text-red-700'><a onClick={logoutUser}>Logout</a></p>
        </>
    )
}

export default Landingpage