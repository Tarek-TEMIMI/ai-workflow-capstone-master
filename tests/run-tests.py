import unittest
import sys
import os

# Ensure the current directory is in the path so we can import our modules
sys.path.append(os.getcwd())

from tests.test_api import *
from tests.test_model import *
from tests.test_logging import *

if __name__ == '__main__':
    # Create a test suite combining all tests
    test_suite = unittest.TestSuite()
    
    # Add tests from the individual modules
    test_suite.addTest(unittest.makeSuite(ApiTest))
    test_suite.addTest(unittest.makeSuite(ModelTest))
    test_suite.addTest(unittest.makeSuite(LoggingTest))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Exit with non-zero code if tests failed (important for CI/CD)
    if not result.wasSuccessful():
        sys.exit(1)