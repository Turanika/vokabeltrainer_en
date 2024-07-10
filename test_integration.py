import unittest
import tkinter as tk
from en_vok_train import VokabelTrainer

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.woerterbuch = {'hello': 'hallo', 'world': 'welt'}
        self.sprache = 'German'
        self.trainer = VokabelTrainer(self.root, self.woerterbuch, self.sprache)

    def tearDown(self):
        self.root.destroy()

    def test_full_workflow(self):
        self.trainer.vokabel_anzeigen()
        self.assertEqual(self.trainer.label_vokabel.cget("text"), 'hello in German')

        self.trainer.naechste_vokabel()
        self.trainer.vokabel_anzeigen()
        self.assertEqual(self.trainer.label_vokabel.cget("text"), 'world in German')

        self.trainer.antwort_anzeigen()
        self.assertEqual(self.trainer.label_vokabel.cget("text"), 'world in German: welt')

        self.trainer.vokabeln_mischen()
        self.assertEqual(self.trainer.index, 0)

if __name__ == '__main__':
    unittest.main()
