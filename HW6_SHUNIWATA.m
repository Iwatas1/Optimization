syms a
syms a1 a2 a3
h = [a1 a2;a2 a3];
g = {};
x = {};
H = {};
d_g = {};
d_x = {};
Q = [2 0; 0 1];
f = @(x) 1/2 * x.'* Q * x + 3;
H{1} = [1 0;0 1];
x{1} = [1;2];
g{1} = Q * x{1};
i = 1;
while true
    min = x{i}-a*H{i}*g{i};
    alpha = solve(diff(matlabFunction(f(min)),a));
    x{i+1} = double(x{i} - alpha * H{i} * g{i});
    g{i+1} = Q * x{i+1};
    d_x{i} = x{i+1} - x{i};
    d_g{i} = g{i+1} - g{i}; 
    G = [d_g{1:i}];
    X = [d_x{1:i}];
    B = struct2cell(solve(h * G - X, [a1 a2 a3]));
    C(1,1) = double(B{1});
    C(1,2) = double(B{2});
    C(2,1) = C(1,2);
    C(2,2) = double(B{3});
    H{i+1} = C;
    if norm(g{i + 1}) <= 1e-6
        disp(H{i +1})
        break
    end
    i = i + 1;
end
disp("H2 is "), disp(H{3});
disp(" and minimum of f(x1, x2) is at "); disp(x{end});
disp(" with value "); disp(f(x{end}));