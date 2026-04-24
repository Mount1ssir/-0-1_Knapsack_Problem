int n = ...;
int W = ...; // Capacity
int u[1..n] = ...; // Utilities
int w[1..n] = ...; // Weights

dvar boolean x[1..n]; // Decision variables

maximize sum(i in 1..n) u[i] * x[i];

subject to {
  sum(i in 1..n) w[i] * x[i] <= W;
}