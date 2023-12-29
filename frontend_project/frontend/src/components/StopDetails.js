// src/components/StopDetails.js
import React from 'react';

const StopDetails = ({ stop }) => {
  return (
    <div>
      <h2>Stop Details</h2>
      {stop ? (
        <div>
          <p>Stop ID: {stop.stop_id}</p>
          <p>Stop Name: {stop.stop_name}</p>
          {/* 他に表示したい情報があればここに追加  routeから持ってくる*/}
        </div>
      ) : (
        <p>No stop selected</p>
      )}
    </div>
  );
};

export default StopDetails;
