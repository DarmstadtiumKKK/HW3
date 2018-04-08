from standart_rules import StandRules


class Player:
    def __init__(self, name):
        self._name = name


class HitsMatch(StandRules):
    def _processing(self,result):
        if result:
            self._list_of_turn[self._counter_for_peoples - 1] = True
            self._current_list[self._counter_for_peoples - 1] += 1
        else:
            if self._current_list[self._counter_for_peoples - 1] == self.limit - 2:
                self._list_of_turn[self._counter_for_peoples - 1] = True
                self._current_list[self._counter_for_peoples - 1] = self.limit
                self._counter_for_peoples -= 1
            else:
                self._current_list[self._counter_for_peoples - 1] += 1

    def _end_checker(self):
        if all(self._list_of_turn[i] for i in range(self._count_of_people)):
            self._end_of_turn()

    def _get_num(self, diction):
        return min(list(diction.values()))


class HolesMatch(StandRules):
    _hit_registrated = False

    _tries = 0

    def _processing(self,result):
        if result:
            self._hit_registrated = True
            self.tries = 0
            self._current_list[self._counter_for_peoples - 1] += 1
        self._list_of_turn[self._counter_for_peoples - 1] = True

    def _end_checker(self):
        if all(self._list_of_turn[i] for i in range(self._count_of_people)):
            self._tries += 1
            if not self._hit_registrated and self._tries < self.limit:
                self._list_of_turn = [False] * self._count_of_people
            else:
                self._end_of_turn()
                self._tries = 0
                self._hit_registrated = False

    def _get_num(self, diction):
        return max(list(diction.values()))
