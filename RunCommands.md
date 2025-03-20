1. Run x script:
.localenv\Scripts\python -m src.scripts.x.py

2. Run specific tests:
set PYTHONPATH=. && .localenv\Scripts\pytest test\test_*.py

3. Run all tests:
set PYTHONPATH=. && .localenv\Scripts\pytest

4. Requirements install:
.localenv\Scripts\python -m pip install -r requirements.txt

5. Start Dashboard:
.localenv\Scripts\python -m src.dashboard.dashboard