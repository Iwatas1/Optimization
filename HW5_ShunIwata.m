%% HW5
% Shun Iwata
% 
% ID: 28699490
% 1,

x_0 = [3;-1;0;1];
x_1 = x_0 - F_inv(x_0)*grad(x_0);
while true
    if norm(x_0 - x_1)<=1e-6
        disp('f minimizes at ');
        disp(x_1);
        fprintf('and the value is %g', f(x_1));
        break
    end
    x_0 = x_1;
    x_1 = x_0 - F_inv(x_0)*grad(x_0);
end
% 2,

Q = [3,0,1;
    0,4,2;
    1,2,3];
% (a)
% Let  ${\vec{d} }^{\left(0\right)} =\left(1,0,0\right)$, then ${\left({\vec{d} 
% }^{\left(0\right)} \right)}^T Q\;{\vec{d} }^{\left(1\right)} =0$, so

d_0 = [1;0;0];
d_1 = null(d_0.' * Q);
%there are two vectors that are orthognal and satisfies the condition, so we choose on of them.
d_1 = d_1(:,1);
disp('d_1 is');disp(d_1);
%check if they are Q-conjugate
d_0.' * Q * d_1

d = [d_0, d_1];
%% 
% In 3 dimensional case, ${\vec{d} }^{\left(2\right)}$can be found by the cross 
% product of ${\left({\vec{d} }^{\left(0\right)} \right)}^T Q\;$ and ${\left({\vec{d} 
% }^{\left(1\right)} \right)}^T Q\;$, thus 

d_2 = (cross(d_0.' * Q, d_1.' * Q )).';
disp('d_2 is');disp(d_2);
%check if they are Q-conjugate
d_0.' * Q * d_2
d_1.' * Q * d_2
disp('Therefore, ');disp(d_0); disp(d_1);disp(d_2); disp(' are Q-conjugate vectors');
% (b)

x_0 = [0;0;0];
b = [-1;1;0];
d = [d d_2];
x =[];
for i = 1:3
    x(:,i) = x_0 - (d(:,i).' * (Q*x_0-b)* d(:,i))/(d(:,i).' * Q * d(:,i));
    x_0 = x(:,i);
end
A = 1/2 * x_0.' * Q * x_0 - x_0.' * b;
disp('minimizer of f(x) is at ');disp(x_0);
disp('and the minimum value is '); disp(A);
%%
function y =f(x)
y = (x(1) + 10*x(2))^2 + 5*(x(3) - x(4))^2 + (x(2) - 2*x(3))^4 + 10*(x(1) - x(4))^4;
end

function y = grad(x)
syms x1 x2 x3 x4
f_0(x1,x2,x3,x4) = (x1 + 10*x2)^2 + 5*(x3 - x4)^2 + (x2 - 2*x3)^4 + 10*(x1 - x4)^4;
v = [x1 ,x2, x3, x4];
g_f = gradient(f_0,v);
y = g_f(x(1),x(2),x(3),x(4));
end

function y = F_inv(x)
syms x1 x2 x3 x4
f_0(x1,x2,x3,x4) = (x1 + 10*x2)^2 + 5*(x3 - x4)^2 + (x2 - 2*x3)^4 + 10*(x1 - x4)^4;
v = [x1 ,x2, x3, x4];
h_f = hessian(f_0,v);
y = inv((h_f(x(1),x(2),x(3),x(4))));
end