clear; clc
ptAonLink1 = [0;0;2;1];
ptBonLink2 = [1;0;1;1];

A1 = create_A_matrix(2,3,0,0);
A2 = create_A_matrix(3,0,0,0);

T0_1 = A2;
T1_2 = A1 * A2;

actualAonLink0 = T0_1 * ptAonLink1;
acutalBonLink0 = T1_2 * ptBonLink2;

expectedAonLink0 = [2;0;5;1];
expectedBonLink1 = [6;0;4;1];