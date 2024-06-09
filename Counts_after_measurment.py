from qiskit import QuantumCircuit

qc = QuantumCircuit(2,2)
qc.h(0)
qc.measure(0,0)


# Note: Statevector(qc) cannot be used if the curcuit has measurment
# to do so -> Use basicSimulator
from qiskit.providers.basic_provider import BasicSimulator #NOTE: Cannot use the Basic simulator can only run the basis gates

#to use the Basic simulator -> creat a Job
job = BasicSimulator().run(qc, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)