% Two-dimesional robot with two links
% and two revolute joints

clear;

links(1) = Link([0 0 2 0]);
links(2) = Link([0 0 1 0]);

robot = SerialLink(links, 'name', 'robot2D');

robot.plot([pi/3, pi/2]);