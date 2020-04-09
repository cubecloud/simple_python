from random import choice, shuffle
from termcolor import colored, cprint

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
    red_on_white = '\033[1;31;40m'
    white_on_gray = '\033[1;30;47m'
    gray_on_white = '\033[1;90;40m'

class Player:
    def __init__(self, N, player_type):
        self.player_number = N
        self.player_types = {1:'Human', 2:'Computer'}
        self.player_type = self.player_types[player_type]
        # если человек то запрашиваем имя
        if self.player_type == self.player_types[1]:
            self.player_name = self.player_types[player_type]
                # self.ask_for_name(self.player_number)
        else:
            self.player_name ='Computer '+str(self.player_number)
        self.player_cards_onhand_list = list()

    def change_card_status(self, index, status):
        self.player_deck[self.player_number][index][1] = status

    def get_card (self, index):
        self.player_cards_onhand_list = self.player_deck_list.append(index)
        self.change_card_status(index, 'Игрок '+ str(self.player_number))

    def set_trump (self, index):
        self.change_card_status(index, 'Козырь')

    def get_deck(self, player_deck):
        self.player_deck=player_deck
        # print(self.player_deck)
    def ask_for_name(self):
        print('Игрок', self.player_number,'введите имя =>')
        while True:
            try:
                self.player_name = str(input())
                break
            except (TypeError, ValueError):
                print("Неправильный ввод")
class Dealer:

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

        self.suits_names = {"П": "Пики", "К": "Крести", "Б": "Бубны", "Ч": "Черви"}
        self.suits_icons = {"П": '\u2660', "К": '\u2663', "Б": '\u2666', "Ч": '\u2665'}



    def show_cards_list(self,deck_list):
        cards_list_str=str()
        for card in deck_list:
            cards_list_str += self.show_card(card)+' '
        return cards_list_str


    # передаем индекс карты из списка self.hidden_playing_deck_order,
    # ссылаясь на индекс верхней карты колоды
    def current_card_index(self):
        # print (self.hidden_playing_deck_order[self.hidden_deck_index])
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
        # print("раздача карты")
        self.players_decks_lists[p_number].append(self.current_card_index())
        # Добавим карту в базу знаний игрока
        self.change_card_status(p_number, self.current_card_index(), 'Игрок ' + str(p_number))
        # print(self.players_decks[p_number])
        # print((self.players_decks[p_number][self.current_card_index()]))
        # Индекс карты в дек листе меняем на следующую карту
        self.hidden_deck_index += 1
        # print((self.players_decks[p_number][self.current_card_index()][1]))

    def what_suit(self, index):
        return self.playing_deck[index][0][0]

    def add_trump_card(self):
        for player_number in range(1, self.players_number + 1):
            # Поменять статус на 'Козырь')
            # Добавим карту в базу знаний всех игроков
            self.change_card_status(player_number, self.current_card_index(), 'Козырь')
        # Сделать с индексом козыря (в деке по этому номеру лежит последняя козырная карта в колоде)
        self.trump_index = self.current_card_index()
        # перенести в скрытом листе, открытого козыря последним в список, перемешанной деки
        # чтобы он был последним
        self.hidden_playing_deck_order.remove(self.trump_index)
        self.hidden_playing_deck_order.append(self.trump_index)
        # Индекс карты в дек листе меняем на следующую карту
        self.hidden_deck_index += 1

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

    def first_turn_choice(self):
        print ("Идет выбор ходящего первым")
        min_card_index =dict()
        for player_number in range (1, self.players_number + 1):
            print('Игрок',player_number, self.show_cards_list(self.players_decks_lists[player_number]))
            min_card_index[player_number] = min([card for card in self.players_decks_lists[player_number]])
        min_card_player = (min(min_card_index.items(), key=lambda x: x[1])[0])
        print ('Минимальная карта у игрока', min_card_player, 'это карта', self.show_card(min_card_index[min_card_player]))
        # Почему-то лямбда не работает в этом случае, как положено - иногда ошибается. Оставил показать.
        # print(self.players_decks_lists)
        # key_min=min(self.players_decks_lists.keys(), key=(lambda k: self.players_decks_lists[k]))
        # print('Первым ходит игрок', key_min)
        return min_card_player

    def show_card(self, index):
        suit = self.what_suit(index)
        # Пока не удалось решить проблему с выводом цветного текста сразу из переменной словаря
        # Делаем проверку и присваиваем цвет через print(f'{переменная}'
        if (suit == 'П') or (suit == 'К'):
            color = colortext.gray_on_white
        else:
            color = colortext.red_on_white
        output = f'{color}' + str(self.playing_deck[index][0][1:]) + f'{color}' + str(
            self.suits_icons[self.what_suit(index)][0:]) + f'{colortext.end}'
        return output


    def show_trump(self):
        print()
        # print (self.trump_index)
        print('Козырь: ' +self.show_card(self.trump_index))
        print('В колоде карт: ' + str(36 - self.hidden_deck_index))
        # print (self.show_card[self.trump_index])
        # print('Козырь:' + self.show_card(self.playing_deck[self.trump_index][0][0:]))


    def show_player_cards(self, p_number):
        cards_on_hand=1
        for card in self.players_decks_lists[p_number]:
            print(f'{cards_on_hand}. '+self.show_card(card))
            cards_on_hand+=1


    def show_all_cards(self):
        self.show_player_cards(2)
        self.show_trump()

    def show_table(self):
        self.game_turn = 1
        self.show_all_cards()


    # Устанавливаем кол-во игроков и их типы
    def set_players(self):
        self.pl =dict()
        if self.players_number != 2:
            print ("НЕ ГОТОВО для более чем 2-х игроков")
            exit(1)
        else:
            self.pl[1]=Player(1,1)
            self.pl[2]=Player(2,2)


    # Инициализируем словарь (массив) с деками игроков
    def table_init(self):

        self.players_decks = dict()
        # Инициализируем словарь для листов с картами игроков, которые они знают (где находятся).
        self.players_decks_lists = dict()

        for player_number in range(1, self.players_number + 1):
            # заносим в словари деки игроков
            self.pl[player_number].get_deck(self.deck)

            self.players_decks.update({player_number: self.playing_deck})
            # готовим словарь для внесения карт
            self.players_decks_lists.update({player_number: []})

        # устанавливаем индекс карты из колоды на 1
        # это индекс для ###### self.hidden_playing_deck_order ######
        self.hidden_deck_index = 1


    # мешаем колоду
    def shuffle(self):
        self.playing_deck = self.deck
        # Это лист индексов колоды карт который отражает фактически колоду
        self.hidden_playing_deck_order = list(self.playing_deck.keys())
        # А теперь перемешанную колоду
        shuffle(self.hidden_playing_deck_order)

    def set_table(self):
        self.set_players()
        self.shuffle()
        self.table_init()
        # print(self.hidden_playing_deck_order)
        # раздача
        for i in range(6):
            for player_number in range(1, self.players_number + 1):
                # добавляем 1 карту каждому игроку
                self.add_card_2player_hand(player_number)
        self.add_trump_card()
        self.player_turn = self.first_turn_choice()

# Основное тело, перенести потом в инит часть логики
if __name__ == '__main__':
    fool_game = Dealer(2)
    fool_game.set_table()
    fool_game.show_table()

