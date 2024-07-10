import unittest
import tkinter as tk
from en_vok_train import VokabelTrainer

class TestVokabelTrainer(unittest.TestCase):
    def setUp(self):
        # Set up a real Tkinter root and a sample woerterbuch
        self.root = tk.Tk()
        self.woerterbuch = {'hello': 'hallo', 'world': 'welt'}
        self.sprache = 'German'
        self.trainer = VokabelTrainer(self.root, self.woerterbuch, self.sprache)

    def tearDown(self):
        # Destroy the Tkinter root window after each test
        self.root.destroy()

    def test_initial_state(self):
        # Test the initial state of the VokabelTrainer
        self.assertEqual(self.trainer.index, 0)
        self.assertEqual(self.trainer.keys, ['hello', 'world'])
        self.assertEqual(self.trainer.sprache, 'German')

    def test_vorherige_vokabel(self):
        # Test the vorherige_vokabel method
        self.trainer.vorherige_vokabel()
        self.assertEqual(self.trainer.index, 1)
        self.trainer.vorherige_vokabel()
        self.assertEqual(self.trainer.index, 0)

    def test_naechste_vokabel(self):
        # Test the naechste_vokabel method
        self.trainer.naechste_vokabel()
        self.assertEqual(self.trainer.index, 1)
        self.trainer.naechste_vokabel()
        self.assertEqual(self.trainer.index, 0)

    def test_antwort_anzeigen(self):
        # Test the antwort_anzeigen method
        self.trainer.index = 0
        self.trainer.antwort_anzeigen()
        self.assertEqual(self.trainer.label_vokabel.cget("text"), 'hello in German: hallo')

    def test_vokabel_anzeigen(self):
        # Test the vokabel_anzeigen method
        self.trainer.index = 0
        self.trainer.vokabel_anzeigen()
        self.assertEqual(self.trainer.label_vokabel.cget("text"), 'hello in German')

    def test_shuffle_vokabeln(self):
        # Test the shuffle_vokabeln method
        original_keys = self.trainer.keys[:]
        shuffle_attempts = 0
        while shuffle_attempts < 10:
            self.trainer.vokabeln_mischen()
            if self.trainer.keys != original_keys:
                break
            shuffle_attempts += 1
        self.assertNotEqual(self.trainer.keys, original_keys, "Vokabeln wurden nach 10 Versuchen nicht gemischt")

if __name__ == '__main__':
    unittest.main()