# test_blockfilend.py
"""
Tests for BlockFiLend module.
"""

import unittest
from blockfilend import BlockFiLend

class TestBlockFiLend(unittest.TestCase):
    """Test cases for BlockFiLend class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockFiLend()
        self.assertIsInstance(instance, BlockFiLend)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockFiLend()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
