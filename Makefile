.PHONY: init install test run1 clean build run2 test_api
init:
	python3 -m venv .venv

install:
	. .venv/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

test:
	. .venv/bin/activate; pytest test.py

run1:
	. .venv/bin/activate; python app.py

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type f -name "*.pyc" -delete

build:
	docker build -t mycalculator:latest .

#  run2:
#     docker run -p 5000:5000 mycalculator:latest

test_api:
    docker run mycalculator:latest python -m pytest test.py -v
