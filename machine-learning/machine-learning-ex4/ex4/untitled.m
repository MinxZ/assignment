syms z;
syms g(z);
g = 1.0 / (1.0 + exp(-z));
ee = diff(g,z);