// App.js
import React, { useState } from 'react';
import Map from './Map';
//import StopDetails from './components/StopDetails';

const App = () => {
  const [selectedStop, setSelectedStop] = useState(null);

  const handleStopClick = (stop) => {
    setSelectedStop(stop);
  };

  return (
    <div>
      <Map selectedStop={selectedStop} onMarkerClick={handleStopClick} />
    </div>
  );
};

export default App;

