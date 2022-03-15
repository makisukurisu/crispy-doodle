import unittest, main, requests

from data import Data

class Tests(unittest.TestCase):

    def test_mono(self):
        self.assertIsInstance(main.getJSON(Data.mono_url), type(Data.MonoCCY))
    
    def test_git(self):
        self.assertEqual(main.getJSON(Data.git_url), Data.Git_Core)
    
    def test_git_underscore(self):
        self.assertEqual(main.getJSON(Data._url), Data._)
    
    def test_git_makisu(self):
        self.assertEqual(main.getJSON(Data.makisu_url), Data.Makisukurisu)

    def test_git_fela(self):
        self.assertEqual(main.getJSON(Data.fela_url), Data.Fela)

    def test_error_connection(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            main.getJSON(Data.noResponse_url)
    
    def test_error_no_schema(self):
        with self.assertRaises(requests.exceptions.MissingSchema):
            main.getJSON(Data.no_schema)
    
    def test_no_json(self):
        self.assertEqual(main.getJSON(Data.noJson_url), None)

    def test_mono_args_incorrect(self):
        self.assertEqual(main.getJSON(Data.mono_personal_url, headers={"XToken": "12345"}), Data.MonoMissingXToken)
    
    def test_mono_args_unknown(self):
        self.assertEqual(main.getJSON(Data.mono_personal_url, headers={"X-Token": "12345"}), Data.MonoWrongXToken)

if __name__ == "__main__":
    unittest.main()