"""
A module providing a class for playing cards with Jokers

This a continuation of the WildCard class from a previous lab. This lab
focuses on the double underscore methods.

Author: Walker White (wmw2)
Date:   October 29, 2026
"""
from functools import total_ordering  # for implementing comparisons in Python3
import card


# decorator "fills in" missing comparisons, at the cost of speed
@total_ordering
class WildCard(card.Card):
    """
    A class to represent a deck of cards with jokers.
    
    Most decks have two jokers: a red joker and a black joker.  We will not
    make a difference between these two jokers, since color does not matter
    during play.
    
    Jokers are wild cards, meaning that they can be turned into whatever card
    you want to turn them into.  This means that a Joker card can have a normal
    suit and rank (representing what we want to convert the joker to).  So we
    identify jokers with a new attribute wild (which has getters and setters).
    
    This class does not need to make any changes to the setters and getters 
    for suit and rank, as those attributes are unchanged.  However, the 
    introduction of Jokers does change the meaning of the setter/getter for 
    the codes. Jokers are represented by the two-character code 'WC'. Setting 
    a card with that code creates a Joker equivalent to the Ace of Spades.
    """
    ### HIDDEN INSTANCE ATTRIBUTES (In addition to those for Card):
    # Attribute _wild:  whether this card is a Joker 
    # Invariant: _wild is a bool
    
    # THESE METHODS ARE FROM LAB 20
    def isWild(self):
        """
        Returns True if this a Joker or wild card.
        """
        return self._wild
    
    def setWild(self, value):
        """
        Sets whether this is a Joker or wild card.
        
        The card will retain is suit and rank values no matter what happens
        to its wild status.
        
        Parameter value: Whether this is a Joker or wild card.
        Precondition: value is a bool
        """
        assert type(value) == bool
        self._wild = value
    
    # This is a DERIVED attribute (it is a combination of suit and rank)
    def getCode(self):
        """
        Returns a two-character code for the card.
        
        The code is a two-character string whose first character generally
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.
        
        All wild cards return the code 'WC' no matter what their suit or
        rank is.
        """
        return super().getCode()
    
    def setCode(self,value):
        """
        Sets the rank and suit of this card using a two-character code.
        
        The code should be a two-character string whose first character
        represents the rank and the second is the first initial of the
        suit.  Non-number ranks are represented by initials.  So '3H' stands
        for 3 of hearts, and 'KS' stands for king of spades).  We use 'T'
        for Ten.  All cards set this way are not jokers/wild.
        
        If the value is 'WC', this creates a joker/wild card that is
        equivalent to the Ace of Spades. Otherwise, the card is not wild.
        
        Parameter value: The code for the new rank and suit
        Precondition: value is a 2-char string that is either 'WC' or has
        value[0] in 'A23456789TJQK' and value[1] in 'CDHS'.
        """
        super().setCode(value)
    
    def __init__(self, suit=0, rank=1, code=None):
        """
        Initializes a card with given the suit and rank.
        
        The suits and rank are represented as integers. Alternatively,
        suit and rank can be encoded together in a two-character string like
        '3H' (3 of hearts) or 'KS' (king of spades). We use 'T' for Ten.
        The code 'WC' indicates a joker. All jokers are equivalent to the Ace 
        of Spades as far as rank and suit are required,
        
        The possible suits are given in SUIT_NAMES, while the possible ranks
        are given in RANK_NAMES. There is no rank 0.
        
        Example: if we execute c = WildCard(0, 12), then this card is the Queen 
        of Clubs, since SUIT_NAMES[0] is 'Clubs' and RANK_NAMES[12] is 'Queen'. 
        The same card could be created by WildCard(code='QC'). However, the 
        card WildCard(0,12,'WC') is the Ace of Spades.
        
        Parameter suit: the suit encoding (optional)
        Precondition: suit is an int in 0..len(SUIT_NAMES)-1 (inclusive)
        
        Parameter rank: the rank encoding (optional)
        Precondition: rank is an int in 1..len(RANK_NAMES)-1 (inclusive)
        
        Parameter code: the card encoded as a string (optional)
        Precondition: code is a 2-char string that is either 'WC' or has
        code[0] in 'A23456789TJQK' and code[1] in 'CDHS'
        """
        if code == 'WC':
            super().__init__(code='AS')
            self.setWild(True)
        else:
            super().__init__(suit, rank, code)
            self.setWild(False)
    
    def __str__(self):
        """
        Returns a readable string representation of this card.
        
        If this card is a Joker, the indicator '[WILD]' appears after the name.
        Otherwise, the result is the same as for the Card class.
        
        Example: '2 of Hearts [WILD]'
        """
        result = super().__str__()
        if self.isWild():
            result += ' [WILD]'
        return result
    
    # THESE ARE FOR THE CURRENT LAB
    def __eq__(self, other):
        """
        Returns True if other is an equivalent card; False otherwise
        
        It is not enough for two cards to share the same suit and rank to
        be equal.  They must either both be wild or neither wild.
        
        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        if not isinstance(other, WildCard):
            return False
        if other.getSuit() != self.getSuit():
            return False
        if other.getRank() != self.getRank():
            return False
        if other.isWild() != self.isWild():
            return False
        return True
    
    def __lt__(self, other):
        """
        Returns: True if this card is less than other
        
        Cards are compared according to poker ordering, with Aces high. In the
        case of ties, wild cards are worth LESS than the natural cards.
        
        Parameter other: the value to compare
        Precondition: other is a Card
        """
        if not isinstance(other, card.Card):
            return False

        other_rank = other.getRank()
        self_rank = self.getRank()

        if self_rank == 1:
            self_value = 13
        else:
            self_value = self_rank

        if other_rank == 1:
            other_value = 13
        else:
            other_value = other_rank

        if self_value != other_value:
            return self_value < other_value

        if isinstance(other, WildCard):
            if other.isWild():
                other_is_wild = True
            else:
                other_is_wild = False
        else:
            other_is_wild = False

        self_is_wild = self.isWild()
        
        if self_is_wild and not other_is_wild:
            return True
        else:
            return False
        
