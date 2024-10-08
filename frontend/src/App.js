import React, { useState } from 'react';
import './App.css';
import { encryptMessage, decryptImage } from './api';

function App() {
  const [message, setMessage] = useState('');
  const [image, setImage] = useState(null);
  const [result, setResult] = useState('');

  const handleEncrypt = async () => {
    try {
      const response = await encryptMessage(message);
      setResult(`Encrypted: ${response.encrypted_message}`);
    } catch (error) {
      console.error('Encryption error:', error);
      setResult('Encryption failed. Please try again.');
    }
  };

  const handleDecrypt = async () => {
    if (image) {
      try {
        const response = await decryptImage(image);
        setResult(`Decrypted: ${response.decrypted_message}`);
      } catch (error) {
        console.error('Decryption error:', error);
        setResult('Decryption failed. Please try again.');
      }
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>CryptoVeil</h1>
        <p>GenAI-Powered Visual Cryptography Engine</p>
      </header>
      <main>
        <section>
          <h2>Encrypt a Message</h2>
          <input 
            type="text" 
            value={message} 
            onChange={(e) => setMessage(e.target.value)} 
            placeholder="Enter your message" 
          />
          <button onClick={handleEncrypt}>Encrypt</button>
        </section>
        <section>
          <h2>Decrypt an Image</h2>
          <input 
            type="file" 
            accept="image/*" 
            onChange={(e) => setImage(e.target.files[0])} 
          />
          <button onClick={handleDecrypt}>Decrypt</button>
        </section>
      </main>
      <div>
        <h3>Result:</h3>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default App;