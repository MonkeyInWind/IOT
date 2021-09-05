import axios from 'axios';
import { IParams } from './types';

class HTTP {
  get = async (params: IParams) => {
    const { url, data = null } = params;
    let urlParams = '';
    if (data !== null) {
      const keys = Object.keys(data);
      if (keys.length) {
        keys.forEach((key, index) => {
          if (index === 0) urlParams = '?';
          urlParams += `${key}=${data[key]}`;
          if (index < keys.length - 1) urlParams += '&';
        });
      }
    }
    return axios
      .get(`${url}${urlParams}`)
      .then((res) => {
        return res;
      })
      .catch((err) => {
        console.error(err);
      });
  };
}

export default new HTTP();
