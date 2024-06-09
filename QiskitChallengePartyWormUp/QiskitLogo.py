# recreate qiskit logo 
from qiskit import QuantumCircuit
from qiskit.visualization import plot_state_qsphere

#create a curcuit with one qubit
qc = QuantumCircuit(4)    

# H gate on thi first qubit
qc.h(0)

# c not gates (0,1), (1,2), (2,3)
qc.cx(0,1)
qc.cx(1,2)
qc.cx(2,3)

# x gate on q1
qc.x(1)

plot_state_qsphere(qc)