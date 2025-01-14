.PHONY: help init install test run1 clean build run2 logs test_api
help:
	@echo "Commandes disponibles :"
	@echo "  make init        - Construit l'environnement virtuel .venv"
	@echo "  make install     - install les requirements.txt"			
	@echo "  make test        - lancer le fichier test.py"
	@echo "  make run1        - Exécute l'application dans .venv en arrière-plan"
	@echo "  make clean       - supprission de l'environemment virtuel et cache arrière-plan"
	@echo "  make build       - creation de l'image docker"
	@echo "  make run2        - lancer le conteneur en cours d'exécution"
	@echo "  make logs        - Affiche les logs du conteneur en cours d'exécution"
	@echo "  make test_api    - lancer des requette vers conteneur pour tester l'etat de fonctionnement"
	@echo "  make help        - Affiche cette aide"
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

run2:
	docker run -d --name mycalculator-container -p 5000:5000 mycalculator

logs:
	docker logs -f mycalculator-container

test_api:
	curl -I GET http://127.0.0.1:5000/

