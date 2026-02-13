class Canvas:
    degree_completion = 4 # years

    def __init__(self, level, credit, loan_debt):
        self.level = level
        self.credit = credit
        self.loan_debt = loan_debt

    def first_method(self, credit):
        self.credit += credit

    def second_method(self, loan_amount):
        self.loan_debt += loan_amount

    def third_method(self, eligible):
        if eligible:
            return self.loan_debt - 100
        else:
            return self.loan_debt

    def fourth_method(self, year_passed):
        return Canvas.degree_completion - year_passed

    def fifth(self, level):
        self.level = level

    def sixth_method(self):
        return self.level

    def seventh(self):
        return self.credit

sam = Canvas("freshman", 12, 1000)
susan = Canvas("sophomore", 31, 1200)
james = Canvas("junior", 66, 1800)
julie = Canvas("senior", 66, 1800)

julie.first_method(12)
susan.second_method(1000)
james.fifth("senior")
sam.first_method(9)
sam.second_method(100)

print(julie.sixth_method())

print(sam.seventh())

print(sam.fifth("sophomore"))

print(susan.third_method(True))

print(james.fourth_method(2))

print(sam.third_method(False))

print(julie.first_method(18))
print(julie)

print(susan.seventh())

print(sam.sixth_method())

print(Canvas)
