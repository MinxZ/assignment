x = -20:0.1:10;
l = -3;
t = 1.414;
f = (1/( (...
(2*pi)^(1/2)...
          )*t)...
       )*...
   exp(-((x-l).^2)/...
        (2*(t^2)));
plot (x,f)
hold on
t = 2;
f = (1/(((2*pi)^(1/2))*t))*exp(-((x-l).^2)/(2*(t^2)));
plot (x,f)
hold off