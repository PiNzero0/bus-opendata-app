// mapBounds.js

import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const MapBounds = ({ stops }) => {
  const [mapBounds, setMapBounds] = useState(null);

  const handleMapLoad = (map) => {
    const bounds = map.getBounds();
    setMapBounds(bounds);
  };

  return (
    <div style={{ height: '500px', width: '100%' }}>
      <LoadScript
        googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}
      >
        <GoogleMap
          mapContainerStyle={{ width: '100%', height: '100%' }}
          center={{ lat: 39.43, lng: 140.06 }}
          zoom={13}
          onLoad={(map) => handleMapLoad(map)}
        >
          {stops
            .filter((stop) => {
              const lat = stop.stop_lat;
              const lng = stop.stop_lon;
              return mapBounds && mapBounds.contains({ lat, lng });
            })
            .map((stop) => (
              <Marker
                key={stop.stop_id}
                position={{ lat: stop.stop_lat, lng: stop.stop_lon }}
              />
            ))}
        </GoogleMap>
      </LoadScript>
    </div>
  );
};

export default MapBounds;
