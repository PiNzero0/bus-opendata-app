// MapMarkers.js

import React from 'react';
import { Marker } from '@react-google-maps/api';

const MapMarkers = ({ stops, setSelectedStop }) => {
  return (
    <>
      {stops.map((stop) => (
        <Marker
          key={stop.stop_id}
          position={{ lat: stop.stop_lat, lng: stop.stop_lon }}
          onClick={() => setSelectedStop(stop)}
        />
      ))}
    </>
  );
};

export default MapMarkers;
