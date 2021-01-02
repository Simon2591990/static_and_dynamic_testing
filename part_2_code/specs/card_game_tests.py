import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spades", 5)
        self.card2 = Card("Hearts", 7)
    
    def test_check_for_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self,self.card1))
    
    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 12", CardGame.cards_total(self, cards))