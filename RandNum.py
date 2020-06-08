from projectq.ops import All, CNOT, H, Measure, X, Z
from projectq import MainEngine

x = 0
y = 0
def get_random_number(quantum_engine):
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number

d = input('press enter to flip quantum coin 1000 times')

random_numbers_list = []
#initialise quantum backend
quantum_engine = MainEngine()
# for loop to generate 10 random numbers

for i in range(1000):
    # calling the random number function and append the return to the list
    random_numbers_list.append(get_random_number(quantum_engine))
# Flushes the quantum engine from memory
quantum_engine.flush()

print('Random numbers', random_numbers_list)
for i in range(1000):
    if random_numbers_list[i] == 1:
        x = x+1
    elif random_numbers_list[i] == 0:
        y = y+1
print('total number of heads = ', x)
print('total number of tails = ', y)
