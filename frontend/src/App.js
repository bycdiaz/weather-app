import React, { useState } from 'react';
import './App.css';
import Form from './components/Form';

function App() {
  const [formState, setFormState] = useState();
  function getFormState(state) {
    return setFormState(state);
  }
  return (
    <div className="App">
      <Form getFormState={getFormState}/>
    </div>
  );
}

export default App;
