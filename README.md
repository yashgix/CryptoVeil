# CryptoVeil: GenAI-Powered Visual Cryptography Engine

CryptoVeil is a full-stack visual cryptography system that utilizes generative AI for cover image creation and implements advanced steganography techniques for secure message hiding. It features a React-based user interface for seamless encryption and decryption operations.

- This project is still in progress.

## Project Structure

- `backend/`: Python backend using FastAPI
  - `api/`: API endpoints
  - `core/`: Core functionality
    - `ai/`: AI and machine learning models
    - `cryptography/`: Encryption and decryption logic
    - `image_processing/`: Image manipulation functions
  - `tests/`: Backend unit tests
- `frontend/`: React frontend
- `data/`: Data storage
- `models/`: Saved AI models
- `docs/`: Project documentation
- `scripts/`: Utility scripts

## Setup Instructions

1. Clone the repository
2. Set up the backend:
   - Create a virtual environment: `python -m venv cryptoveil-env`
   - Activate the environment:
     - Windows: `cryptoveil-env\Scripts\activate`
     - macOS/Linux: `source cryptoveil-env/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`
   - Run the backend: `uvicorn backend.api.main:app --reload`
3. Set up the frontend:
   - Navigate to the frontend directory: `cd frontend`
   - Install dependencies: `npm install`
   - Start the frontend: `npm start`

## Usage

(To be added)




