import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

filename = input("filename?\n")
with open(filename) as fptr: 
    lines = [x.rstrip() for x in fptr.readlines()]

rows = [x.split() for x in lines[1:]]
column_names = lines[0][1:] 

times = [int(x[0])/60 for x in rows]
ticks = []

for element in times: 
    if element % 8 == 0:
        ticks.append(element)

incubating_cells = [int(x[1]) for x in rows]

expressing_cells = [int(x[2]) for x in rows]

apoptosis_cells = [int(x[3]) for x in rows]

dead_cells = [int(x[4]) for x in rows]

virions = [float(x[8]) for x in rows]
max_viral_load = max(virions) 
peak_time = virions.index(max_viral_load)


plt.figure(figsize=(9,5))
plt.plot(times, incubating_cells)
plt.xlim(0,times[-1])
plt.ylabel("Number of Incubating Cells")
plt.xticks(ticks) 
plt.xlabel("Hours After Infection")
plt.title("Incubating Cells") 
plt.savefig("incubatingcells.png")
