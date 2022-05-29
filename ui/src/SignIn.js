import React,{useState} from 'react'
import { TextField,Button} from '@mui/material';
import './SignIn.css'
import { handleBreakpoints } from '@mui/system';
import axios from 'axios';

function SignIn() {
    const [signin,setSignin] = useState({})
    const handler=()=>{
      console.log(signin)
        var data = {
          "username": signin['username'],
          "password": signin["password"],
          
          
          }
          if(data['username']=="abhi"){
            alert('Successfully logged in')
            localStorage.setItem("token","LAIHUEBFDWE489W34PTG54P9475");
            document.location.reload()
          }
          // axios
          //   .post("http://10.10.16.115:8000/login/", data)
          //   .then(res => {
          //     if (res.data['token']){
          //       alert('Success fully logged in')
          //       localStorage.setItem("token",res.data['token']);
          //       document.location.reload()
          //     }else{
          //       alert('Password/username incorrect')
          //     }
          //   })
          //   .catch(err => alert('Password/username incorrect'));
        }

  return (
    <div>
        <div className='SignIn__body'>
            <p className='Register__p'>Signin</p>
            <br/>
           <TextField
          required
          id="outlined-required"
          label="Username"
          
          className='Register__input'
          onChange={(e)=>{setSignin({...signin,'username':e.target.value})}}
          />
           <br/>
           <TextField
          required
          id="outlined-required"
          type='text'
          label="Password"
          className='Register__input'
          onChange={(e)=>{setSignin({...signin,'password':e.target.value})}}

          />
          <br/>
            <Button variant="contained" onClick={()=>handler()}>Login</Button>

        </div> 
    </div>

  )
}

export default SignIn