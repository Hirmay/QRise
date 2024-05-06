# the python file contain all the necessary utils for implementing
# the quantum algorithm by Babbush et al.

import numpy as np
import scipy as sc
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import HGate
from qiskit import QuantumCircuit

class Hamiltonian_Formulation:
    def __init__(self, n, K_matrix, M):
        self.N = 2**n
        self.K_matrix = K_matrix
        self.M = M
        
    def compute_F_matrix(self):
        N = self.N
        K = self.K_matrix
        # Matrix F
        F = np.zeros((N,N))
        for j in range(N):
            for k in range(N):
                if j==k:
                    F[j][k] = sum(K[j]) 
                else:
                    F[j][k] = -K[j][k]
        self.F_matrix = F
    
    def compute_B_matrix(self):
        N = self.N
        K = self.K_matrix
        M = self.M
        sqM_B = np.zeros((N,int(N*(N+1)/2)))
        count = 0 #this will keep track of the coloumn of B based on |j,k>
        for j in range(N):
            for k in range(N):
                if j==k:
                    sqM_B[j][k] = np.sqrt(K[j][j])
                elif j<k:
                    sqM_B[j][N+count] = np.sqrt(K[j][k])
                    sqM_B[k][N+count] = -np.sqrt(K[j][k])
                    count+=1
        sqM_inv = np.linalg.inv(np.sqrt(M))
        #B matrix
        B = np.matmul(sqM_inv,sqM_B)
        #B dagger matrix
        B_dag = np.matrix(B).getH()
        self.B_matrix = B
        self.B_dag_matrix = B_dag
        
    def compute_Hamiltonian(self):
        N = self.N
        #calling compute_B_matrix
        self.compute_B_matrix()
        ## doing the padding
        B = self.B_matrix
        B_dag = self.B_dag_matrix
        
        pad_B = np.pad(B,((0,int(N**2-N)),(0,int(N**2-(N*(N+1)/2)))),"constant")
        pad_B_dag = np.matrix(pad_B).getH()
        temp1 = np.concatenate((0*np.identity(N**2),-pad_B),axis = 1)
        temp2 = np.concatenate((-pad_B_dag, 0*np.identity(N**2)),axis = 1)
        # getting the hamiltonian
        H = np.concatenate((temp1,temp2),axis = 0)
        self.H_matrix = H