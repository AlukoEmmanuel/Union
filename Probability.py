def prob_a_b(a, b, all_possible_outcomes):
    prob_a = len(a) / len(all_possible_outcomes)
    prob_b = len(b) / len(all_possible_outcomes)
    prob_inter = len(a.intersection(b)) / len(all_possible_outcomes)
    # add return statement to return the probabilities
    return (prob_a + prob_b - prob_inter)

# rolling a dice
evens = {2, 4, 6}
greater_than_2 = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call the function for final result
print('Probability for Getting an even number or a number greater the 2')
print(prob_a_or_b(evens, greater_than_2, all_possible_rolls))