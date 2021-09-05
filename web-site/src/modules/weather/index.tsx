import { useEffect, useState } from 'react';
import GlassCard from '../../components/glass-card';
import Service from '../../service';

const Weather = () => {
  useEffect(() => {
    Service.getWeather().then((data) => {
      console.log(data);
    });
  }, []);
  return <GlassCard className='weather-card'></GlassCard>;
};

export default Weather;
