import React, { useState } from 'react';
import { Router, Link, RouteComponentProps } from '@reach/router';

import { Counter, CRUD } from './components';
// import logo from './logo.svg';
// import './App.css';

const Home: React.FC<RouteComponentProps> = () => {
  return (
    <ul>
      <li>
        <Link to='/counter'>
          Counter
        </Link>
      </li>
      <li>
        <Link to='/crud'>
          CRUD
        </Link>
      </li>
    </ul>
  )
}

function App() {


  return (
    <Router>
      <Home path='/'/>
      <Counter path="/counter"/>
      <CRUD path='/crud'/>
    </Router>
  );
}

export default App;


// <div className="App">
//   <header className="App-header">
//     <img src={logo} className="App-logo" alt="logo" />
//     <p>
//       Edit <code>src/App.tsx</code> and save to reload.
//     </p>
//     <a
//       className="App-link"
//       href="https://reactjs.org"
//       target="_blank"
//       rel="noopener noreferrer"
//     >
//       Learn React
//     </a>
//   </header>
// </div>