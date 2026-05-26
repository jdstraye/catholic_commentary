# Contributing to Catholic Commentary Data Pipeline

Thank you for your interest in contributing!

## How to Contribute
- **Add new sources:** Update `data_pipeline/sources.py` and add download/extraction scripts as needed.
- **Improve scripture parsing:** Edit `data_pipeline/scripture_parser.py` and add tests for new formats or languages.
- **Extend the API:** Add endpoints or filters in `data_pipeline/api.py`.
- **Write tests:** Add scripts or use pytest to validate data extraction, mapping, and API responses.
- **Maintain logging and summary reporting:** Ensure all ingestion scripts log errors and always write a summary at the end of the log file.
- **Documentation:** Improve the README or this guide.

## Code Style
- Use Python 3.8+ type hints.
- Follow PEP8 for formatting.
- Document all public functions and classes.

## Issues & Pull Requests
- Open an issue for bugs, feature requests, or questions.
- Fork the repo, create a feature branch, and submit a pull request.

## Validation
- All ingestion and logging changes should be covered by validation tests (see `tests/validation/test_validation_bulk.py`).

## Contact
For major changes or questions, open an issue or discussion on GitHub.
