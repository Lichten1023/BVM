import os
import unittest
import importlib

vm = importlib.import_module('8001.vm')

class HelloWorldProgramTest(unittest.TestCase):
    def test_hello_program(self):
        program_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'programs', 'hello.asm'))
        vm_instance = vm.run_file(program_path)
        expected_output = 'Hello World'
        self.assertEqual(''.join(vm_instance.output), expected_output)
        expected_memory = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
        self.assertEqual(vm_instance.memory[:len(expected_memory)], expected_memory)
        self.assertEqual(vm_instance.registers[0], expected_memory[-1])

if __name__ == '__main__':
    unittest.main()
