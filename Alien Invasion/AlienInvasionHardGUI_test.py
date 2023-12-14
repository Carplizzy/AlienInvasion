import unittest
from AlienInvasion_Game import AlienInvasionHardGUI
from AlienInvasion_Game import AlienInvasionHard


class AlienInvasionHardGUITest(unittest.TestCase):
    gui=AlienInvasionHardGUI()
    
    def test__start_game__(self):
        AlienInvasionHardGUITest.gui.__start_game__()
        result=AlienInvasionHardGUITest.gui.gamemode
        self.assertEqual(result,"easy")

    def test__start_game_hard__(self):
        AlienInvasionHardGUITest.gui.__start_game_hard__()
        result=AlienInvasionHardGUITest.gui.gamemode
        self.assertEqual(result,"hard")
        result=type(AlienInvasionHardGUITest.gui.game)
        self.assertEqual(result,AlienInvasionHard)

    def test__choose_location__(self):
        AlienInvasionHardGUITest.gui.__start_game_hard__()
        AlienInvasionHardGUITest.gui.__choose_location__(1, AlienInvasionHardGUITest.gui.buttons[1])
        results=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(results,"Now choose a letter")

    def test__word_display_control_hard__(self):
        AlienInvasionHardGUITest.gui.__start_game_hard__()
        AlienInvasionHardGUITest.gui.__word_display_control_hard__()
        result=AlienInvasionHardGUITest.gui.game_page_progress_hard.cget("text")
        self.assertEqual(result,"Guesses remaining:7\nWord:")
    
    def test__take_guess__(self):
        AlienInvasionHardGUITest.gui.game.location=None
        AlienInvasionHardGUITest.gui.__start_game_hard__()
        AlienInvasionHardGUITest.gui.__take_guess__("A",AlienInvasionHardGUITest.gui.buttons[1])
        result=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(result,"No location chosen.")

        AlienInvasionHardGUITest.gui.game=AlienInvasionHard("HUSKY")
        AlienInvasionHardGUITest.gui.game.location=1     
        AlienInvasionHardGUITest.gui.__take_guess__("U",AlienInvasionHardGUITest.gui.buttons[1])
        result=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(result, "Correct! Guess again.")

        AlienInvasionHardGUITest.gui.game.location=1
        AlienInvasionHardGUITest.gui.__take_guess__("invalid",AlienInvasionHardGUITest.gui.buttons[2])
        result=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(result, "Invalid Guess! Try again.")

        AlienInvasionHardGUITest.gui.game.guesses=2
        AlienInvasionHardGUITest.gui.game.location=0
        AlienInvasionHardGUITest.gui.__take_guess__("Z",AlienInvasionHardGUITest.gui.buttons[3])
        result=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(result, "No Z in that location.")

        AlienInvasionHardGUITest.gui.game.location=3
        #guesses are 0 at this point
        AlienInvasionHardGUITest.gui.__take_guess__("X",AlienInvasionHardGUITest.gui.buttons[2])
        result=AlienInvasionHardGUITest.gui.game_page_results_hard.cget("text")
        self.assertEqual(result, "YOU LOST!")

        AlienInvasionHardGUITest.gui.__take_guess__("B",AlienInvasionHardGUITest.gui.buttons[2])
        self.assertEqual(result, "YOU LOST!")

        AlienInvasionHardGUITest.gui.__start_game_hard__()
        AlienInvasionHardGUITest.gui.game.player_word=AlienInvasionHardGUITest.gui.game.word

if __name__=='__main__':
    unittest.main()


