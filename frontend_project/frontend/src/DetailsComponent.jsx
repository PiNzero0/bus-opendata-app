
// DetailsComponent.jsx
/*到着時刻バージョン
import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const DetailsComponent = ({ selectedStopId, onCardClick }) => {
  const [stopDetails, setStopDetails] = useState(null);

  useEffect(() => {
    const fetchStopDetails = async () => {
      try {
        const apiUrl = `http://localhost:8000/api/get_bus_info/${selectedStopId}`;
        const response = await fetch(apiUrl);
  
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        console.log(data);  // 追加
        setStopDetails(data);
      } catch (error) {
        console.error('Error fetching stop details:', error.message);
      }
    };
  
    if (selectedStopId) {
      fetchStopDetails();
    }
  }, [selectedStopId]);
  
  if (!stopDetails) {
    return <p>Loading details...</p>;
  }

  // route_idごとにarrival_timesをグループ化
  const groupedArrivalTimes = stopDetails.data.reduce((acc, arrival) => {
    if (!acc[arrival.route_id]) {
      acc[arrival.route_id] = [];
    }
    acc[arrival.route_id].push(arrival.arrival_time);
    return acc;
  }, {});
  

  return (
    <div>
      <Typography variant="h5" component="div">
        {stopDetails.stop_name}
      </Typography>
      {Object.entries(groupedArrivalTimes).map(([routeId, arrivalTimes]) => (
        <Card
          key={routeId}
          style={{ margin: '10px 0', cursor: 'pointer' }}
          onClick={() => onCardClick(routeId)}
        >
          <CardContent>
            <Typography variant="h6" component="div">
              {routeId}の到着時刻:
            </Typography>
            <ul>
              {arrivalTimes
                .sort((a, b) => new Date(`1970/01/01 ${a}`) - new Date(`1970/01/01 ${b}`))
                .map((arrivalTime) => (
                  <li key={arrivalTime}>{arrivalTime}</li>
                ))}
            </ul>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}  

export default DetailsComponent;
*/
// DetailsComponent.jsx

import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const DetailsComponent = ({ selectedStopId, onCardClick }) => {
  const [stopDetails, setStopDetails] = useState(null);

  useEffect(() => {
    const fetchStopDetails = async () => {
      try {
        const apiUrl = `http://localhost:8000/api/get_bus_info/${selectedStopId}`;
        const response = await fetch(apiUrl);
  
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
  
        const data = await response.json();
        console.log(data);  // 追加
        setStopDetails(data);
      } catch (error) {
        console.error('Error fetching stop details:', error.message);
      }
    };
  
    if (selectedStopId) {
      fetchStopDetails();
    }
  }, [selectedStopId]);
  
  if (!stopDetails) {
    return <p>Loading details...</p>;
  }

  // route_idごとにdeparture_timesをグループ化
  const groupedDepartureTimes = stopDetails.data.reduce((acc, departure) => {
    if (!acc[departure.route_id]) {
      acc[departure.route_id] = [];
    }
    acc[departure.route_id].push(departure.departure_time);
    return acc;
  }, {});
  

  return (
    <div>
      <Typography variant="h5" component="div">
        {stopDetails.stop_name}
      </Typography>
      {Object.entries(groupedDepartureTimes).map(([routeId, departureTimes]) => (
        <Card
          key={routeId}
          style={{ margin: '10px 0', cursor: 'pointer' }}
          onClick={() => onCardClick(routeId)}
        >
          <CardContent>
            <Typography variant="h6" component="div">
              {routeId}の出発時刻:
            </Typography>
            <ul>
              {departureTimes
                .sort((a, b) => new Date(`1970/01/01 ${a}`) - new Date(`1970/01/01 ${b}`))
                .map((departureTime) => (
                  <li key={departureTime}>{departureTime}</li>
                ))}
            </ul>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}  

export default DetailsComponent;
