#simulate a Markov-MACHINE   containing 3 states A, B, C
#Run the machine 15 times and record the sequence of states 
#store these state as "S"
#each state cares a weight:
    #A = 1.5
    #B = 2
    #C = 3.3
#Use these weights as values for the growth factor R and calculate the population size in 15 steps
#according to the weights from S
#Start de population from 0.5

import numpy as np
import matplotlib.pyplot as plt

states = ['A', 'B', 'C']

transition_matrix = {
    'A': [0.0, 0.4, 0.6],  
    'B': [0.5, 0.5, 0.0],  
    'C': [0.2, 0.2, 0.6]  
}


current_state = 'A'
S = [] 


for _ in range(15):
    S.append(current_state)
    current_state = np.random.choice(states, p=transition_matrix[current_state])


weights = {
    'A': 1.5,
    'B': 2.0,
    'C': 3.3
}


R_sequence = [weights[state] for state in S]


current_population = 0.5
population_history = [current_population]

print("--- Simulation Results ---")
print(f"{'Step':<5} | {'State':<5} | {'R Weight':<10} | {'Population Size'}")
print("-" * 45)
print(f"{0:<5} | {'-':<5} | {'-':<10} | {current_population:.4f} (Start)")


for step in range(15):
    R = R_sequence[step]
    state = S[step]
    
    
    current_population = R * current_population * (1 - current_population)
    population_history.append(current_population)
    
    print(f"{step+1:<5} | {state:<5} | R = {R:<6} | {current_population:.4f}")


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)


ax1.step(range(1, 16), R_sequence, where='mid', marker='o', color='orange', linewidth=2)
ax1.set_title("Markov Chain Output: R Values over 15 Steps", fontweight='bold')
ax1.set_ylabel("Growth Factor (R)")
ax1.set_yticks([1.5, 2.0, 3.3])
ax1.set_yticklabels(['A (1.5)', 'B (2.0)', 'C (3.3)'])
ax1.grid(True, linestyle='--', alpha=0.6)


ax2.plot(range(16), population_history, marker='s', color='purple', linewidth=2)
ax2.set_title("Population Size Fluctuation", fontweight='bold')
ax2.set_xlabel("Steps")
ax2.set_ylabel("Population Fraction (P)")
ax2.set_ylim(0, 1)
ax2.set_xticks(range(16))
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()