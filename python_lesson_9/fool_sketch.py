from random import choice, shuffle

class Fool:

    def __init__(self, N):
        # кол-во игроков
        self.players_number = N

        # Состав деки
        # { индекс : [ карта(масть и ранг), статус в колоде - 1 из возможных {игрок 1-4, козырь в колоде (козырь), колода, 
        # сброс, на столе (стол)}, вес (динамический, по умолчанию ранг карты)]) 
        self.deck = {1: ['П6', 'Колода', 6], 2: ['П7', 'Колода', 7], 3: ['П8', 'Колода', 8], 4: ['П9', 'Колода', 9],
                     5: ['П10', 'Колода', 10], 6: ['ПВ', 'Колода', 11], 7: ['ПД', 'Колода', 12],
                     8: ['ПК', 'Колода', 13], 9: ['ПТ', 'Колода', 14],
                     10: ['К6', 'Колода', 6], 11: ['К7', 'Колода', 7], 12: ['К8', 'Колода', 8], 13: ['К9', 'Колода', 9],
                     14: ['К10', 'Колода', 10], 15: ['КВ', 'Колода', 11], 16: ['КД', 'Колода', 12],
                     17: ['КК', 'Колода', 13], 18: ['КТ', 'Колода', 14],
                     19: ['Б6', 'Колода', 6], 20: ['Б7', 'Колода', 7], 21: ['Б8', 'Колода', 8], 22: ['Б9', 'Колода', 9],
                     23: ['Б10', 'Колода', 10], 24: ['БВ', 'Колода', 11], 25: ['БД', 'Колода', 12],
                     26: ['БК', 'Колода', 13], 27: ['БТ', 'Колода', 14],
                     28: ['Б6', 'Колода', 6], 29: ['Б7', 'Колода', 7], 30: ['Б8', 'Колода', 8], 31: ['Б9', 'Колода', 9],
                     32: ['Б10', 'Колода', 10], 33: ['БВ', 'Колода', 11], 34: ['БД', 'Колода', 12],
                     35: ['БК', 'Колода', 13], 36: ['БТ', 'Колода', 14]}
        # Статусы
        # Колода - карта в колоде и не видна игрокам
        # Игрок № - карта у игрока № в руке
        # Сброс - карта в сбросе
        # Стол № - Карта от игрока № на столе
        # Козырь - карта открыта в качестве козыря
        #
    def show_all_cards(self):
        deck_list =list()
        for key in self.hidden_playing_deck_order:
             deck_list.append((self.playing_deck[key]))
        # print (deck_list)
        # print(self.hidden_playing_deck_order)

    def shuffle (self):
        self.playing_deck = self.deck
        self.hidden_playing_deck_order = list(self.playing_deck.keys())
        shuffle(self.hidden_playing_deck_order)

    def change_card_status(self,p_number,card_index, status):
        self.players_decks[p_number][card_index][1] = status

    # добавить карту в руку игрока
    def add_card_2player_hand(self, p_number):
        # Добавим карту в руку
        self.players_decks_lists[p_number].append(self.hidden_playing_deck_order[self.hidden_deck_index])
        # Добавим карту в свою базу знаний
        # self.players_decks[p_number]:[1][2]]='Игрок'+str(p_number)
        self.change_card_status (p_number,self.hidden_deck_index,)
        print((self.players_decks[p_number][self.hidden_deck_index][1]))

    def board_init (self):
        # Инициализируем словарь (массив) с деками игроков
        self.players_decks=dict()
        # Инициализируем словарь для листов с картами игроков, которые они знают (где находятся).
        self.players_decks_lists= dict()
        for player_number in range(1, self.players_number+1):
            # заносим в словари деки игроков
            self.players_decks.update({player_number: self.playing_deck})
            # готовим словарь для внесения карт
            self.players_decks_lists.update({player_number:[]})
        self.hidden_deck_index=1

    def add_trump_card(self):
        pass

    def set_the_board(self):
        self.board_init ()
        # print(self.hidden_playing_deck_order)
        for card in range(6):
            # Индекс карты в дек листе.
            for player_number in range(1, self.players_number+1):
                # print(player_number)
                self.add_card_2player_hand(player_number)
                self.hidden_deck_index+=1

        # self.add_trump_card (self, card_index)



    def show_cards(self,players=2):
        pass
    def ai_turn (self):
        pass
    def player_turn (self):
        pass

if __name__ == '__main__':
    fool_game = Fool(2)
    fool_game.shuffle()
    fool_game.show_all_cards()
    fool_game.set_the_board()