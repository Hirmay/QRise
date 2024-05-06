# Classiq Entanglers
<h1>Quantum Research & Industry Skills Exchange (QRISE) - 2024 Hackathon</h1>

<h3>Classiq Challenge</h3>
<p>The challenge is to simulate coupled classical oscillators using quantum computing to obtain exponential speedups. The challenge repository - https://github.com/quantumcoalition/qrise2024-classiq-challenge </p>

<h3>Background</h3>
<p>The progress of quantum computers in the last few years has been immense, with better and better quantum computers being developed each year. Nowadays there are quantum computers with hundreds of qubits that can compute quantum algorithms with circuit depth of up to a few thousand and still receive a significant signal. One of the key challenges is the development of efficient and novel quantum algorithms that are useful and offer exponential advantage over classical methods. One of the very few algorithms we know of under this definition is the Exponential Quantum Speedup in Simulating Coupled Classical Oscillators work, presented in 2023 by Ryan Babbush et al.

Like most quantum algorithms papers, this is a theoretical work. Taking a theoretical paper and implementing it in practice is a massive challenge with many obstacles that need to be overcome, both practical and theoretical.</p>

<p>Research Paper link - </p> <a href="https://journals.aps.org/prx/pdf/10.1103/PhysRevX.13.041041">https://journals.aps.org/prx/pdf/10.1103/PhysRevX.13.041041</a>

<h3>Team Members</h3>
<UL>
  <LI>Ramachandran Sekanipuram Srikanthan</LI>
  <LI>Hirmay Sandesara</LI>
  <LI>Aman Gupta</LI>
</UL>

<h3>Short Presentation</h3>

<p>We have made a short presentation explaning our work and the slides are added in this Git - inside Submission/Slides directory. We have also added our video presentation in Youtube and can be viewed in the below link.</p>

<a href="https://youtu.be/9wHo1hxuORQ">https://youtu.be/9wHo1hxuORQ</a>


<h3>Motivation and Vision</h3>

<UL>
  <LI><p>Throughout this challenge our aim was to practically demonstrate the quantum speedup of the algorithm by {Babbush_2023}. </p></LI>
  <LI><p>We wanted to do this by running an instance of this algorithm which is proven by the authors to be BQP complete and try to ensure scalability to show practical demonstration on a 70+ qubit system (depending on the quantum simulator), possibly showcasing quantum supremacy.</p></LI>
  <LI><p>We believe that we have managed to do that for a specific case which only takes polynomial number of resources and would fit within the depth range of 10^4, 3*10^4</p></LI>
</UL>


<h3>Project structure</h3>
<UL>
  <LI><b>State_EnDecode_Couple_HO.ipynb</b> - Contains state preparation approaches and the measurement of fidelity of the final state. It also contains parsing of state vector back to classical values.</LI>
  <LI><b>state_preparation_classiq.ipynb</b> - Testing our state preparation approach using Classiq framework.</LI>
  <LI><b>Hamiltonian_formation.ipynb</b> - Contains our proposed determinsitic way of computing hamiltonian matrix</LI>
  <LI><b>Structural_Foundation.ipynb</b> - Gives the overall picture from state preparation, hamiltonian formulation, quantum circuit generation, time evolution using various approaches and fidelity measurement.</LI>
  <LI><b>Manual Simulation.pdf</b> - Manual derivation of the hamiltonian for a simple example</LI>
  <LI><b>Submission/hamiltonian_simulation_classiq.ipynb</b> - Describes the full process of simulation of coupled classical oscillator using Classiq.</LI>
  <LI><b>Submission/Complete_run.ipynb</b> - Code for performing a simulation using Classiq where user can edit the values of masses and spring constants.</LI>
  <LI><b>Submission/Complete_run_with_save.ipynb</b> - Containts code for a complete run along with qmod qprog file generation for saving.</LI>
  <LI><b>Submission/output.zip</b> - Contains the saved qmod and qprog file for the run in Submission/Complete_run.ipynb</LI>
</UL>


<h3>Conclusion</h3>

We thank QRISE and Classiq for providing us with this wonderful opportunity.





