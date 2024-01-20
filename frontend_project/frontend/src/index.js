// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import AppWithAppBar from './AppWithAppBar';

const root = document.getElementById('root');
const app = (
  <React.StrictMode>
    <AppWithAppBar />
  </React.StrictMode>
);

ReactDOM.createRoot(root).render(app);
