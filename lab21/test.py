"""
A unit test for wildcards

Run this test script to make sure everything is working properly.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:    October 29, 2026
"""
import introcs
import card


# This is to make sure we use isinstance correctly
class OtherCard(card.Card):
    """A do-nothing subclass of Card"""
    pass


def test_card_eq():
    """
    Tests that __eq__ works properly for WildCard.
    """
    print('Testing Card method __eq__')
    
    card1 = card.Card(1,12)
    introcs.assert_equals(card1,card1)
    
    card2 = OtherCard(1,12)
    introcs.assert_equals(card1,card2)
    
    color = introcs.RGB(255,0,0)
    introcs.assert_not_equals(card1,color)
    
    card3 = card.Card(2,12)
    introcs.assert_not_equals(card1,card3)
    introcs.assert_not_equals(card2,card3)
    
    card3 = card.Card(1,9)
    introcs.assert_not_equals(card1,card3)
    introcs.assert_not_equals(card2,card3)
    
    card3 = card.Card(2,8)
    introcs.assert_not_equals(card1,card3)
    introcs.assert_not_equals(card2,card3)


def test_card_lt():
    """
    Tests that __lt__ works properly for WildCard.
    """
    print('Testing Card method __lt__')

    card1 = card.Card(code='QD')
    card2 = card.Card(code='QS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)
    introcs.assert_false(card1<card1)
    introcs.assert_false(card2<card2)

    card1 = card.Card(code='JD')
    card2 = card.Card(code='QD')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)
    introcs.assert_false(card1<card1)
    introcs.assert_false(card2<card2)

    card1 = card.Card(code='2C')
    card2 = card.Card(code='AS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)
    introcs.assert_false(card1<card1)
    introcs.assert_false(card2<card2)

    card1 = card.Card(code='AD')
    card2 = card.Card(code='AH')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)
    introcs.assert_false(card1<card1)
    introcs.assert_false(card2<card2)


def test_card_deck():
    """
    Tests that the classmethod deck works properly for Card.
    """
    print('Testing Card method deck')
    
    deck1 = card.Card.deck()
    introcs.assert_equals(52,len(deck1))
    
    # Make sure we see all the cards
    found = {}
    for pick in deck1:
        found[pick.getCode()] = pick
    
    introcs.assert_equals(52,len(found))
    
    # This requires __eq__, __lt__ to be correct to work
    deck2 = card.Card.deck()
    deck2.sort()
    for pos in range(0,len(deck1)):
        introcs.assert_equals(deck2[pos],deck1[pos])
    
    pick = deck1[0]
    introcs.assert_equals(0,pick.getSuit())
    introcs.assert_equals(2,pick.getRank())
    
    pick = deck1[-2]
    introcs.assert_equals(2,pick.getSuit())
    introcs.assert_equals(1,pick.getRank())
    
    pick = deck1[-1]
    introcs.assert_equals(3,pick.getSuit())
    introcs.assert_equals(1,pick.getRank())


def test_wild_eq():
    """
    Tests that __eq__ works properly for WildCard.
    """
    print('Testing wild method __eq__')

    card1 = wild.WildCard(1,12)
    card2 = card.Card(1,12)
    introcs.assert_equals(card1,card1)
    introcs.assert_not_equals(card1,card2)

    card2 = wild.WildCard(1,12)
    introcs.assert_equals(card1,card1)

    card2 = wild.WildCard(1,12,'WC')
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(3,12)
    introcs.assert_not_equals(card1,card2)
    card2 = wild.WildCard(1,1)
    introcs.assert_not_equals(card1,card2)


def test_wild_lt():
    """
    Tests that __lt__ works properly for WildCard.
    """
    print('Testing wild method __lt__')

    card1 = wild.WildCard(code='QD')
    card2 = wild.WildCard(code='QS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='JD')
    card2 = wild.WildCard(code='QD')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card1 = wild.WildCard(code='2C')
    card2 = wild.WildCard(code='AS')
    introcs.assert_true(card1<card2)
    introcs.assert_false(card2<card1)

    card3 = wild.WildCard(code='WC')
    introcs.assert_true(card3<card2)
    introcs.assert_false(card2<card3)
    introcs.assert_true(card1<card3)
    introcs.assert_false(card3<card1)


# Script code
if __name__ == '__main__':
    test_card_eq()
    test_card_lt()
    
    # OPTIONALS. Uncomment the ones you complete
    #test_card_deck()
    #test_wild_eq()
    #test_wild_lt()

    print('The module wild passed all tests.')
