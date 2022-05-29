import React,{useState} from 'react'
import './UserProfile.css'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
function UserProfile() {
    const [trigger,setTrigger] = useState(false)
  return (
        <div className='UserProfile'>
            <p className='Register__p'>User Profile</p>
                <div className='UserProfile__body'>
                    <div className='UserProfile__head'>
                        <AccountCircleIcon style={{'fontSize':'50px','paddingRight':'5px'}}/>
                        <p>ABHIJITH B</p>
                    </div>
                    
                    <table className='UserProfile__table'>
                        <tr>
                            <td className='UserProfile__tabletd'>Name   :</td>
                            <td>ABHIJITH B</td>
                            
                        </tr>
                        <tr>
                            <td className='UserProfile__tabletd'>Email   :</td>
                            <td>abhijithb@gmail.com</td>
                        </tr>
                        <tr>
                            <td className='UserProfile__tabletd'>Date of birth :</td>
                            <td>13/08/1989</td>
                        </tr>
                        <tr>
                            <td className='UserProfile__tabletd'>Company Name   :</td>
                            <td>XYZ Company</td>
                        </tr>
                        
                    </table>
                </div>
        </div>
    
  )
}

export default UserProfile