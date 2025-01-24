## **Documentation du Projet : Prédiction des Salaires des Développeurs en Norvège (2024)**

### **1. Introduction**
Ce projet vise à prédire les **salaires des développeurs en Norvège en 2024** en fonction de leur **ancienneté** (niveau d'ancienneté dans l'entreprise). L'objectif est de construire un modèle de **régression linéaire** permettant d'identifier la relation entre l'ancienneté d'un développeur et son salaire, puis de faire des prédictions sur de nouveaux niveau d'ancienneté.

---

### **2. Objectifs**
1. **Analyser les données** disponibles sur les développeurs, incluant leur ancienneté et leur salaire.
2. Construire un **modèle de régression linéaire** pour établir une relation entre l'ancienneté et le salaire.
3. **Évaluer les performances** du modèle à l'aide de métriques comme MAE, MSE et RMSE.
4. Prédire les salaires pour de nouveaux niveau d'ancienneté fournis dans une cellule dédiée.

---

### **3. Prérequis**
- **Bibliothèques Python** :
  - `pandas` : Pour charger et explorer les données.
  - `numpy` : Pour les calculs mathématiques.
  - `matplotlib` et `seaborn` : Pour la visualisation.
  - `sklearn` : Pour la construction et l'évaluation du modèle.
- **Connaissances en Machine Learning** : Notions de régression linéaire et interprétation des métriques.

---

### **4. Description des Données**
Le jeu de données contient deux colonnes principales :
- **Ancienneté** : Ancienneté des développeurs (en années).
- **Salary** : Salaire annuel brut des développeurs (en couronnes norvégiennes, NOK).

Ces données sont utilisées pour analyser la relation entre l'âge et le salaire, et pour construire le modèle prédictif.

---

### **5. Étapes du Projet**

#### **5.1. Chargement et Exploration des Données**
1. **Chargement du dataset** : Utilisation de `pandas` pour charger les données.
2. **Exploration initiale** :
   - Affichage des premières lignes avec `.head()`.
   - Vérification des informations générales avec `.info()`.
   - Résumé statistique des colonnes numériques avec `.describe()`.

#### **5.2. Visualisation et Analyse**
1. **Distribution des données** :
   - Histogramme de chaque variable.
2. **Relation entre `Ancienneté` et `Salary`** :
   - Tracé d'un scatter plot pour visualiser la corrélation.
   - Vérification de la linéarité avec des tendances visuelles.

#### **5.3. Construction du Modèle**
1. **Préparation des données** :
   - Séparation en variables indépendantes (`X`) et dépendantes (`y`).
   - Division des données en ensembles d'entraînement et de test.
2. **Régression Linéaire** :
   - Construction et ajustement du modèle avec `LinearRegression` de `sklearn`.
   - Calcul des coefficients du modèle (pente et intercept).
3. **Évaluation** :
   - Calcul des métriques : MAE, MSE, et RMSE.
   - Visualisation de la ligne de régression.

#### **5.4. Prédiction pour de Nouveaux niveaux d'Ancienneté**
1. Ajout d'une cellule pour entrer une liste de nouveaux niveau d'ancienneté.
2. Utilisation du modèle pour prédire les salaires correspondants.
3. Affichage des résultats.

---

### **6. Résultats**
1. **Performance du modèle** :
   - Valeurs des métriques calculées (MAE, MSE, RMSE).
   - Analyse des écarts entre les salaires réels et prédits.
2. **Prédictions** :
   - Tableau des prédictions pour les nouveaux niveau d'ancienneté fournis.

---

### **7. Conclusion**
Ce projet démontre comment la régression linéaire peut être utilisée pour prédire les salaires en fonction de l'ancienneté dans un secteur spécifique. Les résultats obtenus permettent d'avoir une estimation des salaires pour des ancienneté non présents dans le dataset initial.

---
