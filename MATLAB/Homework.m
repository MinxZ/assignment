a = 0:1:50;
k1 = (-1.5*20.0)/200;
k2 = -1*0.2/(8.617e-3*200);

b = exp(k1.*a);
ab = a.*b;

state = exp(k2.*a);
energy = exp(k2.*a).*a;




