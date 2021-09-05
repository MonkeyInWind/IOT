import HTTP from './http';

const { get } = HTTP;

class Service {
  getWeather = () => {
    return get({
      url: '/api/weather/city/101190401',
    });
  };
}

export default new Service();
