import sys
import unittest
from fool_sketch import Table, Deck

class TestTable(unittest.TestCase):

    def setUp(self):
        self.game = Table(4)
        print()
        print('Start test!')
        pass

    def tearDown(self):
        print()
        print(f'Test completed!')

    # Проверка инициализации начальных параметров
    def test_init(self):
        self.assertEqual(self.game.winner, 0)
        self.assertEqual(self.game.looser, 0)
        self.assertEqual(self.game.players_number, 4)
        self.assertEqual(self.game.playing_deck, Deck.player_deck)
        self.assertEqual(self.game.desktop_list, list())
        self.assertFalse(self.game.end_of_deck)
        self.assertEqual(self.game.action, '')
        self.assertEqual(self.game.result, 0)
        self.assertEqual(self.game.players_numbers_lst,[1, 2, 3, 4])


    # Проверка создания копий дек для каждого игрока
    # Разные объекты но размер один
    def test_set_players(self):
        self.game.set_players()
        self.assertNotEqual(self.game.pl[1],self.game.pl[self.game.next_player(2)])
        self.assertNotEqual(self.game.pl[2],self.game.pl[self.game.next_player(3)])
        self.assertNotEqual(self.game.pl[3],self.game.pl[self.game.next_player(4)])
        self.assertEqual(sys.getsizeof(self.game.pl[1]),sys.getsizeof(self.game.pl[self.game.next_player(2)]))
        self.assertEqual(sys.getsizeof(self.game.pl[2]),sys.getsizeof(self.game.pl[self.game.next_player(3)]))
        self.assertEqual(sys.getsizeof(self.game.pl[3]),sys.getsizeof(self.game.pl[self.game.next_player(4)]))

    # Проверка премешиваемости колоды
    def test_shuffle(self):
        self.game.hidden_playing_deck_order = list(self.game.playing_deck.keys())
        old_hidden_playing_deck_order = self.game.hidden_playing_deck_order
        self.game.shuffle()
        self.assertNotEqual(self.game.hidden_playing_deck_order, old_hidden_playing_deck_order)

    # Проверка того, что колоды в самом начале одинаковы и индекс 1-ой карты сброшен
    def test_table_init(self):
        self.game.set_players()
        self.game.shuffle()
        self.game.table_init()
        self.assertEqual(self.game.hidden_deck_index, 0)
        self.assertEqual(self.game.playing_deck, self.game.pl[1].player_deck)
        self.assertEqual(self.game.playing_deck, self.game.pl[2].player_deck)
        self.assertEqual(self.game.playing_deck, self.game.pl[3].player_deck)
        self.assertEqual(self.game.playing_deck, self.game.pl[4].player_deck)


    # Проверка раздачи карт на руки и того, что они у каждого игрока разные
    # Проверка козыря и того, что козырь перенесен в конец колоды
    # Проверка того, что каждый раз выбирается для 1-ого хода один и тот-же игрок, при одном перемешивании
    def test_set_table(self):
        self.game.set_players()
        self.game.shuffle()
        self.game.table_init()
        for i in range(6):
            for player_number in self.game.players_numbers_lst:
                # добавляем 1 карту каждому игроку
                self.game.add_card_2player_hand(player_number)
        for player_number in self.game.players_numbers_lst:
            self.assertNotIn(self.game.pl[player_number].player_cards_onhand_list, self.game.pl[
                self.game.next_player(player_number)].player_cards_onhand_list)

        self.game.add_trump_card()
        # Проверяем что карта козыря перенесена в конец колоды.
        self.assertEqual(self.game.trump_index, self.game.hidden_playing_deck_order[
            len(self.game.hidden_playing_deck_order) - 1])
        for player_number in self.game.players_numbers_lst:
            self.assertEqual(self.game.pl[player_number].trump_index,self.game.trump_index)
        self.game.show_first_turn_card()
        checkplayer_1, checkindex_1 = self.game.first_turn_choice()
        checkplayer_2, checkindex_2 = self.game.first_turn_choice()
        self.assertEqual(self.game.player_turn, checkplayer_1)
        self.assertEqual(checkplayer_1, checkplayer_2)
        self.assertEqual(checkindex_1, checkindex_2)

