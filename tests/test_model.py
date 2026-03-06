import unittest
from model import model_train, model_predict

class ModelTest(unittest.TestCase):
    def test_01_train(self):
        """Tester l'entraînement du modèle"""
        # On utilise un mode test pour ne pas polluer les logs de prod
        model_train(test=True)
        # Vérifiez ici si le fichier 'test-model-all.joblib' existe
        
    def test_02_predict(self):
        """Tester la prédiction"""
        result = model_predict("all", "2019", "08", "01", test=True)
        self.assertTrue(result['y_pred'] >= 0)

if __name__ == '__main__':
    unittest.main()