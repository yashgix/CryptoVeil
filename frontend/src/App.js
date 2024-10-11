import React, { useState } from 'react';
import './App.css';
import { encodeMessage, decodeMessage } from './api';

function App() {
  const [encodeImage, setEncodeImage] = useState(null);
  const [decodeImage, setDecodeImage] = useState(null);
  const [message, setMessage] = useState('');
  const [encodePassword, setEncodePassword] = useState('');
  const [decodePassword, setDecodePassword] = useState('');
  const [result, setResult] = useState('');
  const [encodedImage, setEncodedImage] = useState(null);

  const handleEncode = async (e) => {
    e.preventDefault();
    try {
      const response = await encodeMessage(encodeImage, message, encodePassword);
      const blob = new Blob([response], { type: 'image/png' });
      const url = window.URL.createObjectURL(blob);
      setEncodedImage(url);
      setResult('Message encoded successfully. Right-click the image and select "Save image as" to download.');
    } catch (error) {
      setResult('Error encoding message: ' + error.message);
    }
  };

  const handleDecode = async (e) => {
    e.preventDefault();
    try {
      const response = await decodeMessage(decodeImage, decodePassword);
      setResult(`Decoded message: ${response.message}\nSize: ${response.size} bytes`);
    } catch (error) {
      setResult('Error decoding message: ' + error.message);
    }
  };

  return (
    <div className="App">
      <h1>CryptoVeil</h1>
      <div className="encode-section">
        <h2>Encode Message</h2>
        <form onSubmit={handleEncode}>
          <input type="file" onChange={(e) => setEncodeImage(e.target.files[0])} required />
          <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Enter message" required />
          <input type="password" value={encodePassword} onChange={(e) => setEncodePassword(e.target.value)} placeholder="Enter password" required />
          <button type="submit">Encode</button>
        </form>
        {encodedImage && <img src={encodedImage} alt="Encoded" />}
      </div>
      <div className="decode-section">
        <h2>Decode Message</h2>
        <form onSubmit={handleDecode}>
          <input type="file" onChange={(e) => setDecodeImage(e.target.files[0])} required />
          <input type="password" value={decodePassword} onChange={(e) => setDecodePassword(e.target.value)} placeholder="Enter password" required />
          <button type="submit">Decode</button>
        </form>
      </div>
      <div className="result">
        <h3>Result:</h3>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default App;