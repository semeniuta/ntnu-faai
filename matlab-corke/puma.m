% PUMA 560 robot (6 DoF)

clear;

mdl_puma560;

pose_zero = p560.fkine([0, 0, 0, 0, 0, 0]);

disp('Pose in the zero configuration:');
disp(pose_zero);

T = SE3(0.5, -0.5, 0.25);
q = p560.ikine6s(T);

disp('Solution to the inverse kinematics problem:');
disp(q);

p560.plot(q);





