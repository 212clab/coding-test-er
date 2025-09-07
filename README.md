# Project Structure
```
coding-test-er/
├── logs/                # Log files (e.g., 250901.log, response_11659.html)
├── problems/            # Daily problem files (e.g., 250901.py, 250902.py)
├── utils/               # Utility modules
│   ├── __init__.py      # Package initialization
│   ├── config.py        # Configuration (e.g., DEFAULT_CONFIG)
│   ├── crawler.py       # Problem crawling logic
│   └── logger.py        # Logging utilities
├── __init__.py          # Package initialization
├── config.py            # Configuration (moved from utils/ for clarity)
└── main.py              # Main entry point
└── .gitignore               # Git ignore file
```
