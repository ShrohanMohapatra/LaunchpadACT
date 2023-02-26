close all;
clear all;
clc;
size_trial = 40;
A = rand(size_trial, size_trial);
B = rand(size_trial, size_trial);
C0 = StrassenMatrixFunction(A, B);
C1 = A*B;
disp(norm(C1-C0))
function C = StrassenMatrixFunction(A, B)
    n_major = size(A);
    n0 = n_major(1);
    n1 = n_major(2);
    if n0 == 1 && n1 == 1
        C = [A(1, 1)*B(1, 1)];
    elseif n0 == n1 && mod(n0, 2) == 0
        A11 = A(1:n0/2, 1:n0/2);
        A12 = A(1:n0/2, n0/2+1:n0);
        A21 = A(n0/2+1:n0, 1:n0/2);
        A22 = A(n0/2+1:n0, n0/2+1:n0);
        B11 = B(1:n0/2, 1:n0/2);
        B12 = B(1:n0/2, n0/2+1:n0);
        B21 = B(n0/2+1:n0, 1:n0/2);
        B22 = B(n0/2+1:n0, n0/2+1:n0);
        M1 = StrassenMatrixFunction((A11+A22), (B11+B22));
        M2 = StrassenMatrixFunction((A21+A22), B11);
        M3 = StrassenMatrixFunction(A11, (B12-B22));
        M4 = StrassenMatrixFunction(A22, (B21-B11));
        M5 = StrassenMatrixFunction((A11+A12), B22);
        M6 = StrassenMatrixFunction((A21-A11), (B11+B12));
        M7 = StrassenMatrixFunction((A12-A22), (B21+B22));
        C11 = M1 + M4 - M5 + M7;
        C12 = M3 + M5;
        C21 = M2 + M4;
        C22 = M1 - M2 + M3 + M6;
        C = zeros([n0 n0]);
        for m = drange(1:n0/2)
            for n = drange(1:n0/2)
                C(m, n) = C11(m, n);
            end
        end
        for m = drange(1:n0/2)
            for n = drange(n0/2+1,n0)
                C(m, n) = C12(m, n-n0/2);
            end
        end
        for m = drange(n0/2+1:n0)
            for n = drange(1:n0/2)
                C(m, n) = C21(m-n0/2, n);
            end
        end
        for m = drange(n0/2+1:n0)
            for n = drange(n0/2+1:n0)
                C(m, n) = C22(m-n0/2, n-n0/2);
            end
        end
    elseif n0 == n1 && mod(n0, 2) == 1
        A1 = zeros([n0+1 n0+1]);
        B1 = zeros([n0+1 n0+1]);
        for k = drange(1:n0)
            for m = drange(1:n0)
                A1(k, m) = A(k, m);
                B1(k, m) = B(k, m);
            end
        end
        C1 = StrassenMatrixFunction(A1, B1);
        C = C1(1:n0, 1:n0);
    end
end