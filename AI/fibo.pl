fib(0, 0).      % Base case 1
fib(1, 1).      % Base case 2

fib(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, F1),
    fib(N2, F2),
    F is F1 + F2.
