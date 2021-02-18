import React, { useState, useEffect } from 'react';

function Destinations() {
  const [destinationList, setDestinationList] = useState();

  async function getDestinations() {
    const response = await fetch('http://localhost:5000/dbinfo');
    const json = await response.json();
    setDestinationList({ data: json });
  }

  useEffect(() => {
    getDestinations()
  }, []);

  return <p>wow</p>
}

export default Destinations;
