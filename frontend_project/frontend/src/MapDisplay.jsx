// MapDisplay.jsx

import React from 'react';
import Button from '@mui/material/Button';
import MapComponent from './MapComponent';

const MapDisplay = ({ selectedLocation, onBackButtonClick }) => {
  return (
    <div>
      <h2>{selectedLocation.name}のマップ</h2>
      <MapComponent 
      img={selectedLocation.img}
      lat={selectedLocation.coords.lat} 
      lng={selectedLocation.coords.lng} 
      />
      <Button variant="contained" onClick={onBackButtonClick}>
        戻る
      </Button>
    </div>
  );
};

export default MapDisplay;
