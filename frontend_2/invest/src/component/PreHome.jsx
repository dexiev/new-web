import React from 'react'
import Login from './Login'
import { useState } from 'react'
import Register from './Register'

const PreHome = () => {
    const [login, setLogIn]= useState(false)
    const handlelogin=()=>{
        setLogIn(!login)
    }

  return (
    <div>

     {
     
        login ? 
        <>
            <Register />
            <h3>Already registered ?</h3>

        </>
    
        : <Login />
        
    }

      

      <button onClick={handlelogin}>Clcick here to log in</button>
    </div>
  )
}

export default PreHome
