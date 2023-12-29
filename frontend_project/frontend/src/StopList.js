// StopList.js

import React, { useState, useEffect } from 'react';

const StopList = ({ onDataLoad }) => {
  const [stops, setStops] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStops = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/stops/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();

        if (Array.isArray(data)) {
          setStops(data);
          onDataLoad(data); // Pass the data to the parent component
        } else {
          console.error('Invalid data structure received from the API:', data);
        }
      } catch (error) {
        console.error('Error fetching stops:', error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStops();
  }, [onDataLoad]);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <ul>
      {stops.map((stop) => (
        <li key={stop.stop_id}>{stop.stop_name}</li>
      ))}
    </ul>
  );
};

export default StopList;

