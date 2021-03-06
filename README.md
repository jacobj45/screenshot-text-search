This is a personal project that was created to perform text search on my mobile screenshots. It uses:
- MeiliSearch for search
- Tesseract for OCR
- ImJoy elFinder for the UI

## Requirements
- Docker
- Docker Compose

## Usage
- Specify the full path to the screenshots folder in `docker-compose.yml`
- Navigate to the repo root directory and run `docker-compose up`
- Open http://localhost:8765 for web UI
