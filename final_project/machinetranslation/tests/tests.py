import unittest
import translator

class TestforTranslator(unittest.TestCase):
    def test_null_for_fren(self):
        translated = translator.french_to_english(None)
        self.assertEqual(translated, "missing")
    
    def test_null_for_enfr(self):
        translated = translator.english_to_french(None)
        self.assertEqual(translated, "missing")

    def test_english_to_french(self):
        translated = translator.french_to_english("Bonjour")
        self.assertEqual(translated, "Hello")

    def test_french_to_english(self):
        translated = translator.english_to_french("Hello")
        self.assertEqual(translated, "Bonjour")

if __name__ == "__main__":
    unittest.main()