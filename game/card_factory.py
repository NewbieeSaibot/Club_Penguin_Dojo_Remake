from engine.card import Card
import pandas as pd

cards = pd.read_csv("./data/info/cards.csv")


class CardFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_card_by_id(card_id):
        card = Card(cards['name'][card_id], cards['element'][card_id], cards['force'][card_id],
                    cards['image_path'][card_id])

        return card
