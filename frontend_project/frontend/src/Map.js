//とりあえずこれだけで地図が表示されるやつ
import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker, InfoWindow } from '@react-google-maps/api';

const Map = () => {
  const [stops, setStops] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedStop, setSelectedStop] = useState(null);

  useEffect(() => {
    const fetchStops = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/stops/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();

        // Check if data is an array before setting state
        if (Array.isArray(data.stops)) {
          setStops(data.stops);
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
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  const defaultCenter = {
    lat: 39.38678,
    lng: 140.04908,
  };

  return (
    <div style={{ height: '500px', width: '100%' }}>
      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
        <GoogleMap mapContainerStyle={{ width: '100%', height: '100%' }} center={defaultCenter} zoom={15}>
          {stops.map((stop) => {
            // Ensure stop_lat and stop_lon are numbers
            const lat = parseFloat(stop.stop_lat);
            const lng = parseFloat(stop.stop_lon);

            return (
              <Marker
                position={{ lat, lng }}
                onClick={() => setSelectedStop(stop)}
              />
            );
          })}
          {selectedStop && (
            <InfoWindow
              position={{
                lat: parseFloat(selectedStop.stop_lat),
                lng: parseFloat(selectedStop.stop_lon),
              }}
              onCloseClick={() => setSelectedStop(null)}
            >
              <div>
                <h3>{selectedStop.stop_name}</h3>
                {/* 他の詳細情報もここに表示 */}
              </div>
            </InfoWindow>
          )}
        </GoogleMap>
      </LoadScript>
    </div>
  );
};

export default Map;

