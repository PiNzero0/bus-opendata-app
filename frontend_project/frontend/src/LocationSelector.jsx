// LocationSelector.jsx
import React from 'react';
import Button from '@mui/material/Button';
import ActionAreaCard from './ActionAreaCard'; // ActionAreaCard コンポーネントをインポート
import akita from './img/poke-akita.png';
import kaduno from './img/poke-kaduno.png';
import oga from './img/poke-oga.png';
import semboku from './img/poke-senboku.png';
import yokote from './img/poke-yokote.png';
const LocationSelector = ({ onSelectLocation }) => {

  const locations = [
    { name: 'ポケふた秋田', img: akita , coords: { lat: 39.752642, lng: 140.061295 }},
    { name: 'ポケふた男鹿', img: oga, coords: { lat: 39.88201, lng: 139.84772 }},
    { name: 'ポケふた横手', img: yokote , coords: { lat: 39.293561, lng: 140.545941 }},
    { name: 'ポケふた仙北', img: semboku , coords: { lat: 39.699992, lng: 140.662631 }},
    { name: 'ポケふた鹿角', img: kaduno , coords: { lat: 40.181213, lng: 140.785474 } },
  ];

  return (
    <div>
      <h2>観光地を選択してください</h2>
      
      {/* ActionAreaCard コンポーネントの組み込み */}
      <ActionAreaCard locations={locations} onSelectLocation={onSelectLocation} />
    </div>
  );
};

export default LocationSelector;
