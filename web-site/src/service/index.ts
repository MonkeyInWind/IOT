import HTTP from './http';

const { get } = HTTP;

class Service {
  getWeather = async () => {
    const res: any = await get({
      url: '/api/weather/common',
      data: {
        source: 'pc',
        province: '江苏',
        city: '苏州',
        weather_type: 'observe|forecast_24h|alarm|tips|air',
      },
    });
    return res.data;
  };
}

export default new Service();
