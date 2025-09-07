# Project Structure
```
algorithm-study/
├── shared/                  # JSON data for crawled problem details (e.g., 11659.json)
├── _212c/                   # Python solutions
│   ├── logs/                # Log files (e.g., 250901.log, response_11659.html)
│   ├── problems/            # Daily problem files (e.g., 250901.py, 250902.py)
│   ├── utils/               # Utility modules
│   │   ├── __init__.py      # Package initialization
│   │   ├── config.py        # Configuration (e.g., DEFAULT_CONFIG)
│   │   ├── crawler.py       # Problem crawling logic
│   │   └── logger.py        # Logging utilities
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Configuration (moved from utils/ for clarity)
│   └── main.py              # Main entry point
├── _pqr4579/                # JavaScript solutions
└── .gitignore               # Git ignore file
```

# Setup
```
Clone the repository:
git clone https://github.com/your_username/algorithm-study.git
cd algorithm-study


Install dependencies (Python):
pip install requests beautifulsoup4


Run the Python script:
python _212c/main.py



Workflow

Sync with friend's repo:
git fetch upstream
git merge upstream/main
git push origin main


Add solutions:

Python: Add to _212c/problems/ (e.g., 250902.py).
JavaScript: Add to _pqr4579/.
Commit and push:git add _212c/
git commit -m "Add solution for problem 12345"
git push origin main




Share data: Problem data is saved in shared/ (e.g., 11659.json).


Cooperation

Python solutions: _212c/ (private repository).
JavaScript solutions: _pqr4579/.
Shared data: Use shared/ for JSON files.
Pull requests: Submit PRs to friend_username/algorithm-study for collaboration.
```
