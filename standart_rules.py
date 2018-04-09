from abc import ABCMeta, abstractmethod

from copy import deepcopy


class StandRules(metaclass=ABCMeta):
    limit = 10

    def __init__(self, numb_of_holes, player_list):
        self._counter_for_holes = 1
        self._counter_for_peoples = 1
        self.finished = False
        self._numb_of_holes = numb_of_holes
        self._player_list = player_list
        self._count_of_people = len(player_list)
        self._create_table(self._create_name_list(player_list))
        self._current_list = [0] * self._count_of_people
        self._list_of_turn = [False] * self._count_of_people
        self._empty_list = [None] * self._count_of_people

    def _create_name_list(self, player_list):
        name_list = []
        for i in range(self._count_of_people):
            name_list.append(player_list[i]._name)
        return name_list

    def _create_table(self, player_list):
        self.table = []
        '''(self.table.append([]) for i in range(0,self._numb_of_holes+1))
        print(self.table)
        ((self.table[i].append([None]*self._count_of_people)) for i in range(0,self._numb_of_holes+1))'''
        self.table.append(tuple(player_list))

    def _append_to_table(self):
        self.table.append(tuple(self._current_list))

    def _cleaner_list(self):
        self._current_list = [0] * self._count_of_people
        self._list_of_turn = [False] * self._count_of_people

    def _check_for_write(self, numb):
        if self._list_of_turn[numb]:
            return True
        else:
            return False

    def get_table(self):
        new_list = deepcopy(self._empty_list)
        table_for_print = deepcopy(self.table)
        prov = False
        for i in range(self._count_of_people):
            if self._current_list[i] != 0 and all(self._list_of_turn[i] for i in range(self._count_of_people)):
                table_for_print.append(tuple(self._current_list))
            else:
                if self._current_list[i] != 0 and self._check_for_write(i):
                    new_list[i] = self._current_list[i]
                    prov = True
        if prov:
            table_for_print.append(tuple(new_list))
        for i in range(self._counter_for_holes - 1, self._numb_of_holes):
            if len(table_for_print) < self._numb_of_holes + 1:
                table_for_print.append(tuple(self._empty_list))
        return table_for_print

    def _get_victorious(self, result, summ_up):
        winners = []
        for i in range(self._count_of_people):
            if summ_up[i] == result:
                winners.append(self._player_list[i])
        return winners

    def get_winners(self):
        if self._counter_for_holes <= self._numb_of_holes:
            raise RuntimeError('Match still not ended')
        summ_up = {}
        for i in range(self._count_of_people):
            summ_up[i] = 0
            for j in range(1, self._numb_of_holes + 1):
                summ_up[i] += self.table[j][i]

        return self._get_victorious(self._get_num(summ_up), summ_up)

    def _counter_iteration(self):
        self._counter_for_peoples += 1
        if self._counter_for_peoples > self._count_of_people:
            self._counter_for_peoples = 1

    def hit(self, result=False):
        if self.finished:
            raise RuntimeError('Match ended')
        while self._list_of_turn[self._counter_for_peoples - 1]:
            self._counter_iteration()
        self._processing(result)
        self._counter_iteration()
        self._end_checker()

    def _end_of_turn(self):
        self._append_to_table()
        self._cleaner_list()
        self._counter_for_holes += 1
        self._counter_for_peoples = self._counter_for_holes
        while self._counter_for_peoples > self._count_of_people:
            self._counter_for_peoples -= self._count_of_people
        if self._counter_for_holes == self._numb_of_holes + 1:
            self.finished = True

    @abstractmethod
    def _processing(self, result):
        pass

    @abstractmethod
    def _end_checker(self):
        pass

    @abstractmethod
    def _get_num(self):
        pass
