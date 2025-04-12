import unittest
from analyzer import analyze_code_with_adk

class TestAnalyzerWithADK(unittest.TestCase):
    def test_sample_code(self):
        sample_code = """def example_function():\n    pass"""
        results = analyze_code_with_adk(sample_code)
        self.assertIsInstance(results, list)
        self.assertGreaterEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()