class Account:
    max = 100.00
    min = 0.00

    def __init__(self, starting_balance: float):
        self._balance = starting_balance

    def __str__(self):
        return f"£{self._balance}"

    def get_balance(self):
        return self._balance

    def increase_balance(self, amt: float):
        if amt == 0.00:
            raise ValueError("This amount has no effect")
        elif amt < 0:
            raise ValueError("Cannot increase by negative, please use decrease_balance")

        new_bal = self._balance + amt

        if new_bal > self.max:
            raise ValueError(f"Balance cannot go over maximum of {self.max}")

        self._balance = new_bal
        return self._balance

    def decrease_balance(self, amt: float):
        if amt == 0.00:
            raise ValueError("This amount has no effect")
        elif amt < 0:
            raise ValueError("Cannot increase by negative, please use decrease_balance")

        new_bal = self._balance - amt

        if 0 - new_bal > self.min:
            raise ValueError(f"Balance cannot go under minimum of {self.min}")

        self._balance = new_bal
        return self._balance


class DebtAccount(Account):
    def __init__(self, starting_balance: float, overdraft_available: float):
        super().__init__(starting_balance)
        self.min = overdraft_available

    def __str__(self):
        if self._balance < 0:
            return f"(£{-self._balance})"
        else:
            return f"£{self._balance}"


acc = DebtAccount(5.00, 50.00)
acc.decrease_balance(10.00)
print(acc)
