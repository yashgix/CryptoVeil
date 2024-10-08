import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const encryptMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/encrypt`, { message });
    return response.data;
  } catch (error) {
    console.error('Encryption error:', error);
  }
};

export const decryptImage = async (image) => {
  try {
    const formData = new FormData();
    formData.append('image', image);
    const response = await axios.post(`${API_URL}/decrypt`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  } catch (error) {
    console.error('Decryption error:', error);
  }
};