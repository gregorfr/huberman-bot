import random

# Generating a random instruction
def generate_instruction():
    x = random.randint(1, 5)  # Random number between 1-5
    z = random.randint(1, 120)  # Random number between 1-120
    y = random.choice(["jumping jacks", "push-ups", "sit-ups", "squats", "lunges", "sunlight viewing", "doomscrolling"])  # Random activity
    return f"{x} times a week, for {z} minutes, do {y}"

# Number of instructions to generate
num_instructions = 1000

# File path (adjust as needed)
file_path = 'data/random_protocols.txt'

# Generate and write instructions to a file
with open(file_path, 'w') as file:
    for _ in range(num_instructions):
        instruction = generate_instruction()
        file.write(instruction + '\n')
