import numpy as np
import matplotlib as plt 

with open("simcov.stats") as fptr: 
    lines = [x.rstrip() for x in fptr.readlines()]

rows = [x.split() for x in lines[1:]]
column_names = lines[0][1:] 

time_increments = [int(x[0]) for x in rows]

incubating_cells = [int(x[1]) for x in rows]

expressing_cells = [int(x[2]) for x in rows]

apoptosis_cells = [int(x[3]) for x in rows]

dead_cells = [int(x[4]) for x in rows]

 

 
