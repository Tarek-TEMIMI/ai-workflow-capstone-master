import unittest
import os
from logger import update_train_log # Importez votre fonction de log

class LogTest(unittest.TestCase):
    def test_01_log_exists(self):
        """Vérifier que le mécanisme de log écrit bien un fichier"""
        log_file = "train-test.log"
        if os.path.exists(log_file):
            os.remove(log_file)
        update_train_log("all", (0,100), 0.05, 10, "test")
        self.assertTrue(os.path.exists(log_file))

if __name__ == '__main__':
    unittest.main()