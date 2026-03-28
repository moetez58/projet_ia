import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const fetchData = async () => {
  const response = await axios.get(`${API_URL}/data`);
  return response.data;
};

export const fetchStats = async () => {
  const response = await axios.get(`${API_URL}/stats`);
  return response.data;
};