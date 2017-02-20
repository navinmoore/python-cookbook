# -*-coding:utf-8-*-

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


'''
d = Date()
format(d)
format(d, 'mdy')
# 2012-12-21
"the date is {:ymd}".format(d)
# 'the date is 2012-12-21'
'''
