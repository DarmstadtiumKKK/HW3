from standart_rules import StandRules


class Player:
    def __init__(self, name):
        self._name = name


class HitsMatch(StandRules):
    def hit(self, result=False):
        if self.finished:
            raise RuntimeError('Match ended')
        while self._list_of_turn[self._counter_for_peoples - 1] == 'no':
            self._counter_for_peoples += 1
            if self._counter_for_peoples > self._count_of_people:
                self._counter_for_peoples = 1
        if result:
            self._list_of_turn[self._counter_for_peoples - 1] = 'no'
        self._current_list[self._counter_for_peoples - 1] += 1
        if self._list_of_turn[self._counter_for_peoples - 1] == 'yes' and self._current_list[
            self._counter_for_peoples - 1] == self.limit - 1:
            self._list_of_turn[self._counter_for_peoples - 1] = 'no'
            self._current_list[self._counter_for_peoples - 1] = self.limit
        else:
            self._counter_for_peoples += 1
        if self._counter_for_peoples > self._count_of_people:
            self._counter_for_peoples = 1
        if all(self._list_of_turn[i] == 'no' for i in range(self._count_of_people)):
            self._append_to_table()
            self._cleaner_list()
            self._counter_for_holes += 1
            if self._counter_for_holes > self._numb_of_holes:
                self.finished = True

    def _get_num(self, diction):
        vals = list(diction.values())
        minimum = vals[0]
        for i in range(1, len(vals)):
            if vals[i] < minimum:
                minimum = vals[i]
        return minimum


class HolesMatch(StandRules):
    flag = True

    tries = 0

    def hit(self, result=False):

        if self.finished:
            raise RuntimeError('Match ended')
        while self._list_of_turn[self._counter_for_peoples - 1] == 'no':
            self._counter_for_peoples += 1
            if self._counter_for_peoples > self._count_of_people:
                self._counter_for_peoples = 1
        if result:
            self.flag = False
            self.tries = 0
            self._current_list[self._counter_for_peoples - 1] += 1
        self._list_of_turn[self._counter_for_peoples - 1] = 'no'
        if all(self._list_of_turn[i] == 'no' for i in range(self._count_of_people)):
            self.tries += 1
            if self.flag and self.tries < self.limit:
                self._list_of_turn = ['Yes'] * self._count_of_people
            else:
                self._append_to_table()
                self._cleaner_list()
                self._counter_for_holes += 1
                print(self._counter_for_holes)
                self._counter_for_peoples = self._counter_for_holes - 1
                self.tries = 0
                self.flag = True
                if self._counter_for_holes == self._numb_of_holes + 1:
                    self.finished = True
        self._counter_for_peoples += 1
        if self._counter_for_peoples > self._count_of_people:
            self._counter_for_peoples = 1

    def _get_num(self, diction):
        vals = list(diction.values())
        minimum = vals[0]
        for i in range(1, len(vals)):
            if vals[i] > minimum:
                minimum = vals[i]
        return minimum
