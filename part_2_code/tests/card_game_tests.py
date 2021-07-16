import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = CardGame()
        self.card1 = Card("Clubs",1)
        self.card2 = Card("Diamonds",3)
        self.card3 = Card("Hearts",7)
        self.card4 = Card("Clubs", 4)
        self.all_cards = (self.card1,self.card2,self.card3,self.card4)
        



    def test_check_for_ace(self):
        result = self.card.check_for_ace(self.card1)
        self.assertTrue(result)
        
    
       


    def test_highest_card(self):
        result = self.card.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2,result)
        
        
          

    def test_cards_total(self): 
        total = self.card.cards_total(self.all_cards)
        self.assertEqual=('You have a total of', total)
        






        


    