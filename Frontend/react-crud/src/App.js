import React from 'react'
import axios from 'axios'


function App() {
  
  const get_data = () => {
    axios.get("http://127.0.0.1:8000/api/products").then(
    res => {
      console.log(res)
    }
    );
};
  
  return <div className="App">
      Hello

      <button onClick={get_data}>Get Data</button>
    </div>
}

export default App;
