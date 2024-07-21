from fractions import Fraction

x = ['w'] * 5 + ['b'] * 4
y = ['w'] * 7 + ['b'] * 6

def black_probability(x, y):
    x_w_count = x.count('w')
    x_b_count = x.count('b')
    y_b_count = y.count('b')

    total_combinations = len(x) * (len(y) + 1)

    prob1 = Fraction(x_w_count * y_b_count, total_combinations)
    prob2 = Fraction(x_b_count * (y_b_count + 1), total_combinations)

    return prob1 + prob2

result = black_probability(x, y)
print(result)
