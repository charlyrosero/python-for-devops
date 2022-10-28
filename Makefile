install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
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
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 633987678946.dkr.ecr.us-east-2.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 633987678946.dkr.ecr.us-east-2.amazonaws.com/fastapi-wiki:latest
	docker push 633987678946.dkr.ecr.us-east-2.amazonaws.com/fastapi-wiki:latest
	
all: install post-install lint test deploy