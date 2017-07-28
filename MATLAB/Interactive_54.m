% Cyou Meikin 16B09909 Question No.54

disp('A baseball outfielder throws a baseball at a speed and an initial angle.')
disp('Input right data then you will know the kinetic energy of the baseball at the highest point of its trajectory.')

% Initialize
g = 9.81;                     % ass: Gravitational constant ? 9.81m/s^(-2)
m = input('Mass of Ball(kg): ');
while m <= 0
    disp('Please write a positive number for mass.')
    m = input('Mass of Ball(kg): ');
end
v = input('Initial speed(m/s): ');
while v <= 0 
    disp('Please write a positive number for speed.')
    v = input('Initial speed(m/s): ');
end
a = input('Initial angle(degree) to the horizontal: ');
while a <= 0
    disp('Make sure 0 < initial angle <= 90.')
    a = input('Initial angle(degree): ');
end
while a > 90
        disp('Make sure 0 < initial angle <= 90.')
        a = input('Initial angle(degree): ');
end
v_y_ini = v*sind(a);           % initial speed on y-axis
v_x = v*cosd(a);


% calculate speed on y-axis in respect to time
syms t;
v_y = v_y_ini - g*t;

% calculate time when the ball gets to the heightest point
t_highest = solve(v_y==0,t);

% calculate ball's height,kinetic energye when the ball gets to the heightest point
h_highest = height(t_highest,v_y_ini,g);
kinetic_energy_highest = (1/2)*m*v^2 - m*g*h_highest;

% Caculate the time ball hits the ground.
syms t;
h = height(t,v_y_ini,g);
t_0 = solve(h==0,t);
% t_0 is the time ball's height gets to be 0 (the initial time and the time
% ball hits the ground)

t_end = t_0(2);
t_end = double(t_end);
% t_end is the time point when ball hits the ground.

% Draw a diagram for trajectory.
t = 0:t_end/128:t_end;
s = v_x*t;
h = height(t,v_y_ini,g);
s_end = v_x*t_end;

ax = gca;
ax.XAxisLocation = 'origin';
ax.XLim = [0 s_end+0.01];% avoid error(xlim = [0 0])when a = 90
h_highest = double(h_highest);% to plot comet we can not use sym
ax.YLim = [0 h_highest];
axis equal;
title('Question NO.54');
ylabel('Height (m)');
xlabel('Horizontal distance (m)');
hold on
comet(s,h)
hold on
plot(s_end/2,h_highest,'ro','MarkerSize',8)
hold on
legend('trajectory','Highest point','Location','southoutside','Orientation','horizontal')
hold off

% Draw a diagram for 'Kinetic energy','Height','Highest point'.
t = 0:t_end/16:t_end;
h = height(t,v_y_ini,g);
kinetic_energy = (1/2)*m*v^2 - m*g*h;

figure
bar(t,kinetic_energy,'FaceColor','y')
title('Question NO.54')
ylabel('Kinetic energy (J)')
xlabel('Time (s)')
hold on
yyaxis right
plot(t,h,'-bo')
ylabel('Height (m)')
hold on 
plot(t_highest,h_highest,'ro','MarkerSize',12)
hold on
legend('Kinetic energy','Height','Highest point','Location','southoutside','Orientation','horizontal')
hold off

% Write an answer for the question.
fprintf('Mass of baseball = %d kg,Speed = %d m/s,Angle = %d degrees.\n',m,v,a);
kinetic_energy_highest = double(kinetic_energy_highest);
X = ['When the baseball gets to the highest point,its kinetic energy is ',num2str(kinetic_energy_highest),'J.'];
disp(X)