import random

# --- Simulate coin toss ---
def toss_coin(n_times=1000):
    outcomes = [random.choice(['H', 'T']) for _ in range(n_times)]
    prob_heads = outcomes.count('H') / n_times
    prob_tails = outcomes.count('T') / n_times
    return prob_heads, prob_tails

for i in range(5):
    prob_heads, prob_tails = toss_coin()
    print("\nP(Heads):", prob_heads)
    print("P(Tails):", prob_tails)
