# Health Calculator App - DevOps Project
Health Calculator App est une application Python conçue pour effectuer des calculs simple des métriques de santés. Elle peut être exécutée localement dans un environnement virtuel ou déployée dans un conteneur Docker. 
le projet est entièrement containerisé avec Docker, géré par un Makefile, le depot inclut également une pipeline CI/CD pour un déploiement automatisé sur Azure App Service.

## Fonctionnalités et les calculs
Calculs de santé :
IMC (BMI) : Calcul basé sur le poids (kg) et la taille (m).
BMI = weight (kg)/(height (m))^2

BMR (Basal Metabolic Rate) : Basé sur les formules  de Harris-Benedict.
For males:
BMR = 88.362 + (13.397 x weight (kg)) + (4.799 x height (cm)) - (5.677 x age (years))
For females:
BMR = 447.593 + (9.247 x weight (kg)) + (3.098 x height (cm)) - (4.330 x age (years))

## Project Structure

The repository is organized as follows:

```plaintext
DEVOPS-PROJECT/
├── Dockerfile          # Instructions de création de l'image Docker
├── Makefile            # Script pour automatiser les tâches
├── app.py              # Code principal de l'application
├── health_utils.py     # Utilitaires pour vérifier l'état de santé
├── requirements.txt    # Dépendances Python
├── templates/
│   └── home.html       # Interface utilisateur HTML
├── test.py             # Tests unitaires
├── .github/workflows/	 
│   └── ci-cd.yml	# Pipeline CICD pour le deploiement
│   └── test_pipeline_With_makefile	# Template pour la config de pipeline test Makefile
└── README.md           # Documentation du projet

```

## Descriptions des Fichiers

- **`Dockerfile`** :
Contient les instructions pour construire une image Docker pour l'application. Il inclut les étapes nécessaires pour installer les dépendances, copier les fichiers de l'application et configurer l'environnement d'exécution.

- **`Makefile`** :
Un script d'automatisation pour simplifier les tâches courantes comme l'installation des dépendances, l'exécution des tests, la création de l'image Docker, et le lancement de l'application, voilà les commandes de makefile:
	- init        - Construit l'environnement virtuel .venv"
	- install     - install les requirements.txt"			
	- test        - lancer le fichier test.py"
	- run1        - Exécute l'application dans .venv en arrière-plan"
	- clean       - supprission de l'environemment virtuel et cache arrière-plan"
	- build       - creation de l'image docker"
	- run2        - lancer le conteneur en cours d'exécution"
	- logs        - Affiche les logs du conteneur en cours d'exécution"
	- test_api    - lancer des requette vers conteneur pour tester l'etat de fonctionnement"
	- make help   - Affiche cette l'aide et les commandes de makefile"
   
- **`app.py`** :
Le fichier principal de l'application. Il configure les routes de l'API REST et les connecte aux fonctions définies dans health_utils.py pour fournir les points d'accès aux calculs d'IMC et de BMR.

- **`health_utils.py`** :
Contient les fonctions utilitaires principales pour le calcul de l'IMC et du BMR. Ce fichier regroupe toute la logique métier de l'application.

- **`requirements.txt`** :
Liste des dépendances Python nécessaires pour exécuter l'application. Ces dépendances seront installées automatiquement dans l'environnement virtuel ou lors de la construction de l'image Docker.

- **`templates/home.html`** :
Un fichier HTML utilisé comme interface utilisateur pour présenter ou tester l'application. Ce fichier peut être enrichi pour inclure des formulaires ou afficher les résultats des calculs.

- **`test.py`** :
Fichier de tests unitaires pour vérifier le bon fonctionnement des fonctions de calcul définies dans health_utils.py. Il garantit que l'application produit les résultats attendus.

- **`.github/workflows/ci-cd.yml`** :
Un fichier YAML décrivant le pipeline CI/CD. Il automatise les tests, la construction de l'image Docker et le déploiement de l'application sur Azure App Service lorsque du code est poussé dans la branche principale.

- **`.github/workflows/test_pipeline_With_makefile`** :
Un modèle de pipeline CI/CD basé sur Makefile. Vous pouvez renommer ce fichier avec l'extension .yml si vous souhaitez exécuter un pipeline spécifique utilisant les commandes définies dans le Makefile.

- **`README.md`** :
Documentation complète du projet, expliquant l'objectif, les fonctionnalités, les instructions d'installation et d'exécution, ainsi que les détails du pipeline CI/CD.

## Prérequis

- **`Python`** 3.10 ou supérieur
- **`Docker`** installé sur votre machine
- **`Compte Azure`** avec App Service configuré
- **`Make`** installé pour automatiser les tâches


## Installation et utilisation

1. ** Cloner le dépôt**:
   ```bash
   git clone <repository-url>
   cd DEVOPS-PROJECT
   ```

2. **Exécuter localement**:
  1- Initialiser l'environnement
     ```bash
     make init
     ```
   2- Installer les dependances:
     ```bash
     make install
     ```
   3- lancer une test de fonctionnement d'API:
     ```bash
     make test
     ```
   4- lancer l'App:
     ```bash
     make run1
     ```
   5- supprimer l'environnement virtuel + cache:
     ```bash
     make clean
     ```
   6- builder l'image Docker grace à Dockerfile:
     ```bash
     make build
     ```
   6- lancer un conteneur Docker avec l'image qu'on a buildé:
     ```bash
     make run2
     ```
   6- voir les logs de conteneur docker:
     ```bash
     make logs
     ```
   6- test le bon fonctionnement de site via une commande:
     ```bash
     make test_api
     ```
4. **Application**:
   - Start the Flask app locally:
     ```bash
     make run
     ```


5. **Run Tests**:
   - Execute unit tests to verify functionality:
     ```bash
     make test
     ```

## Additional Configuration

- **Environment Variables**:
  - Use the `.env` file to store any environment-specific configurations or sensitive information. Be sure to keep this file out of version control by listing it in `.gitignore`.

## Deployment Instructions

For deployment, configure CI/CD pipelines according to your preferred platform (e.g., GitHub Actions, Azure Pipelines). This template can be used with cloud deployment platforms like AWS, Azure, or Heroku for easy scalability.
  - Use `pipeline.yaml` as a template for a pipeline to build and deploy an application on Azure

## Author

This template was created by **Ali Mokh** and is intended as an educational resource for DevOps projects involving Flask applications.

## License and Usage

This project template is open to use by anyone and may be freely adapted for personal or professional projects. If you use this template as part of teaching materials or educational content, please cite **Ali Mokh** as the original author.

