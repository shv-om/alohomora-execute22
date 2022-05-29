import logo from './logo.svg';
import Home from './Home' 
import SignIn from './SignIn'
import Register from './Register';
import Dashboard from './Dashboard';
import UserProfile from './UserProfile';

function App() {
  return (
    <div className="App">
      {
        localStorage.getItem("token")==="NILL" ? <Home/>:<Dashboard/>
      }
     
      
    </div>
  );
}

export default App;
