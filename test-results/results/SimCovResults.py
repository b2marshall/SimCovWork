import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

with open(naive.stats) as fpt:
    lines = [x.rstrip() for x in fprt.readlines()]

rows_naive = [x.split() for x in lines[1:]]
naive_virions = [float(x[8]) for x in rows_naive]
max_load_naive = max(naive_virions) 


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

if  (max_viral_load/max_load_naive) < .8 and (max_viral_load/max_load_naive) > .6 and peak_time < 4800 and peak_time > 3840:
    print("Peak happens at roughly the right time and the right amount, eh")
else: 
    print("viral loads incomparable.")

plt.figure(figsize=(9,5))
plt.plot(times, incubating_cells)
plt.xlim(0,times[-1])
plt.ylabel("Number of Incubating Cells")
plt.xticks(ticks) 
plt.xlabel("Hours After Infection")
plt.title("Incubating Cells") 
plt.savefig("incubatingcells.png")
