class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            if number == 4:
                if number % 2 == 0:
                    factors.append(2)
                    number //= 2
                if number % 2 == 0:
                    factors.append(2)
                    number //= 2
            else:
                factors.append(number)
        return factors
