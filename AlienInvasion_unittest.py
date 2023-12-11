import unittest
from AlienInvasionGameWORKIN import AlienInvasion
class AlienInvasionTest(unittest.TestCase):
    
    def test_gen_word_(self):
        AlienInvasion_gamewords=["dog","cat","apple","pie","lime","ballon","cookie","lamp","pea","scarf","mittens","husky","python"]
        result=AlienInvasion._gen_word_()
        self.assertIn(result,AlienInvasion_gamewords)
    
    def test_word_track_(self):
        result=AlienInvasion._word_track_("cat")
        expected={"A":1,"B":0,"C":1,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":1,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
        self.assertEqual(result,expected)
        
    def test__guess_valid__(self):

        game=AlienInvasion
        game.word_track=game._word_track_("cat")
        results=game.__guess_valid__(game,"A")
        self.assertEqual(results,1)

        results=game.__guess_valid__(game,"A")
        self.assertEqual(results,"DNE")

        results=game.__guess_valid__(game,"B")
        self.assertEqual(results,0)

        results=game.__guess_valid__(game,"invalid gues")
        self.assertEqual(results,"DNE")

    def test_update_pword_(self):

        game=AlienInvasion("CAT")
        results=game.__update_pword__("C")
        self.assertEqual(results,["C","_","_"])

        results=game.__update_pword__("D")
        self.assertEqual(results,["C","_","_"])


    def test_check_win_lose_(self):
        game=AlienInvasion("cat")

        results=game._check_win_lose_()
        self.assertEqual(results,None)

        game.player_word=["C","A","T"]
        results=game._check_win_lose_()
        self.assertEqual(results,True)

        game=AlienInvasion()
        game.guesses=0
        results=game._check_win_lose_()
        self.assertEqual(results,False)

    def test_turn_(self):
        #runs guess valid, if guess is valid and count =0 deduct a guess
        #if guess valid >0 then update p_word and return count
        game=AlienInvasion("CAT")
        results=game.__turn__("A")
        self.assertEqual(results,1)
        self.assertEqual(game.guesses,7)
        self.assertAlmostEqual(game.player_word,["_","A","_"])

        results=game.__turn__("invalid guess")
        self.assertEqual(results,"DNE")
        self.assertEqual(game.guesses,7)
        self.assertAlmostEqual(game.player_word,["_","A","_"])

        results=game.__turn__("B")
        self.assertEqual(results,None)
        self.assertEqual(game.guesses,6)
        self.assertAlmostEqual(game.player_word,["_","A","_"])

        results=game.__turn__("B")
        self.assertEqual(results,"DNE")
        self.assertEqual(game.guesses,6)
        self.assertAlmostEqual(game.player_word,["_","A","_"])


if __name__=='__main__':
    unittest.main()


