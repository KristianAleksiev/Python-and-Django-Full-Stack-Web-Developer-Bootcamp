# War Card Game
from random import shuffle


SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):

        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print()
        return drawn_card

    def remove_war_cards(self):

        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """Return True if player still has cards"""

        return len(self.hand.cards) != 0

### Game logic
print("Welcome to War, let's begin!")
#Create a deck, shuffle and split in half
deck = Deck()
deck.shuffle()
half_one, half_two = deck.split_in_half()

#Creating the players
computer = Player("computer", Hand(half_one))
name = input("What is your name?")
user = Player(name, Hand(half_two))

total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds +=1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(computer.name + " has the count: " + str(len(computer.hand.cards)))
    print("Play a card!")
    print()

    table_cards = []

    comp_card = computer.play_card()
    player_card = user.play_card()

    table_cards.append(comp_card)
    table_cards.append(player_card)

    if comp_card[1] == player_card[1]:
        war_count += 1

        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(comp_card[1]) < RANKS.index(player_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

    else:
        if RANKS.index(comp_card[1]) < RANKS.index(player_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)


print("Game over, number of rounds: "+str(total_rounds))
print("A war happend " + str(war_count) + " times")
print("Does the computer still have cards? ")
print(str(computer.still_has_cards()))
print("Does the player still have cards? ")
print(str(user.still_has_cards()))
