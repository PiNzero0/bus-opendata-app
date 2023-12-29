// src/components/MapComponent.js
import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const MapComponent = ({ stops }) => {
  const [selectedStop, setSelectedStop] = useState(null);

  const mapStyles = {
    height: '400px',
    width: '100%',
  };

  const defaultCenter = {
    lat: 37.7749,
    lng: -122.4194,
  };

  const onSelect = (stop) => {
    setSelectedStop(stop);
  };

  return (
    <LoadScript googleMapsApiKey= {process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
      <GoogleMap mapContainerStyle={mapStyles} zoom={13} center={defaultCenter}>
        {stops.map((stop) => (
          <Marker
            key={stop.stop_id}
            position={{ lat: stop.lat, lng: stop.lng }}
            onClick={() => onSelect(stop)}
          />
        ))}
      </GoogleMap>
    </LoadScript>
  );
};

export default MapComponent;
