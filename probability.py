from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)



# State vector 
from qiskit.quantum_info import Statevector
stateVector = Statevector(qc)

# to get probability
probability = stateVector.probabilities()
print(probability)