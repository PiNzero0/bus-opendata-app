// src/index.js
import React from 'react';
import { createRoot } from 'react-dom/client';
import Map from './Map';

const root = createRoot(document.getElementById('root'));

root.render(<Map />);