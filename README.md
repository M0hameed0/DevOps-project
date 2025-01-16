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
- **`les secrets et variables`** definir les variables et les secrets necessaires dans Repository secrets de Github


## Installation et utilisation

1. **Cloner le dépôt**:
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
   7- lancer un conteneur Docker avec l'image qu'on a buildé:
     ```bash
     make run2
     ```
   8- voir les logs de conteneur docker:
     ```bash
     make logs
     ```
   9- test le bon fonctionnement de site via une commande:
     ```bash
     make test_api
     ```
## les secrets et variables
Pour que le deploiment en Azure se passe bien, notre pipline à besoin de quelques variable pour mieux euthentifie et se connecter à Azure
Ces variables secrètes contiennent des informations sensibles nécessaires pour permettre à GitHub Actions de s'authentifier auprès d'Azure et de déployer l'application sur Azure App Service en toute sécurité. Voici leur rôle détaillé :

- **`AZUREAPPSERVICE_CLIENTID`** : Identifie l'application (Service Principal) utilisée pour s'authentifier sur Azure.
- **`AZUREAPPSERVICE_SUBSCRIPTIONID`** : Spécifie l'abonnement Azure où les ressources sont déployées.
- **`AZUREAPPSERVICE_TENANTID`** : Identifie le locataire Azure AD (organisation) pour l'authentification.
  
## Pipeline ci-cd.yml:
Le projet inclut un pipeline GitHub Actions pour automatiser les taches presenté dans Makefile, et le deploiement automatique sur AZURE, voilà quelques Actions de notre Pipeline:
   1- le pipeline se divise en 2 partie principal (jobs) que je vais explique dans l'etape suivants
   2- Les tests unitaires sont integré à notre pipline
   3- la construction automatique de l'image Docker
   4- Deploiement sur Azure App Service

la premier partie de pipline (build), vas nous permettre de lancé automatiquement les etapes defini dans Makefile, jusqu'a l'etape de buildé l'image Docker, et aussi créer le fichier ZIP qu'on vas televerser pour le deploiement sur azure.

la deuxieme partie de pipline (deploy), consiste à telecharger l'artfact ZIP qu'on avait créer dans la partie build, puis le decompresser et se connecter à notre environnement Azure gràce à les variables qu'on avait defini dans Repository secrets de GITHUB, et en final deployer l'APP dans l'environnement de deploiement.

## Déclenchement du déploiement
c'est simple, Poussez vos modifications sur la branche main, voilà les commande git :

     ```bash
 	git add .
	git commit -m "Mise à jour"
	git push origin main
     ```

puis, notre pipeline se déclenchera automatiquement et déploiera l'application sur Azure.
## Acceder à l'APP:
Dans mon cas, j'ai deployer l'application dans Azure APP service, voilà le lien pour acceder à l'application:

https://app-python-hng3b7gbgsb9e7c5.francecentral-01.azurewebsites.net/

image de l'appli WEB:

![image](https://github.com/user-attachments/assets/9a9d67d6-66f9-42f2-bc64-fd76a5a99ffe)


## Author

This template was created by **Mohamed Nait boufous** and is intended as an educational resource for DevOps projects involving Flask applications.


