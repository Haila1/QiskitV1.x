# Aer simulator
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2,1)
qc.h([0,1])
qc.cx(0,1)
qc.measure(1,0)

#to use get_statevector() -> first use save_statevector()
qc.save_statevector()
qc.draw()

# get the AerSimulator() backend to qc 
transpiled_qc = transpile(qc, backend=AerSimulator())
job = AerSimulator().run(transpiled_qc)
result = job.result()
State = result.get_statevector()

State.draw('latex')

