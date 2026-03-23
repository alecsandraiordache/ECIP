#simulate event probabilities
#estimate P(A|B) from data
#interpret conditional probability


import numpy as np

n_samples = 100000
np.random.seed(42)


prob_B = 0.30
B = np.random.rand(n_samples) < prob_B


A = np.zeros(n_samples, dtype=bool)

A[B] = np.random.rand(np.sum(B)) < 0.80


A[~B] = np.random.rand(np.sum(~B)) < 0.20


p_B_empirical = np.mean(B)


p_A_and_B_empirical = np.mean(A & B)

p_A_given_B = p_A_and_B_empirical / p_B_empirical


print("-" * 50)
print(f"Total simulated events (days): {n_samples}")
print(f"Empirical P(B) [Probability of Rain]:         {p_B_empirical:.4f}")
print(f"Empirical P(A and B) [Rain AND Traffic]:      {p_A_and_B_empirical:.4f}")
print("-" * 50)
print(f"Estimated P(A|B) [Traffic GIVEN it rained]:   {p_A_given_B:.4f}")
print("-" * 50)


"""
Discussion: Interpreting Conditional Probability P(A|B)

1. What is Conditional Probability?
   Conditional probability, written as P(A|B), measures the likelihood of 
   event A occurring under the specific condition that event B has already 
   occurred. The vertical bar '|' is read as "given".

2. The Formula in Practice:
   Mathematically, P(A|B) = P(A and B) / P(B).
   In our simulation:
   - P(B) is the probability that it rains (~0.30).
   - P(A and B) is the probability that it rains AND there is traffic (~0.24).
   - By dividing the times they happened together by the total times B happened 
     (0.24 / 0.30), we isolate the effect.

3. Interpreting the Result:
   Our estimated P(A|B) is approximately 0.80 (80%). This means that if we 
   ALREADY KNOW it is raining (Event B is true), we have an 80% certainty 
   that there will be a traffic jam (Event A). 
   
   The core concept here is "Shrinking the Universe": when we ask for P(A|B), 
   we stop looking at all 100,000 days. We shrink our entire universe of data 
   down to ONLY the 30,000 days where it rained, and we ask, "Out of these 
   specific days, how many had traffic?"
"""