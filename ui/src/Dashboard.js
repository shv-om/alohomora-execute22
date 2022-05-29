import React, { useState,useEffect } from 'react'
import './Dashboard.css'
import PersonIcon from '@mui/icons-material/Person';
import DashboardIcon from '@mui/icons-material/Dashboard';
import SettingsIcon from '@mui/icons-material/Settings';
import LogoutIcon from '@mui/icons-material/Logout';
import DashRight from './DashRight';
import UserProfile from './UserProfile';
import { TextField,Button} from '@mui/material';


function Dashboard() {
    const [toggle,setToggle] = useState(true)
    const [togglepro,setTogglepro] = useState(false)
    const [toggledash,setToggledash] = useState(false)
    const [tempkeyword,setTempKeyword] = useState('')
    const [keyword,setKeyword] = useState('')
    
    

  return (
      
    <div className='Dashboard'>
        {
            keyword ? (<><div className='Dashboard_left' id="nop">
            
            <img onClick={()=>{
                if(toggle){
                    document.getElementById('nop').style.flex=0.02
                }else{
                    document.getElementById('nop').style.flex=0.1
                }
                setToggle(!toggle)
            }} src="https://img.icons8.com/material-outlined/24/000000/menu--v1.png"/>

           
            <div style={{'color':!togglepro && 'black'}} onClick={()=>{setTogglepro(!togglepro)}} className='Dashboard__order Dashboard_leftmenu'>
                <DashboardIcon/>
                <p className='Dashboard__menutext'>Dashboard</p>
            </div>
            <div style={{'color':togglepro && 'black'}} onClick={()=>{setTogglepro(!togglepro)}} className='Dashboard__order Dashboard_leftmenu'>
                <PersonIcon />
                <p className='Dashboard__menutext'>Userprofile</p>
            </div>
            

            
            <div className='Dashboard_bottom'>
                <div className='Dashboard__order Dashboard_leftmenu'>
                    <SettingsIcon />
                    <p className='Dashboard__menutext' >Settings</p>
                </div>
                <div className='Dashboard__order Dashboard_leftmenu' onClick={()=>{
                        localStorage.setItem("token","NILL")
                        document.location.reload()
                    }
                        }>
                    <LogoutIcon />
                    <p className='Dashboard__menutext' >Logout</p>
                </div>
            </div>
        </div>
        <div className='Dashboard_right'>
            {
                togglepro ? <UserProfile/> : <DashRight/>
            }
        

            


                
        </div>
        </>
):(<>   
<div className='Dashboard__keyword'>
        <TextField
          required
          id="outlined-required"
          label="Enter the keyword"
          
          className='Register__input'
          onChange={(e)=>setTempKeyword(e.target.value)}
          />
          <br/>
          <Button variant="contained" style={{'width':'550px'}} onClick={()=>setKeyword(tempkeyword)}>Submit</Button>
    </div>
       {/* <DashRight/> */}
        
</>)
        
}
    </div>
  )
}

export default Dashboard