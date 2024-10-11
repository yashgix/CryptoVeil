import axios from 'axios';

const API_URL = 'http://localhost:8000';  // Ensure this matches your backend URL

export const encodeMessage = async (image, message, password) => {
  const formData = new FormData();
  formData.append('image', image);
  formData.append('message', message);
  formData.append('password', password);

  try {
    const response = await axios.post(`${API_URL}/encode`, formData, {
      responseType: 'arraybuffer',
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  } catch (error) {
    console.error('Encoding error:', error);
    throw error;
  }
};

export const decodeMessage = async (image, password) => {
  const formData = new FormData();
  formData.append('image', image);
  formData.append('password', password);

  try {
    const response = await axios.post(`${API_URL}/decode`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  } catch (error) {
    console.error('Decoding error:', error);
    throw error;
  }
};