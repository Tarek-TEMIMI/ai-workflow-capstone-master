import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os

# 1. Simulation de données (Remplacez par vos vrais y_test et y_pred)
# Dans un cas réel, vous chargeriez vos logs ou feriez une prédiction ici
dates = pd.date_range(start='2019-01-01', periods=30, freq='D')
y_true = np.array([100 + i*2 + np.random.randint(-10, 10) for i in range(30)])
y_pred_rf = np.array([100 + i*2.1 + np.random.randint(-5, 5) for i in range(30)]) # Votre modèle
y_baseline = np.full(shape=30, fill_value=y_true.mean()) # Baseline (Moyenne simple)

# 2. Calcul des performances (Monitoring exigé par le feedback)
rmse_rf = np.sqrt(mean_squared_error(y_true, y_pred_rf))
rmse_base = np.sqrt(mean_squared_error(y_true, y_baseline))

# 3. Création du graphique
plt.figure(figsize=(12, 6))
plt.plot(dates, y_true, label='Valeurs Réelles', color='black', linewidth=2, marker='o')
plt.plot(dates, y_pred_rf, label=f'Random Forest (RMSE: {rmse_rf:.2f})', color='blue', linestyle='--')
plt.plot(dates, y_baseline, label=f'Baseline Moyenne (RMSE: {rmse_base:.2f})', color='red', linestyle=':')

plt.title('Comparaison des Modèles : Revenus AAVAIL', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Revenu ($)')
plt.legend()
plt.grid(True, alpha=0.3)

# 4. Sauvegarde
if not os.path.exists('plots'):
    os.makedirs('plots')

plt.savefig('plots/model_comparison.png')
print("Graphique généré avec succès dans plots/model_comparison.png")
plt.show()