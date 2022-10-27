install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			python -m textblob.download_corpora
format:
	#format code
	black *.py library/*.py
lint:
	#flake8 ir #pylint
	pylint --disable=R,C *.py library/*.py
test:
	#test
	python -m pytest -vv --cov=library test_logic.py test_*.py
run:
	docker run -p 127.0.0.1:8080:8080 1dc64134b568
build:
	#build container
	docker build -t deploy-fastapi .
deploy:
	#deploy
	
all: install lint test deploy