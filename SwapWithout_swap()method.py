# swap without swap() method
from qiskit import QuantumCircuit

#create a curcuit with one qubit
qc = QuantumCircuit(2)

# c not gates
qc.cx(0,1)
qc.cx(1,0)
qc.cx(0,1)

qc.draw('mpl')