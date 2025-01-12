# 🚗 Car Game

Car Game est un jeu d'arcade simple développé avec Pygame. L'objectif est d'éviter les véhicules qui apparaissent sur la route tout en accumulant des points. Plus vous survivez longtemps, plus la vitesse augmente, rendant le jeu de plus en plus difficile !

 # 🎮 Fonctionnalités

    Menu principal :
        Lancer une nouvelle partie.
        Accéder aux réglages pour ajuster la vitesse.
        Quitter le jeu.
    Réglages :
        Ajuster la vitesse de base du jeu.
        Revenir au menu principal.
    Game Over : Si vous entrez en collision avec un autre véhicule, le jeu se termine. Vous avez alors plusieurs options :
        - Rejouer la partie.
        - Revenir au menu principal.
        - Quitter le jeu.

# 🎮 Contrôles

| Touche               | Action                                    |
|----------------------|-------------------------------------------|
| `←` (flèche gauche)  | Déplacer la voiture vers la voie de gauche|
| `→` (flèche droite)  | Déplacer la voiture vers la voie de droite|
| `Y`                  | Rejouer après un Game Over                |
| `M`                  | Revenir au menu principal après un Game Over|
| `N`                  | Quitter le jeu après un Game Over         |


 # 🔧 Installation et Exécution
Prérequis :

    Python 3.x doit être installé sur votre machine.
    La bibliothèque Pygame doit être installée.

Pour installer Pygame, exécutez la commande suivante :
```
pip install pygame
```
    - Si erreur, créer un environnement virtuel ( Exemple: python3 -m venv car ; source car/bin/activate et ensuite réexcutez la commande d'installation.)
Lancer le jeu

    Clonez ce dépôt ou copiez les fichiers du projet.
    Assurez-vous que le répertoire images contient les images des véhicules et de la voiture du joueur.
    Exécutez le fichier car_game.py :

python3 car_game.py

## 📂 Structure du projet

Car Game/
├── images/                      # Dossier contenant les images des véhicules
│   ├── car.png
│   ├── pickup_truck.png
│   ├── semi_trailer.png
│   ├── taxi.png
│   └── van.png
├── car_game.py                  # Fichier principal du jeu
└── README.md                    # Fichier de documentation du projet


# # 🖼️ Ressources

    - Images des véhicules : Les images utilisées pour les véhicules et la voiture du joueur se trouvent dans le dossier images. Vous pouvez remplacer ces images par vos propres sprites, en veillant à conserver les mêmes noms de fichiers.

# # 🚀 Améliorations possibles

Voici quelques idées d'amélioration pour le jeu :

   -  Ajout de niveaux : Introduire des niveaux avec des vitesses de jeu progressives.
   -   Ajout de bonus : Ajouter des objets à collecter, tels que des boosts de vitesse ou des protections temporaires contre les collisions.
   - Effets sonores : Ajouter des sons pour les collisions et les changements de voie.
   - Meilleur design du menu : Rendre le menu principal et les écrans de fin de partie plus attrayants visuellement.

# # 📜 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer à votre convenance.
