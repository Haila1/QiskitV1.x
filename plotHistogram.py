
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)

# State vector 
from qiskit.quantum_info import Statevector
stateVector = Statevector(qc)

# to get count
count = stateVector.sample_counts(shots=1024)
print(count)


# to plot histogram
from qiskit.visualization import plot_histogram
plot_histogram(count)