from biosynth_bridge.growth_simulation import simulate_growth

# Simulate the growth of a cell population
population = simulate_growth(initial_population=10, growth_rate=1.5, time_steps=10)
print(f"Cell population after 10 time steps: {population}")
