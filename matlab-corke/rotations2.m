R1 = rot2(0);

R2 = rot2(2 * pi / 3);

axis([-2 2 -2 2], 'square');
hold on;

trplot2(R1, 'frame', '1', 'color', 'r');

trplot2(R2, 'frame', '2', 'color', 'b');