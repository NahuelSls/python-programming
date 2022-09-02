from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        return reduce(lambda x, y: x - y, args)

    def mul(self, *args):
        if not all(args):
            raise ValueError
        '''
        def mul2(a, b):
            return a * b
        return reduce(mul2, args)
        '''
        return reduce(lambda x, y: x * y, args)

    '''
    def div(self, *args):
        return reduce(lambda x, y: x/y, args)
    '''

    def div(self, a, b):
        '''
        if not b:
            return float('inf')

        return a / b
        '''
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')

    def avg(self, it, lt=None, ut=None):

        while it:
            if not lt:
                lt = min(it)

            if not ut:
                ut = max(it)

            _it = [x for x in it if x <= ut and x >= lt]

            return sum(_it) / len(_it)

        else:
            return 0

