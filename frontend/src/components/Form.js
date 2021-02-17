import React, { useState } from 'react';

function Form() {
  const [formInfo, setFormInfo] = useState({
    cityName: '',
    notes: ''
  });

  function handleSubmit(event) {
    event.preventDefault();

    return fetch( 'http://localhost:5000/forminput', {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, 
      method: 'POST',
      body: JSON.stringify(formInfo)
    });
  }

  function handleChange(event) {
    setFormInfo(prevState => ({
      ...prevState,
      [event.target.name]: event.target.value
    }));
  }

  return (
    <form onSubmit={handleSubmit} method="post" action="http://localhost:5000/forminput">
      <label>City Name:
        <input
          type="text"
          name="cityName"
          value={formInfo.cityName}
          onChange={handleChange}
        />
      </label>
      <label>Notes:
        <textarea
          name="notes"
          value={formInfo.notes}
          onChange={handleChange}
        />
      </label>
      <input type="submit" value="Submit" />
    </form>
  )
}

export default Form;