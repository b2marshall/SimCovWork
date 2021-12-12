import matplotlib
import pickle 
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

unvax = open('chia-unvaccinated-data','rb') 
chia_unvax = pickle.load(unvax)
unvax.close()

vax = open('chia-vaccinated-data','rb') 
chia_vax = pickle.load(vax)
unvax.close()

distances = []
for i in range(0,len(chia_vax)):
    distances.append(abs(chia_unvax[i]-chia_vax[i]))
print(distances) 

with open('naive.stats') as fpt:
    lines = [x.rstrip() for x in fprt.readlines()]

rows_naive = [x.split() for x in lines[1:]]
naive_virions = [float(x[8]) for x in rows_naive]
max_load_naive = max(naive_virions) 


filename = input("filename?\n")
with open(filename) as fptr: 
    lines = [x.rstrip() for x in fptr.readlines()]

rows = [x.split() for x in lines[1:]]
column_names = lines[0][1:] 

times = [int(x[0]) for x in rows]
ticks = []

for element in times: 
    if element % 1440 == 0:
        ticks.append(element/(24*60))

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
plt.plot(times, virions, color='green', label='Vaccinated Patient')
plt.plot(times, naive_virions, color='red', label='Naive Patient')
plt.xlim(0,times[-1])
plt.ylabel("Virions")
plt.xticks(ticks) 
plt.xlabel("Days After Infection")
plt.legend(fontsize=16)
plt.title("Virions Over Time") 
plt.savefig("virions.png")
