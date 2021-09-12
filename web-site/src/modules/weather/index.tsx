import { useEffect, useState } from 'react';
import { If } from 'react-if';
// @ts-ignore
import GlassCard from '@components/glass-card';
// @ts-ignore
import Service from '@service';
import dayJs from 'dayjs';
import './index.scss';
import weatherMap from './weather-map';

const Weather = () => {
  const [todayAir, setTodayAir] = useState<{
    [name: string]: string | number;
  }>({});
  const [todayWeather, setTodayWeather] = useState<{
    [name: string]: string | number;
  }>({});

  const [todayAlarm, setTodayAlarm] = useState<any[]>([]);

  const [icon, setIcon] = useState<any>({});

  const setWeatherIcon = (weather: string) => {
    if (!weather || !weatherMap[weather]) {
      setIcon(weatherMap.unknown);
      return;
    }
    setIcon(weatherMap[weather]);
  };

  useEffect(() => {
    Service.getWeather().then((res: any) => {
      const { data } = res;
      const { air, alarm, forecast_24h, observe, tips } = data;
      console.log(data);

      setTodayAir(air);
      setTodayWeather(observe);
      setWeatherIcon(observe.weather);
      setTodayAlarm(alarm);
    });
  }, []);

  return (
    <GlassCard className='weather-card'>
      <h3 className='title'>江苏省-苏州市</h3>
      <div className='today-container'>
        <div className='air-container'>
          空气质量: {todayAir.aqi_name} (pm2.5: {todayAir['pm2.5']})
        </div>
        <div className='today-weather'>
          <div className='temp-container'>
            <div className='temp'>{todayWeather.degree}°C</div>
            <div className='weather-icon-container'>
              <img src={icon?.default} alt={`${todayWeather.weather}`} />
            </div>
            <div className='weather-text'>{todayWeather.weather || ''} </div>
            <div className='weather-update-time'>
              {dayJs(todayWeather.update_time).format('HH:MM')}更新
            </div>
            <div></div>
          </div>
          <div className='humidity-wind-container'>
            <div>{`湿度：${todayWeather.humidity || ''}%`}</div>
            <div>{`风力：${todayWeather.wind_power || ''}`}</div>
          </div>
        </div>
        <If condition={!!todayAlarm}>
          {/* <div className='weather-alarms'>{todayAlarm[0]?.detail}</div> */}
        </If>
      </div>
    </GlassCard>
  );
};

export default Weather;
