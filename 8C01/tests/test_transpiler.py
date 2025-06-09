import os
import sys
import unittest

# Allow imports from the parent package when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from compiler.transpiler import transpile


class TranspilerTestCase(unittest.TestCase):
    def test_set_instruction(self):
        asm = transpile("SET A, 1")
        self.assertIn("MVI A, 1", asm)

    def test_add_instruction(self):
        asm = transpile("ADD B, 2")
        self.assertIn("ADD B, 2", asm)


if __name__ == "__main__":
    unittest.main()
