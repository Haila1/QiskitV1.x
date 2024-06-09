# coin flip game 
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit.providers.basic_provider import BasicSimulator



def coin_flip():
    #create a curcuit with one qubit
    qc = QuantumCircuit(1, 1)

    # apply H gate 
    qc.h(0)

    # measure the result 
    qc.measure(0, 0)  

    # use basicSimulator to get count
    #to use the Basic simulator -> creat a Job that runs the qc on the simulator for a number of shots 
    job = BasicSimulator().run(qc, shots=1024)

    # get the result
    result = job.result()

    #get the count
    counts = result.get_counts()
    x = list(counts)[0]
    return x
   

x = coin_flip()
Head=0
Tail=0
for i in range(0,10):
     cf = coin_flip()
     if cf == '1':
        Head =Head + 1
     else:
        Tail = Tail+ 1


print(f'heads: {Head},  tails: {Tail}')