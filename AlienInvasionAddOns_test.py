import unittest
from AlienInvasion_Game import AlienInvasionAddOns
class AlienInvasionAddOnsTest(unittest.TestCase):
    gui=AlienInvasionAddOns()
    def test__init__(self):
        result=AlienInvasionAddOnsTest.gui.hints
        expected={"HUSKY":"#LikeA_____","PYTHON":"The best programming language!","CAT":"Has nine lives!","DOG":"Woof!","TEA":"White, green, oolong, and black","ROCK":"Spongebob's bestfriend's house."
                    ,"BINARY":"10010=18","LAMP":"Provides light.","BALLONS":"Great party decor!","APPLE":"Hit sir Issac Newton.","LAPTOP":"Portable computer."}
        self.assertEqual(result,expected)

    def test__reveal_hint__(self):
        AlienInvasionAddOnsTest.gui.__start_game__()
        AlienInvasionAddOnsTest.gui.game.word="HUSKY"
        AlienInvasionAddOnsTest.gui.__reveal_hint__()
        result=AlienInvasionAddOnsTest.gui.hint
        self.assertEqual(result,"#LikeA_____")

    def test__start_game__(self, friend=None,word=None):
        """This method is called when either start easy or start easy with a friend is clicked. If easy with a friend is clicked 
        Arguements:
            friend: True if friend mode is enabled, None if playing alone
            word: 6 letter string or None
        """
        AlienInvasionAddOnsTest.gui.__start_game__(friend=1,word="friend")
        result=AlienInvasionAddOnsTest.gui.game.word
        self.assertEqual(result,"friend")

if __name__=='__main__':
    unittest.main()


