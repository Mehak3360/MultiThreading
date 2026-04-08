import os

cores = os.cpu_count()
print("Logical cores in your system:", cores)
print("You should test threads from 1 to", 2 * cores)
