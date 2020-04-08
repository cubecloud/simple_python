from random import choice, shuffle
from termcolor import colored, cprint

def dprint(d,key_format = "\033[1;32m",value_format = "\033[1;34m"):
    for key in d.keys() :
        print (key_format, key, value_format, d[key])

class colortext:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

class Fool:

    def __init__(self, N):
        # кол-во игроков
        self.players_number = N

        # Состав деки
        # { индекс : [ карта(масть и ранг), статус в колоде - 1 из возможных {игрок 1-4, козырь в колоде (козырь),
        # колода, сброс, на столе (стол)}, вес (динамический, по умолчанию ранг карты)])
        # Изначально все карты в колоде и не видны игрокам

        self.deck = {1: ['П6', 'Колода', 6], 2: ['П7', 'Колода', 7], 3: ['П8', 'Колода', 8], 4: ['П9', 'Колода', 9],
                     5: ['П10', 'Колода', 10], 6: ['ПВ', 'Колода', 11], 7: ['ПД', 'Колода', 12],
                     8: ['ПК', 'Колода', 13], 9: ['ПТ', 'Колода', 14],
                     10: ['К6', 'Колода', 6], 11: ['К7', 'Колода', 7], 12: ['К8', 'Колода', 8], 13: ['К9', 'Колода', 9],
                     14: ['К10', 'Колода', 10], 15: ['КВ', 'Колода', 11], 16: ['КД', 'Колода', 12],
                     17: ['КК', 'Колода', 13], 18: ['КТ', 'Колода', 14],
                     19: ['Б6', 'Колода', 6], 20: ['Б7', 'Колода', 7], 21: ['Б8', 'Колода', 8], 22: ['Б9', 'Колода', 9],
                     23: ['Б10', 'Колода', 10], 24: ['БВ', 'Колода', 11], 25: ['БД', 'Колода', 12],
                     26: ['БК', 'Колода', 13], 27: ['БТ', 'Колода', 14],
                     28: ['Ч6', 'Колода', 6], 29: ['Ч7', 'Колода', 7], 30: ['Ч8', 'Колода', 8], 31: ['Ч9', 'Колода', 9],
                     32: ['Ч10', 'Колода', 10], 33: ['ЧВ', 'Колода', 11], 34: ['ЧД', 'Колода', 12],
                     35: ['ЧК', 'Колода', 13], 36: ['ЧТ', 'Колода', 14]}
        # Статусы
        # Колода - карта в колоде и не видна игрокам
        # Игрок № - карта у игрока № в руке
        # Сброс - карта в сбросе
        # Стол № - Карта от игрока № на столе
        # Козырь - карта открыта в качестве козыря'

        # cprint('\u2660', 'white','on_grey')
        # cprint('\u2663', 'white','on_grey')
        # cprint('\u2666', 'red','on_grey')
        # cprint('\u2665', 'red','on_grey')

        self.suits_names = {"П": "Пики", "К": "Крести", "Б": "Бубны", "Ч": "Черви"}
        self.suits_icons = {"П": '\u2660', "К": '\u2663', "Б": '\u2666', "Ч": '\u2665'}
        self.set_table()



    def show_all_cards(self):
        # self.show_card(self.current_card_index())
        self.show_player_cards(2)

        # deck_list =list()
        # for key in self.hidden_playing_deck_order:
        #      deck_list.append((self.playing_deck[key]))
        # print (deck_list)
        # print(self.hidden_playing_deck_order)

    def show_player_cards(self, p_number):
        cards_on_hand=1
        for card in self.players_decks_lists[p_number]:
            print(str(cards_on_hand)+'. '+self.show_card(card))
            cards_on_hand+=1
    def show_trump(self):
        pass

    def show_card(self, index):
        suit = self.what_suit(index)
        return str(self.playing_deck[index][0][1:])+str(self.suits_icons[self.what_suit(index)][0])
        # if (suit == 'П') or (suit == 'К'):
        #     # output = '{}{}'.format(self.playing_deck[index][0][1:],self.suits_icons[self.what_suit(index)][0])
        #     # print(colored(output, 'grey', 'on_white'))
        #     return str(self.playing_deck[index][0][1:])+str(self.suits_icons[self.what_suit(index)][0])
        # else:
        #     # output = '{}{}'.format(self.playing_deck[index][0][1:],self.suits_icons[self.what_suit(index)][0])
        #     # print(colored(output, 'red', 'on_white'))
        #     return str(self.playing_deck[index][0][1:])+str(self.suits_icons[self.what_suit(index)][0])

    def shuffle(self):
        self.playing_deck = self.deck
        # Это лист индексов колоды карт который отражает фактически колоду
        self.hidden_playing_deck_order = list(self.playing_deck.keys())
        # А теперь перемешанную колоду
        shuffle(self.hidden_playing_deck_order)

    # передаем индекс карты из списка self.hidden_playing_deck_order,
    # ссылаясь на индекс верхней карты колоды
    def current_card_index(self):
        return self.hidden_playing_deck_order[self.hidden_deck_index]

    # Получаем номер игрока, и статус карты для изменения
    def change_card_status(self, p_number, index, status):
        self.players_decks[p_number][index][1] = status

    def add_card_2discard_yard(self):
        for player_number in range(1, self.players_number + 1):
            # Убрать карту со стола (поменять статус стола и принадлежности на 'Сброс')
            # Добавим карту в свою базу знаний
            self.change_card_status(player_number, self.current_card_index, 'Сброс')

    # добавить карту в руку игрока
    def add_card_2player_hand(self, p_number):
        # Добавим карту в руку
        self.players_decks_lists[p_number].append(self.current_card_index())
        # Добавим карту в базу знаний игрока
        self.change_card_status(p_number, self.current_card_index(), 'Игрок ' + str(p_number))
        # Индекс карты в дек листе меняем на следующую карту
        self.hidden_deck_index += 1
        # print((self.players_decks[p_number][self.hidden_deck_index][1]))

    def what_suit(self, index):
        return self.playing_deck[index][0][0]

    def add_trump_card(self):
        for player_number in range(1, self.players_number + 1):
            # Поменять статус на 'Козырь')
            # Добавим карту в базу знаний игроков
            self.change_card_status(player_number, self.current_card_index(), 'Козырь')
        # self.what_suit(self.current_card_index())
        self.game_trump_char = self.playing_deck[self.current_card_index()][0][0]
        self.game_trump_name = self.suits_names[self.game_trump_char]
        # Индекс карты в дек листе меняем на следующую карту
        self.hidden_deck_index += 1

    def table_init(self):
        # Инициализируем словарь (массив) с деками игроков
        self.players_decks = dict()
        # Инициализируем словарь для листов с картами игроков, которые они знают (где находятся).
        self.players_decks_lists = dict()
        for player_number in range(1, self.players_number + 1):
            # заносим в словари деки игроков
            self.players_decks.update({player_number: self.playing_deck})
            # готовим словарь для внесения карт
            self.players_decks_lists.update({player_number: []})
        # устанавливаем индекс карты из колоды на 1
        # это индекс для ###### self.hidden_playing_deck_order ######
        self.hidden_deck_index = 1

    # Ввод имени
    def ask_for_name(self,p_number):
        print('Игрок', p_number,'введите имя =>')
        while True:
            try:
                player_name = str(input())
                break
            except (TypeError, ValueError):
                print("Неправильный ввод")
        return player_name


    def set_players(self):
        if self.players_number != 2:
            print ("НЕ ГОТОВО для более чем 2-х игроков")
            exit(1)
        else:
            self.player1_name = 'Computer'
            # self.player2_name = self.ask_for_name(2)
            self.player2_name = 'Dummy'

    def set_table(self):
        self.shuffle()
        self.table_init()
        self.set_players()
        # print(self.hidden_playing_deck_order)
        # раздача
        for i in range(6):
            for player_number in range(1, self.players_number + 1):
                # добавляем 1 карту каждому игроку
                self.add_card_2player_hand(player_number)
        self.add_trump_card()

    def show_table(self):
        self.show_all_cards()

    def show_cards(self, players=2):
        pass

    def ai_turn(self):
        pass

    def player_turn(self):
        pass


if __name__ == '__main__':
    fool_game = Fool(2)
    fool_game.show_table()

