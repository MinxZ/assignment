syms Mu;%(N/m,friction constant)
syms E(theta);
m = 0.2;%(kg)
r = 0.15;%(m)
g = 9.81;%(m/s^2)
v = 1.5;%(m/s)
E_k(Mu) = dsolve(diff(E,theta) == -2*Mu*E + m*g*r*cos(theta) - Mu*r*m*g*sin(theta),E(0) == 0)
%Solve a Single Differential Equation diff(E,theta) == -2*Mu*E + m*g*r*cos(theta) - Mu*r*m*g*sin(theta),E(0) == 0
E_k(Mu) = subs(E_k(Mu), theta, pi/2) %substitute theta with pi/2
E_k = E_k(Mu) == (1/2)*m*v^2 
solve(E_k,Mu) %Solve E_k(Mu) == (1/2)*m*v^2 to calculate Mu




