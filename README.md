# 💣 JKLM BombParty Bot : Invisible & Imbattable

Un bot Selenium pour **JKLM.fun (BombParty)** conçu pour être à la fois ultra-performant et indétectable. Il simule un comportement humain avec des erreurs de frappe réalistes, des temps de réaction variables et un système de contrôle à distance par touches.

---

## ✨ Fonctionnalités
* **Frappe Humaine :** Délai aléatoire entre chaque lettre pour simuler un vrai clavier.
* **Simulation d'erreurs :** Le bot fait parfois des fautes de frappe volontaires, les efface et se corrige (20% de chances).
* **Indétectable :** Utilise la détection visuelle de l'input pour ne s'activer que lorsque c'est réellement votre tour.
* **Contrôles à la volée :** Mise en pause ou arrêt total instantané via des touches raccourcies.
* **Gestion des Accents :** Nettoyage automatique du dictionnaire pour correspondre au format de JKLM.

---

## 🛠️ Prérequis
1. **Python 3.x** installé sur votre ordinateur.
2. Navigateur **Microsoft Edge**.
3. Un fichier **mots.txt** à la racine du projet (un mot par ligne).

---

## 🚀 Installation

Ouvrez votre terminal et installez les dépendances nécessaires avec cette commande :

pip install pyautogui selenium keyboard webdriver-manager

---

## 🎮 Utilisation

1. **Préparation :** Placez votre fichier **mots.txt** dans le dossier du script.
2. **Lancement :** Dans votre terminal, lancez : python JKLMbot.py
3. **Lien :** Collez le lien complet de la partie (ex: https://jklm.fun/ABCD) quand le script le demande.
4. **En jeu :**
   * Rejoignez la partie avec votre pseudo (ex: thib).
   * **CRUCIAL :** Faites un clic gauche manuel dans la zone de texte du jeu une fois la page chargée pour que le bot puisse écrire au bon endroit.

---

## ⌨️ Contrôles Clavier

* **Touche [9] : PAUSE / REPRISE** (Suspend le bot pour discuter ou jouer manuellement).
* **Touche [0] : ARRÊT TOTAL** (Ferme le script et le navigateur Edge immédiatement).

---

## ⚠️ Avertissements
* **Focus souris :** Le bot simule des frappes réelles. Si vous changez de fenêtre pendant votre tour, il écrira dans le vide.
* **Fair-play :** Ce script est une preuve de concept. L'utilisation abusive de bots peut nuire à l'expérience des autres joueurs et entraîner un bannissement.

---
Développé pour l'élite des bombardiers. 🚀