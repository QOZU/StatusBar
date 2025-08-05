# test_statusbar.py
"""
Tests for StatusBar module.
"""

import unittest
from statusbar import StatusBar

class TestStatusBar(unittest.TestCase):
    """Test cases for StatusBar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StatusBar()
        self.assertIsInstance(instance, StatusBar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StatusBar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
