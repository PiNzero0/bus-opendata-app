import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea, Grid } from '@mui/material';


const ActionAreaCard=({ locations, onSelectLocation }) => {

  const handleLocationSelect = (location) => {
    onSelectLocation(location);
  };


  return (
    <Grid container spacing={2}>
      {locations.map((location, index) => (
        <Grid item key={index} xs={12} sm={6} md={4} lg={3}>
          <Card sx={{ maxWidth: 345 }}>
            <CardActionArea onClick={() => handleLocationSelect(location)}>
              <CardMedia
                component="img"
                height="350"
                image={location.img}
                alt={`poke futa ${index + 1}`}
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {location.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Click me to select locationCard
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
};

export default ActionAreaCard;
