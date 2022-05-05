from collections import Counter


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return (f'{self.value} of {self.suit}')

    def __hash__(self):
        return hash((self.value, self.suit))


class CardHand:
    def __init__(self):
        self.counter = Counter()

    def put_card(self, card: Card):
        self.counter[card] += 1

    def get_card(self, card: Card):
        if card in self.counter:
            self.counter[card] -= 1
            return card
        raise ValueError("Card didn't found")

    def __contains__(self, item):
        return item in self.counter and self.counter[item] > 0

    def __len__(self):
        return sum([value for value in self.counter.values()])

    def __str__(self):
        if len(self) == 0:
            return "Card hand is empty"
        else:
            cards = [f'- {value}: {key}' for key, value in self.counter.items() if value > 0]
            lines = '\n'.join(cards)
            return f"Card hand: \n {lines}"


if __name__ == '__main__':
    card1 = Card(3, 'Hearts')
    card2 = Card(10, 'Spades')
    card3 = Card('Q', 'Clubs')
    hand1 = CardHand()
    print(hand1)
    hand1.put_card(card1)
    hand1.get_card(card1)
    print(hand1)
    hand1.put_card(card2)
    hand1.put_card(card3)
    hand1.put_card(card1)
    print(len(hand1))
    print(hand1.get_card(card2))
    print(card2 in hand1)
    print(len(hand1))
    print(hand1)
