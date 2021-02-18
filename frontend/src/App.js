import React, { useState } from 'react';
import './App.css';

import Form from './components/Form';
import DestinationsList from "./components/DestinationsList";

function App() {
  const [formState, setFormState] = useState();

  return (
    <div className="App">
      <h1>Dream Destinations</h1>
      <Form />
      <DestinationsList />
    </div>
  );
}

export default App;
