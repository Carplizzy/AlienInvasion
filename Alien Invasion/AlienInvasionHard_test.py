import unittest
from AlienInvasion_Game import AlienInvasionHard

class AlienInvasionHardTest(unittest.TestCase):
    
    def test_gen_word_(self):
        AlienInvasion_gamewords=["HUSKY","PYTHON","CAT","DOG","TEA","ROCK","BINARY","LAMP","APPLE","LAPTOP"]
        result=AlienInvasionHard.__gen_word__()
        self.assertIn(result,AlienInvasion_gamewords)
    
    def test_word_track_(self):
        game=AlienInvasionHard()
        result=game.__word_track__("CAT")
        expected=[{"A":0,"B":0,"C":1,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":1,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":1,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}]
        self.assertEqual(result,expected)

    def test_guess_location(self):
        game=AlienInvasionHard("CAT")
        results=game.__guess_location__(0)
        self.assertEqual(results,0)

        game.__turn__("C")
        results=game.__guess_location__(0)
        self.assertEqual(results,None)


    def test__guess_valid__(self):
        
        game=AlienInvasionHard(word="CAT")
        game.__guess_location__(0)
        result=game.__guess_valid__("C")
        self.assertEqual(result,1) 

        game.__guess_location__(1)
        result=game.__guess_valid__("B")
        self.assertEqual(result,0)
        game.__turn__("B")

        game.__guess_location__(1)
        result=game.__guess_valid__("B")
        self.assertEqual(result,"DNE")

        game=AlienInvasionHard(word="APPLE")
        game.__guess_location__(0)
        result=game.__guess_valid__("P")
        self.assertEqual(result,0) 

        game=AlienInvasionHard(word="APPLE")
        game.__guess_location__(1)
        result=game.__guess_valid__("P")
        self.assertEqual(result,1) 
    
    def test__update_pword__(self):

        game=AlienInvasionHard("CAT")
        game.location=0
        results=game.__update_pword__("C")
        self.assertEqual(results,["C","_","_"])

        game.location=1
        results=game.__update_pword__("A")
        self.assertEqual(results,["C","A","_"])

    def test__check_win_lose__(self):

        game=AlienInvasionHard("CAT")

        game.player_word=["C","A","_"]
        results=game.__check_win_lose__()
        self.assertIsNone(results)

        game.player_word=["C","A","T"]
        results=game.__check_win_lose__()
        self.assertTrue(results)

        game=AlienInvasionHard()
        game.guesses=0
        results=game.__check_win_lose__()
        self.assertFalse(results)

    def test__turn__(self):

        game=AlienInvasionHard("CAT")
        game.__guess_location__(0)
        expected_wordtrack=[{"A":0,"B":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":1,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":1,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}]
        results=game.__turn__("C")
        self.assertEqual(results,1)
        self.assertEqual(game.word_track,expected_wordtrack)
        self.assertEqual(game.guesses,7)


        game.__guess_location__(1)
        results=game.__turn__("B")
        self.assertEqual(results,None)
        expected_wordtrack=[{"A":0,"B":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":1,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":1,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}]
        self.assertEqual(game.word_track,expected_wordtrack)
        self.assertEqual(game.guesses,6)

        game.__guess_location__(1)
        results=game.__turn__("B")
        self.assertEqual(results,"DNE")
        self.assertEqual(game.word_track,expected_wordtrack)
        self.assertEqual(game.guesses,6)

if __name__=='__main__':
    unittest.main()


