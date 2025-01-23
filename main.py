import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

df = pd.read_csv('ML_exo1.csv', index_col= [0])
df.head()

pd.DataFrame(pearsonr(df['Traffic Density'], df['Air pollution']), index = ['person_coeff','p_value'], columns= ['resultat_test'])

slope, intercept, r_value, p_value, std_err = stats.linregress(df['Traffic Density'], df['Air pollution'])

def Prediction (X):
    return slope * X + intercept

fitline = Prediction(df['Traffic Density'])


plt.scatter(df['Traffic Density'], df['Air pollution'], color="blue", label="Données réelles")
plt.plot(df['Traffic Density'], fitline, color="red", label="Modèle de régression")
plt.title("Relation entre la densité de trafic et la pollution de l'air")
plt.xlabel("Densité de trafic (véhicules/heure)")
plt.ylabel("Pollution de l'air (PM2.5 µg/m³)")