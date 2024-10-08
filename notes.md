Formateurs : Baptiste Courbe & Theophile
Lundi.
- Intégration continue: à faire dans le
dev > recette > prod.

CI : Code versioning & Test running
CD : continuous delivery : nouveau code = nouvelle release non déployées sur un env. Le déploiement est fait à la main
CD : continuous deployment: nouveau code = nouvelle release => déploiement automatique

pyramide de test : unit test < integration test < test fonctionnel

?artifactory

Continuous Training > CD > CI. Le CT nécessite un failgate

Questions: 
[cycle de ré-entraînement] Déclenchement du training par une modification de la donnée
[Test de la cohérence du modèle]
sonar
bonne pratique ? faut-il mocker les services? ou vrais appels? outil pour monitorer le coverage des tests (éviter le déploiement si seuil pas atteint)
est-on obligé 

Bonnes pratiques:
*requirements :
- séparer les requirements. Selon la fonctionnalité.
- propre à ton module
- requirements liés au test
- dépendances (req.dev) permettant de développer

*sur les tests
- lorsqu'on a un bug (peut-être un cas dégénéré qu'on avait pas prévu) écrire un test unitaire associé à ce bug. Pour documenter le bug.
- prioriser les tests par rapport à là où sont les limites (mauvaise qualité de la donnée, modèle instable)
- la pyramide est une check-list
- format test end-to-end given...when...then
- les tests fonctionnels sont à exécuter en dernier. On met les tests du moins coûteux au plus coûteux
- test d'integration = test d'un usecase. exemple: feature_engineering.
- tp 2 : on teste juste le fait que le modèle puisse être déclenché par la disponibilité d'un fichier. Dans ce cas là, on peut mocker le training ou faire le training d'un modèle dégradé.
Dans ce cas, le train est fait dans la CI.
- test doit être idempotent.

*iac
- terraform : le code terraform dépend du cloud provider. terraform a son propre langage
- terraform et ansible peuvent être déployés dans la CI ou en local
- ansible permet de configurer la machine dans l'état voulu. Il faut que la machine soit accessible en ssh car ansible se connecte en SSH
- ansible est en python et nécessite un fichier yaml.
- 80% des projets sont packagés dans un container docker. Les containers peuvent être exposés.
- tag avec le nom du projet.
- Imbrication des outils.
    1- on crée les ressources par terraform et on enregistre l'ip de la machine
    2- on configure la ressource (EC2) avec ansible à qui on communique l'ip
    3- on déploie une image docker dessus en utilisant ansible.
    -(2) est skippé si on utilise ECS
- docker compose : pour installer un pool de container
- jupyter hub : interface. jupyter lab: c'est le lab avec les espaces de travail.
les 2 sont sur des containers différents dans le cas du TP
il est possible de tester (mettre des tests sur terraform & ansible)
- Airflow : avoir une indépendance des environnements pour pouvoir avoir des env. python différents pour les projets. i.e. avoir une conteneurisation du code
- ?bluecore.
- deployer un contexte 
Option 1: déployer un airflow au niveau de l'entreprise, puis faire des tâches qui contenerise le code du projet avec son env. dédié.
- Option 2: d'avoir un airflow au niveau du projet. donc un airflow & UI par projet et un scheduler par projet.
- delta-table, à lire

- La modification du code est directement pris en compte dans la UI du moment où le code a été changé dans le répertoire des DAGS. Pas besoin d'attendre la CI. [dans le cadre du TP]
-> sinon, on intègre dans la CI une étape de déploiement des DAGs qui n'est ni plus, ni moins qu'une copie des scripts dans le directory des DAGs.

- tout coupler lorsque démo.
- découpler lorsque cycle de vie différent entre les artefacts ou lorsque les ressources sont différentes.
- on automatise quand on commence à faire répéter la même tâche manuelle et qu'elle prenne du temps.
? airflow worker
- joblib > pickle pour enregistrer les modèles.
*ML Flow
experiments = group de models. Best practice : group them by subjects
models = pointeurs to the experimented model

ps aux | grep mlflown #get ports
mlflow.set_tracking_uri("https://0.0.0.0:52473)

--port 52473

Cloud provider FR:
OVHcloud
Scalingo
Scaleway
DSS outscale