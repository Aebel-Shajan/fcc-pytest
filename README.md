# Pytest tutorial

I followed the tutorial below to learn about pytest.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/cHYq1MRoyI0/0.jpg)](https://www.youtube.com/watch?v=cHYq1MRoyI0)


Pytest documentation: https://docs.pytest.org/en/latest/contents.html

# Setup
Create a virtual environment by running the following command:
```
python -m venv venv
```

Activate the virtual env:
* windows: `venv\Scripts\activate`
* macOSLinux: `source venv/bin/activate`


Install project dependencies: 
```
pip install -r requirements.txt
```

# Usage
Run tests by doing:
```
pytest ./tests/test_circle.py
```
