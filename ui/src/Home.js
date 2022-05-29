import React,{useState} from 'react'
import './Home.css'
import Register from './Register'
import SignIn from './SignIn'


function Home() {
  const [current,setCurrent] = useState('')
  return (
    <div className='Home'>
       <div className='Home__header'>

                <p className='Home__home' onClick={()=>setCurrent('')}>Home</p>
                <p className='Home__signin' onClick={()=>setCurrent('sign')}>Sign in</p>
                <p className='Home__register' onClick={()=>setCurrent('reg')}>Register</p>
                
        </div>

        <div className='Home__teamname'>
        <img className='Home__logos' src={require('./image.png')} alt="Whats-App-Image-2022-05-28-at-8-27-04-PM" border="0"/>

          {
            current == "sign" ? (<SignIn/> ):current == "reg" ?(<Register/>):(
            <><img style={{'cursor':'pointer'}}onClick={()=>alert()} src='https://ebf.com/wp-content/uploads/2019/01/mobile-security.gif'/>
            <h1>ALOHOMORA</h1>
            <p>KEY TO EVERY LOCK</p></>)
          }
            
            
                
        </div>
        
    </div>
  )
}

export default Home