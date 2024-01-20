import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, MarkerF, Marker } from '@react-google-maps/api';
import DetailsComponent from './DetailsComponent';
import { Drawer, Card, CardContent, Typography } from '@mui/material';


const MapComponent = ({ smallimg, lat, lng }) => {
  const [stops, setStops] = useState([]);
  const [selectedStop, setSelectedStop] = useState(null);
  const [loading, setLoading] = useState(true);
  const [center, setCenter] = useState(null);
  const [mapCenter, setMapCenter] = useState(null);
  const [selectedRouteId, setSelectedRouteId] = useState(null);
  const [filteredStops, setFilteredStops] = useState([]);
  const [selectedStopName, setSelectedStopName] = useState(null);

  useEffect(() => {
    const fetchStops = async () => {
      try {
        const apiUrl = 'http://localhost:8000/api/stops/';
        const response = await fetch(apiUrl);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        if (Array.isArray(data.stops)) {
          setStops(data.stops);
        } else {
          console.error('Invalid data structure received from the API:', data);
        }

        // データが取得されたら、selectedStop が空でなければそれを保持
        if (selectedStop) {
          const updatedSelectedStop = data.stops.find(
            (stop) => stop.stop_id === selectedStop.stop_id
          );
          if (updatedSelectedStop) {
            setSelectedStop(updatedSelectedStop);
          } else {
            setSelectedStop(null);
          }
        }

        setMapCenter({
          lat: parseFloat(lat),
          lng: parseFloat(lng),
        })
      
      } catch (error) {
        console.error('Error fetching stops:', error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStops();
  }, [lat, lng]);


  const handleMarkerClick = (stop) => {
    setSelectedStop(stop);
    setSelectedStopName(stop.stop_name);
  };

  const handleCloseDrawer = () => {
    setSelectedStop(null);
  };


  const centerMapToCoordinates = (coords) => {
    setMapCenter({ lat: parseFloat(coords.lat), lng: parseFloat(coords.lng) });

  };


  const handleCardClick = async (routeId) => {
    try {
      const apiUrl = 'http://localhost:8000/api/get_stop_id/${routeId}';
      const response = await fetch(apiUrl);
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
  
      if (data && data.stops) {
        setFilteredStops(data.stops);
  
        // 非同期処理が終わった後にログを出力
        console.log('Filtered Stops:', data.stops);
  
        setSelectedStop(data.stops);
        setCenter({
          lat: parseFloat(data.stops.stop_lat),
          lng: parseFloat(data.stops.stop_lon),
        });
        setSelectedStopName(data.stops.stop_name);
      } else {
        console.error('Invalid data structure received from the API:', data);
      }
    } catch (error) {
      console.error('Error fetching stop info:', error.message);
    }
  };

  
  return (
    <>
      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
        <GoogleMap
          mapContainerStyle={{ width: '100%', height: 'calc(75vh)' }}
          center={mapCenter}
          zoom={15}
        >
          {(filteredStops.length > 0 ? filteredStops : stops).map((stop) => (
            <React.Fragment key={stop.stop_id}>
              <MarkerF
                position={{ lat: stop.stop_lat, lng: stop.stop_lon }}
                onClick={() => handleMarkerClick(stop)}
              />
              <MarkerF
                position={mapCenter}
                icon={{
                  url: smallimg,
                }}
              />
            </React.Fragment>
          ))}
        </GoogleMap>
      </LoadScript>
      <Drawer anchor="right" open={Boolean(selectedStop)} onClose={handleCloseDrawer}>
        <div style={{ width: 300 }}>
          <Card>
            <CardContent>
              {/* バス停の名前を表示 */}
              {selectedStop ? (
                <Typography variant="h6" component="div">
                  {selectedStopName}
                </Typography>
              ) : (
                <Typography variant="h6" component="div">
                  バス停を選択してください
                </Typography>
              )}
              {/* DetailsComponentを呼び出す */}
              {selectedStop && (
                <DetailsComponent
                  selectedStopId={selectedStop.stop_id}
                  onCardClick={handleCardClick}
                />
              )}
            </CardContent>
          </Card>
        </div>
      </Drawer>
    </>
  );
}  
export default MapComponent;