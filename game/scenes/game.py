from engine.scene import Scene
from engine.player import Player, mutex
from engine.render_able_object import RenderAbleObject

import game.globals as gl
from game.card_factory import CardFactory

from threading import Thread
from time import sleep
import random


class Game(Scene):
    def __init__(self):
        super().__init__()
        self.background = "./game/data/images/backgrounds/empty_dojo.png"
        self.time = 0
        self.start = 1
        self.player = None
        self.player2 = None
        self.game_loo = None
        self.stop_thread = False
        self.score = 0
        self.round = 0
        self.round_time = 1

    def initialize_game(self):
        player = Player()
        player2 = Player()
        player2.ai = True
        for i in range(20):
            card = CardFactory.get_card_by_id(i)
            card.player = player
            card.interact_able = True
            player.deck.append(card)
            card2 = CardFactory.get_card_by_id(i)
            card2.visible = False
            player2.deck.append(card2)

        player.shuffle_deck()
        player.take_cards(3)
        self.objects.append(player)

        for i in range(len(player.hand)):
            player.hand[i].current_pos[0] = 300 + 150 * i
            player.hand[i].current_pos[1] = 400

        player2.shuffle_deck()
        player2.take_cards(3)
        self.objects.append(player2)
        self.player = player
        self.player2 = player2
        self.game_loo = Thread(target=self.game_loop)
        self.game_loo.start()

    def game_loop(self):
        while True:
            if self.stop_thread:
                sleep(2)
                gl.active_scene = 0
                break
            sleep(1)
            self.time += 1
            if self.time == self.round_time:
                self.time = 0
                self.round += 1
                self.game_logic()

    def game_logic(self):
        if self.round == 1:
            pass

        for i in range(len(self.player.hand)):
            self.player.hand[i].current_pos[0] = 300 + 150 * i
            self.player.hand[i].current_pos[1] = 400

        # Be sure that player has any selected card, selecting a random card if select card is None
        if self.player.selected_card is None:
            self.player.selected_card = self.player.hand[random.randint(0, len(self.player.hand)-1)]

        self.player2.selected_card = self.player2.hand[random.randint(0, len(self.player.hand)-1)]

        # re pos the selected cards to the center of dojo
        self.player.selected_card.current_pos[0] = 350
        self.player.selected_card.current_pos[1] = 200

        self.player2.selected_card.visible = True
        self.player2.selected_card.current_pos[0] = 550
        self.player2.selected_card.current_pos[1] = 200

        # Now we can run the logic of the selected cards.

        extra_force = {
            "Water": {"Water": 0, "Fire": 3, "Snow": 0},
            "Fire": {"Water": 0, "Fire": 0, "Snow": 3},
            "Snow": {"Water": 3, "Fire": 0, "Snow": 0},
        }

        current_force_player1_card = self.player.selected_card.force
        current_force_player2_card = self.player2.selected_card.force

        current_force_player1_card += extra_force[self.player.selected_card.type][self.player2.selected_card.type]
        current_force_player2_card += extra_force[self.player2.selected_card.type][self.player.selected_card.type]

        # Who won the round?
        round_text = RenderAbleObject(x=320, y=0, height=200, width=400)
        self.objects.append(round_text)
        round_text.visible = False
        if current_force_player1_card > current_force_player2_card:
            self.score += 1
            round_text.image_path = "./game/data/images/game/player_1_won_round.png"
        elif current_force_player1_card < current_force_player2_card:
            self.score -= 1
            round_text.image_path = "./game/data/images/game/player_2_won_round.png"
        else:
            round_text.image_path = "./game/data/images/game/draw.png"

        round_text.visible = True
        sleep(2)
        round_text.visible = False

        mutex.acquire()
        self.player.hand.remove(self.player.selected_card)
        self.player2.hand.remove(self.player2.selected_card)
        mutex.release()
        del self.player.selected_card
        del self.player2.selected_card
        self.player.selected_card = None
        self.player2.selected_card = None

        empty = not(self.player.take_cards(1) and self.player2.take_cards(1))

        for i in range(len(self.player.hand)):
            self.player.hand[i].current_pos[0] = 300 + 150 * i
            self.player.hand[i].current_pos[1] = 400

        if empty:
            self.stop_game()

    def stop_game(self):
        self.stop_thread = True
        final_text = RenderAbleObject(x=350, y=100, height=200, width=400)
        self.objects.append(final_text)
        if self.score > 0:
            final_text.image_path = "./game/data/images/game/player_1_won_game.png"
        elif self.score < 0:
            final_text.image_path = "./game/data/images/game/player_2_won_game.png"
        else:
            final_text.image_path = "./game/data/images/game/draw.png"
