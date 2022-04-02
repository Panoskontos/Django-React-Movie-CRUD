import React from 'react'
import './App.css';

// import bootsrap
import 'bootstrap/dist/css/bootstrap.min.css';


class App extends React.Component {
    

  render(){

    return(
      <div className='container'>


      <div id="product-container">
        {/* 2 sub containers for form and list */}
        <div id="form-wrapper">
          <form action="">
            <div>
              <input type="text" name="product" id="product-input" placeholder="Add a product"/>
            </div>
            <div>
              <button type="submit">Add</button>
            </div>
          </form>
        </div>

        <div id="list-wrapper">

        </div>

      </div>

      </div>
    )
  }
}
  


export default App;
