# Catholic Commentary Data Pipeline

This project collects, organizes, and provides Catholic commentary (encyclicals, homilies, saints' reflections, Church Fathers, etc.) mapped to scripture references for use in a web application.


## Features
- Data model for scripture references and commentary
- List of authoritative Catholic sources
- Scripture reference parser and mapping
- Automated data collection and ingestion
- SQLite database schema
- FastAPI-based API for querying commentaries
- **Robust logging and error handling**: All ingestion steps are logged, including errors and skipped files. A summary line is always written at the end of each run.
- **Filename sanitization**: All downloaded files are sanitized for cross-platform compatibility.
- **Deduplication**: Duplicate works are detected and skipped.
- **PDF extraction**: Uses `pypdf` for extracting text from PDF sources.
- **Validation test suite**: 50+ tests ensure ingestion, scripture mapping, and logging are robust.

## Getting Started
1. Clone the repository
2. Create and activate a Python 3.13+ virtual environment
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the ingestion and extraction scripts to populate the database. After each run, check `downloaded_sources/ccel/ccel_ingest.log` for a summary at the end of the file.
5. Start the API server:
   ```
   uvicorn data_pipeline.api:app --reload
   ```
6. Query the API:
   - Example: `http://127.0.0.1:8000/commentary/?book=Leviticus&chapter=6`

## Contributing
- See CONTRIBUTING.md for guidelines on adding new sources, improving parsing, or extending the API.

## License
See individual source licenses for commentary content. Project code is MIT licensed.
