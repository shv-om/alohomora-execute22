import React,{useState} from 'react'
import { TextField,Button } from '@mui/material';
import './Register.css'
import axios from 'axios';


function Register() {
  const [details,setDetails] = useState({})
  const handler=()=>{
    const data={
      'username':details["name"],
      "email": details["email"],
      "password": details['password'],
      "authenticate_info": {
          "dob": details['date'],
          "image": null
      }
    }
  
  
  
      axios
        .post("http://10.10.16.115:8000/register/", data)
        .then(res => {
          console.log(res)
          if (res.data['token']){
            alert('Success fully logged in')
            localStorage.setItem("token",res.data['token']);
            document.location.reload()
          }else{
            alert('Password/username incorrect')
          }
        })
        .catch(err => alert('Password/username incorrect'));
    }
	
  return (
    <div className='Register'>

        <div className='Register__body'>
            <p className='Register__p'>Register</p>
          <TextField
          required
          id="outlined-required"
          label="Username"
          className='Register__input'
          onChange={(e)=>{setDetails({...details,'name':e.target.value})}}
          />
          <br/>
           <TextField
          required
          id="outlined-required"
          label="Email"
          type="email"
          className='Register__input'
          onChange={(e)=>{setDetails({...details,'email':e.target.value})}}
          />
          <br/>
          <h4 className='dob'>Date of birth</h4>
           <TextField
          required
          id="outlined-required"
          type='date'
          className='Register__input'
          onChange={(e)=>{setDetails({...details,'date':e.target.value})}}
          />
          <br/>
           <TextField
          required
          id="outlined-required"
          type='password'
          label="New Password"
          className='Register__input'
          onChange={(e)=>{setDetails({...details,'password':e.target.value})}}

          />
          <br/>
           <TextField
          required
          id="outlined-required"
          type='password'
          label="Confirm Password"
          className='Register__input'
          onChange={(e)=>{setDetails({...details,'cpassword':e.target.value})}}
          />
         <br/>
         <h4 className='dob'>Upload file</h4>
         <TextField
          required
          id="outlined-required"
          type='file'
          className='Register__input'
          onChange={(e)=>{
            if (e.target.files && e.target.files[0]) {
              let img = e.target.files[0];
            setDetails({...details,'image':URL.createObjectURL(img)})
          }}
        }
          />
          <br/>
          <Button variant="contained" onClick={()=>handler()}>Register</Button>
        </div>

        
    </div>
  )
}

export default Register