import matplotlib
import pickle 
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

'''
unnecessary probably
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
'''

with open('naive1.stats') as fpt1:
    lines_naive_1 = [x.rstrip() for x in fpt1.readlines()]

with open('naive4.stats') as fpt4:
    lines_naive_4 = [x.rstrip() for x in fpt4.readlines()]
    
with open('naive16.stats') as fpt16:
    lines_naive_16 = [x.rstrip() for x in fpt16.readlines()]

rows_naive_1 = [x.split() for x in lines_naive_1[1:]]
naive_virions_1 = [float(x[8]) for x in rows_naive]
max_load_naive_1 = max(naive_virions_1) 


rows_naive_4 = [x.split() for x in lines_naive_4[1:]]
naive_virions_4 = [float(x[8]) for x in rows_naive]
max_load_naive_4 = max(naive_virions_4)


rows_naive_16 = [x.split() for x in lines_naive_16[1:]]
naive_virions_16 = [float(x[8]) for x in rows_naive]
max_load_naive_16 = max(naive_virions_16) 

with open('PI1.stats') as fp1:
    lines_pi_1 = [x.rstrip() for x in fp1.readlines()]

with open('PI4.stats') as fp4:
    lines_pi_4 = [x.rstrip() for x in fp4.readlines()]
    
with open('PI16.stats') as fp16:
    lines_pi_16 = [x.rstrip() for x in fp16.readlines()]
    
rows_pi_1 = [x.split() for x in lines_pi_1[1:]]
pi_virions_1 = [float(x[8]) for x in rows_pi_1]
max_load_pi_1 = max(pi_virions_1) 

rows_pi_4 = [x.split() for x in lines_pi_4[1:]]
pi_virions_4 = [float(x[8]) for x in rows_pi_4]
max_load_pi_4 = max(pi_virions_4) 

rows_pi_16 = [x.split() for x in lines_pi_16[1:]]
pi_virions_16 = [float(x[8]) for x in rows_pi_16]
max_load_pi_16 = max(pi_virions_16) 

'''
#filename = input("filename?\n")
with open(filename) as fptr: 
    lines = [x.rstrip() for x in fptr.readlines()]

rows = [x.split() for x in lines[1:]]
column_names = lines[0][1:] 
'''
times = [int(x[0]) for x in rows_naive_1]
ticks = []
labels = []
for element in times: 
    if element % 1440 == 0:
        ticks.append(element)
        labels.append(str((int(element/(24*60)))))

        
        
incubating_cells = [int(x[1]) for x in rows]

expressing_cells = [int(x[2]) for x in rows]

apoptosis_cells = [int(x[3]) for x in rows]

dead_cells = [int(x[4]) for x in rows]

virions = [float(x[8]) for x in rows]
max_viral_load = max(virions) 
peak_time = virions.index(max_viral_load)


plt.figure(figsize=(9,5))
plt.plot(times, virions, color='green', label='PI Patient')
plt.plot(times, naive_virions, color='red', label='Naive Patient')
plt.xlim(0,times[-1])
plt.ylabel("Virions")
plt.xticks(ticks,labels)

plt.xlabel("Days After Infection")
plt.legend(fontsize=16)
plt.title("Virions Over Time") 
plt.savefig("virions.png")
plt.clf()
plt.cla()
plt.close()


plt.figure(figsize=(9,5))
plt.plot(times, naive_virions_1, color='green', label='Naive Patient - 1 FOI', linestyle='dashed')
plt.plot(times, pi_virions_1, color='green', label='PI Patient - 1 FOI', linestyle='solid')
plt.plot(times, naive_virions_4, color='red', label='Naive Patient - 4 FOI', linestyle='dashed')
plt.plot(times, pi_virions_4, color='red', label='PI Patient - 4 FOI', linestyle='solid')
plt.plot(times, naive_virions_16, color='blue', label='Naive Patient - 16 FOI', linestyle='dashed')
plt.plot(times, pi_virions_16, color='blue', label='PI Patient - 16 FOI', linestyle='solid')
plt.xlim(0,times[-1])
plt.ylim(0,5000000)
plt.yticks(np.linspace(0,5000000, num=5), ['1M', '2M', '3M', '4M','5M'])
plt.ylabel("Virions")
plt.xticks(ticks,labels)
plt.xlabel("Days After Infection")
plt.legend(fontsize=14)
plt.title("Virions Over Time") 
plt.savefig("oneplot.png")
plt.clf()
plt.cla()
plt.close()

plt.figure(figsize=(9,5))
plt.plot(times, naive_virions_1, color='green', label='Naive Patient - 1 FOI', linestyle='dashed')
plt.plot(times, pi_virions_1, color='green', label='PI Patient - 1 FOI', linestyle='solid')
plt.plot(times, naive_virions_4, color='red', label='Naive Patient - 4 FOI', linestyle='dashed')
plt.plot(times, pi_virions_4, color='red', label='PI Patient - 4 FOI', linestyle='solid')
plt.plot(times, naive_virions_16, color='blue', label='Naive Patient - 16 FOI', linestyle='dashed')
plt.plot(times, pi_virions_16, color='blue', label='PI Patient - 16 FOI', linestyle='solid')
plt.xlim(0,times[-1])
plt.yscale("log")
plt.ylim(0,5000000)
plt.yticks(np.linspace(0,5000000, num=5), ['1M', '2M', '3M', '4M','5M'])
plt.ylabel("Virions")
plt.xticks(ticks,labels)
plt.xlabel("Days After Infection")
plt.legend(fontsize=14)
plt.title("Virions Over Time") 
plt.savefig("oneplotlog.png")
plt.clf()
plt.cla()
plt.close()

