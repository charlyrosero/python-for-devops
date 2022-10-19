install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py library/*.py
lint:
	#flake8 ir #pylint
	pylint --disable=R,C *.py library/*.py
test:
	#test
deploy:
	#deploy
all: install lint test deploy