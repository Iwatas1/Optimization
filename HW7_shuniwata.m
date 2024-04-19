%% Homework 7 
% Shun Iwata
% 
% ID: 28699490
% 1,

g = {};
x = {};
H = {};
d = {};
d_g = {};
d_x = {};
Q = [2 0; 0 1];
f = @(x) 1/2 * x.'* Q * x + 3;
H{1} = [1 1;1 2];
x{1} = [1;2];
g{1} = Q * x{1};
i = 1;
while true
    if norm(g{i}) <= 1e-6
        disp(sprintf('Minimizer at (%d, %d) ', x{i}));
        fprintf('and the value is %3.3f', f(x{i}));
        break
    end
    d{i} = -H{i} * g{i};
    alpha = -(g{i}.' * d{i})/(d{i}.' * Q * d{i});
    x{i+1} = x{i} + alpha * d{i};
    g{i+1} = Q * x{i+1};
    d_x{i} = alpha * d{i};
    d_g{i} = g{i+1} - g{i};
    H{i+1} = H{i} + ((d_x{i} - H{i}*d_g{i})*(d_x{i} - H{i}*d_g{i}).')/(d_g{i}.' * (d_x{i} - H{i} * d_g{i}));
    i = i + 1; 
end
% 2,

A = [0.3 0.1;0.4 0.2; 0.3 0.7];
b = [5;3;4];
x = inv(A.' * A) * A.' * b;
fprintf("%3.3f pounds of first type of concrete, and %3.3f pounds of secong type of concrete.", x(1), x(2));