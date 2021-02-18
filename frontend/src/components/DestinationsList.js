import React, { useState, useEffect } from 'react';

function Destinations() {
  const [destinations, setDestinations] = useState();

  async function getDestinations() {
    try {
      const response = await fetch('http://localhost:5000/dbinfo');
      const json = await response.json();
      setDestinations(json);
    } catch(error) {
      console.log(error);
    }
  }

  useEffect(() => {
    getDestinations()
  }, []);

  function DestinationList() {
    if (destinations) {
      return destinations.map(destination => {
        return (
          <li>
            <img
              src={`http://openweathermap.org/img/wn/${destination.icon}@2x.png`}
              alt="current weather icon"
            />
            <p>{destination.name}</p>
            <p>{destination.description}</p>
            <p>{`Feels Like: ${destination.feels_like}`}</p>
            <p>{destination.notes}</p>
          </li>
        )
      })
    }
  }

  return (
    <ul className="destinations">
      <DestinationList />
    </ul>
  )

}

export default Destinations;
