// AppWithAppBar.jsx
import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, IconButton, Box } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import LocationSelector from './LocationSelector';
import MapDisplay from './MapDisplay';

const AppWithAppBar = () => {
  const [selectedLocation, setSelectedLocation] = useState(null);

  const handleLocationSelect = (location) => {
    setSelectedLocation(location);
  };

  const handleBackButtonClick = () => {
    setSelectedLocation(null);
  };

  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <IconButton size="large" edge="start" color="inherit" aria-label="open drawer" sx={{ mr: 2 }}>
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}>
            観光地マップアプリ
          </Typography>
        </Toolbar>
      </AppBar>
      <Box sx={{ marginTop: 4, padding: 2 }}>
        {!selectedLocation ? (
          <LocationSelector onSelectLocation={handleLocationSelect} />
        ) : (
          <MapDisplay
            selectedLocation={selectedLocation}
            onBackButtonClick={handleBackButtonClick}
          />
        )}
      </Box>
    </div>
  );
};

export default AppWithAppBar;
