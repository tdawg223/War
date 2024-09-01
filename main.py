import random
class Card:
  def __init__(self,suit, face):
    self.suit = suit
    self.face = face

  def __repr__(self):
    return f"{self.face} of {self.suit}"
 
  def __gt__(self, other):
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    return faces.index(self.face) > faces.index(other.face)

  def __eq__(self, other):
    return self.face == other.face
    


class Deck:
  def __init__(self):
    self.suits = ["Spades","Clubs","Diamonds","Hearts"]
    self.faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    self.cards = []
    for suit in self.suits:
      for face in self.faces:
        card = Card(suit, face)
        self.cards.append(card)
    #random.shuffle(self.deck)
    #return self.deck

  def shuffle_deck(self):
    random.shuffle(self.cards)
    return self.cards
    

  def __len__(self):
    return len(self.cards)

  def card_values(self):
    pass

class Player:
  def __init__(self,name):
    self.name = name
    self.side = []
    self.deck = []
    self.inplay = []
    


class War:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    deck = Deck()
    deck.shuffle_deck()
    self.player1.deck.extend(deck.cards[:26])
    self.player2.deck.extend(deck.cards[26:])

  def draw(self):
    if len(self.player1.deck) == 0:
      random.shuffle(self.player1.side)
      self.player1.deck.extend(self.player1.side)
      self.player1.side.clear()
      if len(self.player1.deck) == 0:
        if len(self.player1.inplay) == 0:
          print("Player 2 is the winner!")
        return self.player2
    if len(self.player2.deck) == 0:
      random.shuffle(self.player2.side)
      self.player2.deck.extend(self.player2.side)
      self.player2.side.clear()
      if len(self.player2.deck) == 0: 
        if len(self.player2.inplay) == 0:
          print("Player 1 is the winner!")
        return self.player1
    player1_draw = self.player1.deck.pop(0) # pops from top of the deck
    player2_draw = self.player2.deck.pop(0)
    self.player1.inplay.append(player1_draw)
    self.player2.inplay.append(player2_draw)
    
  
  def compare(self):
    if self.player1.inplay[-1] > self.player2.inplay[-1]:
      victor = self.player1

    elif self.player2.inplay[-1] > self.player1.inplay[-1]:
      victor = self.player2

    else:
      print("You have entered a war!")
      victor = self.battle()
    self.cleanup(victor)
    return victor
    
  def battle(self):
    #while self.player1.inplay[-1] == self.player2.inplay[-1]:
    for i in range(4):

        #print("?")
      self.draw() # This is where we left off
    print(self.player1.inplay)
    print(self.player2.inplay)
    return self.compare()
        

  def cleanup(self, winner):
    winner.side.extend(self.player1.inplay)
    winner.side.extend(self.player2.inplay)
    self.player1.inplay.clear()
    self.player2.inplay.clear()
    

  def turns(self):
    while True:
      input("Player 1 hit enter to  draw your card")
      print()
      input("Player 2 hit enter to  draw your card")
      print()
      no_more = self.draw()
      if no_more != None:
        break
        
      print("Player1 cards in play:", self.player1.inplay)
      print()
      print("Player2 cards in play:", self.player2.inplay)
      print()
      no_more = self.compare()
      #if no_more != None:
        #break
      # if len(self.player1.side) == 52:
      #   print("Congrats Player 1! You win!!")
      #   break
      # elif len(self.player2.side) == 52:
      #   print("Congrats Player 2! You win!!")
      #   break
      # else:

      print(
          "Player 1 cards left in deck:"
          , len(self.player1.deck)
        )
      print(
          "Player 1 winnings:"
          , len(self.player1.side)
        )
      print("Player 2 left in deck:", len(self.player2.deck))
      print("Player 2 winnings:", len(self.player2.side))
      print()
      
        
        
      
      
    


          
        
    
    
    

  

    


    



war = War(Player("Trevor"), Player("Roger"))
war.turns()

#war.player1.deck = [Card("Hearts", 3)] 
#war.player2.deck = [Card("Clubs", 3), Card("Spades", "Jack"), Card("diamonds", 6)]
#war.turns()
# war.draw()
# #print("Hello")
# war.compare()
# #print("c1")
# print(war.player1.inplay, war.player1.deck, war.player1.side)
# print(war.player2.inplay, war.player2.deck, war.player2.side)
# war.draw()
# war.compare()
# #print("c2")
# print(war.player1.inplay, war.player1.deck, war.player1.side)
# print(war.player2.inplay, war.player2.deck, war.player2.side)
#war.player1.deck = [Card("Diamonds","Ace")] , Card()



    


    