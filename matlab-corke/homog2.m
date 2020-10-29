Origin = SE2(0, 0, 0);

T1 = SE2(1., 1., pi/4);

T2 = SE2(0, 0.5, -pi/4);

axis([-5 5 -5 5], 'square');
hold on;

trplot2(Origin, 'frame', '0');

trplot2(T1, 'frame', '1');

trplot2(T2, 'frame', '2', 'color', 'r');

trplot2(T1 * T2, 'frame', '3', 'color', 'g');

