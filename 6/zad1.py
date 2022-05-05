def _check(*args):
    for elem in args:
        if not (isinstance(elem, int)):
            raise TypeError('Wrong type')


def _check2(*args):
    for elem in args:
        if elem < 0:
            raise ValueError('Delta less than 0')


class Clock:
    def __init__(self, hour: int, min: int, sec: int):
        _check(hour, min, sec)
        self.hour = hour
        self.min = min
        self.sec = sec

    def advance(self, h_delta: int, min_delta: int, s_delta: int):
        _check(h_delta, min_delta, s_delta)
        _check2(h_delta, min_delta, s_delta)
        self.sec += s_delta
        rem = self.sec // 60
        self.sec %= 60
        self.min += min_delta + rem
        rem = self.min // 60
        self.min %= 60
        self.hour += h_delta + rem
        rem = self.min // 24
        self.hour %= 24

    def __str__(self):
        return (f'{self.hour:02d}:{self.min:02d}:{self.sec:02d}')


class Calendar:
    def __init__(self, year: int, month: int, day: int):
        _check(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    def advance(self, y_delta: int, m_delta: int, d_delta: int):
        _check(y_delta, m_delta, d_delta)
        _check2(y_delta, m_delta, d_delta)
        self.day += d_delta
        rem = self.day // 30
        self.day %= 30
        self.month += m_delta + rem
        rem = self.month // 12
        self.month %= 12
        self.year += y_delta + rem

    def __str__(self):
        return (f'{self.year:04d}:{self.month:02d}:{self.day:02d}')


if __name__ == "__main__":
    c = Clock(15, 45, 32)
    d = Calendar(2002, 30, 45)
    print(c)
    c.advance(0, 0, 600)
    print(c)
    print(d)
