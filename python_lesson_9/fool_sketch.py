from random import choice, shuffle
import copy
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
        self.player_types = {1: 'Human', 2: 'Computer'}
        self.player_type = self.player_types[player_type]
        # если человек то запрашиваем имя
        if self.player_type == self.player_types[1]:
            self.player_name = self.player_types[player_type]
            # self.ask_for_name(self.player_number)
        else:
            self.player_name = 'Computer ' + str(self.player_number)
        self.player_cards_onhand_list = list()
        self.suit_range={'П':(1,10),'К':(10,19),'Б':(19,28),'Ч':(28,37)}

    def change_card_status(self, index, status):
        self.player_deck[index][1] = status
        # print(index)
        # print(self.player_deck)

    def change_card_weight (self, index, new_weight):
        self.player_deck[index][2] = new_weight

    def get_card_weight(self,index):
        return self.player_deck[index][2]

    def add_card_weight(self, index, add_weight):
        return self.change_card_weight(index, self.get_card_weight(index)+add_weight)

    def add_weight_2suit(self, suit_char, add_weight):
        for index in range (self.suit_range[suit_char][0],self.suit_range[suit_char][1]):
            self.add_card_weight  (index, add_weight)
            # print(self.player_deck[index])

    # возвращает из руки карту с наименьшим индексом
    def lowest_from_hand(self):
        return min(self.player_cards_onhand_list)

    # возвращает из руки _козырную_ карту с наименьшим индексом
    def lowest_trump_from_hand(self):
        try:
            temp = min(self.trumps_from_hand())
            return temp
        except  (ValueError):
            temp=[]
            return temp


    # возвращает List из козырных карт в руке
    def trumps_from_hand(self):
        trumps_onhand=[]
        for index in self.player_cards_onhand_list:
            if index in self.trump_range:
                trumps_onhand.append(index)
        return trumps_onhand

    def what_suit(self, index):
        return self.player_deck[index][0][0]

    def get_card(self, index):
        # print(index)
        self.player_cards_onhand_list.append(index)
        self.change_card_status(index, 'Игрок ' + str(self.player_number))
        # print('Лист',self.player_cards_onhand_list)
        # print('Дека',self.player_deck)


    def set_trump (self, index):
        self.trump_index = index
        self.trump_char = self.player_deck[index][0][0]
        self.change_card_status(index, 'Козырь')
        self.add_weight_2suit(self.what_suit(index),100)
        # print ('index', self.trump_index)
        # print ('char', self.trump_char)
        # print ('Range', self.suit_range[self.trump_char][0], self.suit_range[self.trump_char][1])
        self.trump_range = range(self.suit_range[self.trump_char][0], self.suit_range[self.trump_char][1])
        # print('Козырь', self.what_suit(index))

    def get_deck(self, player_deck):
        self.player_deck= copy.deepcopy(player_deck)

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
            self.pl[player_number].change_card_status(self.current_card_index, 'Сброс')

    # добавить карту в руку игрока
    def add_card_2player_hand(self, p_number):
        # Добавим карту в руку игрока
        self.pl[p_number].get_card(self.current_card_index())
        # Индекс карты в дек листе меняем на следующую карту
        self.hidden_deck_index += 1
        # print((self.players_decks[p_number][self.current_card_index()][1]))

    def what_suit(self, index):
        return self.playing_deck[index][0][0]

    def add_trump_card(self):
        for player_number in range(1, self.players_number + 1):
            # Поменять статус на 'Козырь')
            # Добавим карту в базу знаний всех игроков
            self.pl[player_number].change_card_status (self.current_card_index(), 'Козырь')
            # Сделать с индексом козыря (в деке по этому номеру лежит последняя козырная карта в колоде)
            self.pl[player_number].set_trump(self.current_card_index())

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
            print('Игрок',player_number, self.show_cards_list(self.pl[player_number].trumps_from_hand()))
            min_card_index[player_number] = self.pl[player_number].lowest_trump_from_hand()
        # Пробуем операцию мин
        try:
            min_card_player =  min(min_card_index.keys(), key=(lambda k: min_card_index[k]))
            print (f'Минимальная карта у игрока {min_card_player}, это карта', self.show_card(min_card_index[min_card_player]))
            return min_card_player
        except (TypeError, ValueError):
            check_player=0
            check_card=0
            for player_number in range (1, self.players_number + 1):
                print ('мин кард индекс', min_card_index[player_number])
                if min_card_index[player_number] == []:
                    continue
                elif min_card_index[player_number] > check_card:
                    check_card=min_card_index[player_number]
                    check_player=player_number
            if check_card !=None:
                min_card_player=check_player
            else:
                for playerNumber1 in range (1, self.players_number + 1):
                    print('Игрок',playerNumber1, self.show_cards_list(self.pl[playerNumber1].player_cards_onhand_list))
                    min_card_index[playerNumber1] = self.pl[playerNumber1].lowest_from_hand()
                min_card_player = (min(min_card_index.items(), key=lambda x: x[1])[0])

        print(min_card_index)
        print (f'Минимальная карта у игрока {min_card_player}, это карта', self.show_card(min_card_index[min_card_player]))
        return min_card_player

        # for player_number in range (1, self.players_number + 1):
        #     if player_number+1>self.players_number:
        #         break
        #     if min_card_index[player_number] > min_card_index[player_number+1]:
        #         min_card_player = player_number
        #     elif (min_card_index[player_number] == min_card_index[player_number+1]):
        #         for playerNumber1 in range (1, self.players_number + 1):
        #             print('Игрок',playerNumber1, self.show_cards_list(self.pl[playerNumber1].player_cards_onhand_list))
        #             min_card_index[playerNumber1] = self.pl[playerNumber1].lowest_from_hand()
        #         min_card_player = (min(min_card_index.items(), key=lambda x: x[1])[0])
        #     else:
        #         min_card_player=playerNumber1+1
        #     for player_number in range (1, self.players_number + 1):
        #         print('Игрок',player_number, self.show_cards_list(self.pl[player_number].player_cards_onhand_list))
        #         min_card_index[player_number] = self.pl[player_number].lowest_from_hand()
        # min_card_player = (min(min_card_index.items(), key=lambda x: x[1])[0])
        # min_card_player =  min(min_card_index.keys(), key=(lambda k: min_card_index[k]))


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
        for card in self.pl[p_number].player_cards_onhand_list:
            print(f'{cards_on_hand}. '+self.show_card(card))
            cards_on_hand+=1


    def show_all_cards(self):
        self.show_player_cards(2)
        self.show_trump()


    def show_table(self):
        self.game_turn = 1
        self.show_all_cards()


    # Устанавливаеv кол-во игроков
    def set_players(self):
        self.pl =dict()
        if self.players_number != 2:
            print ("НЕ ГОТОВО для более чем 2-х игроков")
            exit(1)
        else:
            # Иницианилизируем работу класса игроков и делаем их словарем
            self.pl[1]= Player(1,1)
            self.pl[2]= Player(2,2)


    # Инициализируем словарь (массив) с деками игроков
    def table_init(self):
        for player_number in range(1, self.players_number + 1):
            # заносим в словари деки игроков
            self.pl[player_number].get_deck(self.playing_deck)

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

