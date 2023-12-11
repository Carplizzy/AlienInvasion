import unittest
from AlienInvasionClasses import AlienInvasionHard

class AlienInvasionTestHard(unittest.TestCase):
    
    def test_gen_word_(self):
        AlienInvasion_gamewords=["dog","cat","apple","pie","lime","ballon","cookie","lamp","pea","scarf","mittens","husky","python"]
        result=AlienInvasionHard._gen_word_()
        self.assertIn(result,AlienInvasion_gamewords)
    
    def test_word_track_(self):
        result=AlienInvasionHard.__word_track__("cat")

        expected=[{"A":0,"B":0,"C":1,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":1,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0},
                  {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":1,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}]
        self.assertEqual(result,expected)

    def test_guess_location(self):

        game=AlienInvasionHard("cat")
        results=game.__guess_location__(0)
        self.assertEqual(results,0)

        game.__turn__("C")
        results=game.__guess_location__(0)
        self.assertEqual(results,None)


    def test__guess_valid__(self):
        """This method validates that a letter guess is valid depending on location guess. A guess is invalid if it has already been guessesed in that location.
        Arguements:
            guess: a single alphabetical string
        Returns:
            count: returns count=0 if the guess is valid but not correct, returns count=1 if the guess is valid and correct.
            "DNE": returns "DNE" if guess is invalid
        """
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

    def test__check_win_(self):

        game=AlienInvasionHard("CAT")

        game.player_word=["C","A","_"]
        results=game._check_win_()
        self.assertIsNone(results)

        game.player_word=["C","A","T"]
        results=game._check_win_()
        self.assertTrue(results)

        game=AlienInvasionHard()
        game.guesses=0
        results=game._check_win_()
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


