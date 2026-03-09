#for each value of R, calculate the population size and plot the data 
#r= [2, 2.5, 1, 12, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
#consider the above vector as values of the R factor. Measure yearly across 17 years
#answer the q : what will be the population growth in year 17? 

import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

getcontext().prec = 20  
getcontext().Emax = 999999999 

R_values = [2, 2.5, 1, 12, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]


exact_population = Decimal('0.5') 


years = [0]
population_history = [float(exact_population)] 

exact_population_year_16 = Decimal('0')


for year, R in enumerate(R_values, start=1):
    R_dec = Decimal(str(R))
    
    
    exact_population = R_dec * exact_population * (Decimal('1') - exact_population)
    
    
    if year == 16:
        exact_population_year_16 = exact_population


    years.append(year)
    
    
    try:
        plot_val = float(exact_population)
    except OverflowError:
        plot_val = float('-inf') 
        
    population_history.append(plot_val)


exact_growth = exact_population - exact_population_year_16

print(f"The EXACT mathematical population size in Year 17 is: {exact_population:.4E}")
print(f"The EXACT mathematical population growth in Year 17 is: {exact_growth:.4E}")

# Biologically: 
# The actual population growth is ZERO because the population went completely 
# EXTINCT back in Year 5. In Year 4 (R=12), the population overshot the 
# environment's carrying capacity (reaching 215%), causing a mathematical 
# collapse into negative numbers in Year 5. You cannot have negative animals!

plt.figure(figsize=(10, 6))


plt.plot(years, population_history, marker='o', color='purple', linewidth=2)


plt.axhline(0, color='red', linestyle='--', label='Extinction Line (Zero)')

plt.title("Population Size with Changing R Values (17 Years)")
plt.xlabel("Year")
plt.ylabel("Population Fraction (P)")
plt.xticks(range(0, 18))
plt.grid(True)
plt.legend()


plt.show()