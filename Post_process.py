import numpy as np
from sympy import symbols as syb
from sympy import MatrixSymbol as msyb
from sympy import sqrt, Array, I, Matrix
from sympy.physics.quantum import Bra,Ket, TensorProduct
from sympy.physics.quantum.gate import HadamardGate as H
from sympy.physics.quantum.gate import ZGate as Z
from sympy import simplify, Eq, linsolve, solve
from sympy.solvers import solve

class post_processing:
    def __init__(self, E = 1, K = np.array(([1,1],[1,1])) ,M = [1,1],x_ini = [1,-1], x_dot_ini = [0,0] ) -> None:
        self.E = E
        self.K = K
        self.M = M
        self.x_ini = x_ini
        self.x_dot_ini = x_dot_ini
        self.N = len(M)
        self.x = list(syb('x0:%d'%self.N,real = True)) #unknowns postion vector
        self.x_dot = list(syb('v0:%d'%self.N,real = True)) #unknown velocity vector
        self.psi, self.mu = self.__dummy_state()

    def __dummy_state(self):
        mu = []
        for i in range(self.N):
            for j in range(self.N):
                if j>i:
                    mu.append((I*sqrt(self.K[i,j])*(self.x[i]-self.x[j]))/sqrt(2*self.E))
                elif j==i:
                    mu.append((I*sqrt(self.K[j,j])*self.x[j])/sqrt(2*self.E))
        # N terms kinetic energy part of the quantum state
        y_dot = []
        for i in range(self.N):
            y_dot.append(self.x_dot[i]*sqrt(self.M[i])/sqrt(2*self.E))
            psi0 = y_dot+mu
        #padding with zeros
        for i in range(int(3*self.N*(self.N-1)/2)):
            psi0.append(0)
        return psi0, mu


    def __get_ke_part(self):
        return self.psi[:self.N]     #extracted the kitentic part of the state
    
    def __x_measure_equations(self):
        psi0_ext = self.__get_ke_part() #get the KE part
        q = int(np.log2(self.N))    #number of qubits carrying kinetic energy terms
        gate = H(q)
        H_matrix = gate.get_target_matrix()
        # Create the tensor product of the Hadamard gate for n qubits
        H_otimes_q = TensorProduct(*[H_matrix for _ in range(q)])
        phi0_ext = H_otimes_q*Matrix(psi0_ext)
        phi_amps = []
        for i in range(len(phi0_ext)):
            phi_amps.append(phi0_ext[i]*phi0_ext[i])
        return phi_amps
    
    def eliminate_solution(self,out_probs_comp,solutions):
        filtered_sols = []
        for cases in solutions:
            # Check if all values in the dictionary match the corresponding compare value
            if np.allclose(out_probs_comp,[float(_) for _ in np.array(list(cases.values()))**2/2]):
                filtered_sols.append(cases)
        return filtered_sols
    
    def post_process_ke(self,out_probs_x,out_probs_comp):
        out_probs_comp = out_probs_comp[:self.N]
        out_probs_x = out_probs_x[:self.N]  #only the first N probabilities that correspond to kinetic part  
        amps_list = self.__x_measure_equations()
        Eq_list = []
        for i in range(self.N):
            Eq_list.append(simplify(amps_list[i])-out_probs_x[i])
        solution = solve(Eq_list, self.x_dot,dict =True)
        eliminate_sols = self.eliminate_solution(out_probs_comp,solution)
        return {"Equations":Eq_list, "Solutions": eliminate_sols}
    

    def __get_pe_part(self):
        return self.psi[self.N:int(self.N*(self.N+3)/2)]     #extracted the potential energy part of the state


    def __eq_association(self):
        lst = simplify(abs(np.array(self.mu))*abs(np.array(self.mu)))
        Eq_list = []
        for i in range(len(lst)):
            if lst[i] != 0: #removing zeros in equations because of zeros in K matrix
                Eq_list.append(lst[i]-self.out_probs_pe[i])
        return Eq_list

    def post_process_pe(self,out_probs_comp):
        self.out_probs_pe = out_probs_comp[self.N:int(self.N*(self.N+3)/2)]
        Eq_list = self.__eq_association()
        solution = solve(Eq_list,self.x ,dict =True)
        return {"Equations":Eq_list,"Solutions": solution}
