from sympy import *

print("-"*72)
print("Structure problem in the reference configuration (S)")
print("-"*72)

# Declare useful symbols
X, Y, t = symbols('x[0] x[1] t')
A, rho_S, rho_F, mu, lam, eta = symbols('A rho_S rho_F mu lambda eta')

# Define a suitable solution field for the solid displacement
U_S = Matrix([0.0,
              -A*sin(pi*t)*sin(pi*X)*2*Y])
print("U_S =\n%s" % U_S)

# The kinematics of the motion are then described as follows
I = Matrix([[1, 0], [0, 1]])
Grad_U_S = Matrix([[simplify(diff(U_S[0], X)), simplify(diff(U_S[0], Y))],
                   [simplify(diff(U_S[1], X)), simplify(diff(U_S[1], Y))]])
F_S = I + Grad_U_S
C = F_S.T*F_S
E = Rational(1, 2)*(C - I)

# Compute the terms in (S) defined by U_S
Sigma_S = F_S*(2*mu*E + lam*E.trace()*I)
Div_Sigma_S = Matrix([simplify(diff(Sigma_S[0], X) + diff(Sigma_S[1], Y)),
                      simplify(diff(Sigma_S[2], X) + diff(Sigma_S[3], Y))])
d2U_S_dt2 = Matrix([simplify(diff(U_S[0], t, 2)), simplify(diff(U_S[1], t, 2))])

# Use (S) to determine B_S
B_S = rho_S*d2U_S_dt2 - Div_Sigma_S
print("B_S =\n%s" % B_S)

# Check if (S) is satisfied
check_S = rho_S*d2U_S_dt2 - Div_Sigma_S - B_S
print("check_S =\n%s" % Matrix([simplify(check_S[0]), simplify(check_S[1])]))

print("-"*72)
print("Mesh problem in the reference configuration (M)")
print("-"*72)

# Define a suitable solution field for the mesh displacement
U_M = Matrix([0.0,
              -A*sin(pi*t)*sin(pi*X)*2*(1 - Y)])
print("U_M =\n%s" % U_M)

# Check whether U_S = U_M on the interface
check_M = U_S.subs(Y, Rational(1, 2)) - U_M.subs(Y, Rational(1, 2))
print("check_M =\n%s" % check_M)

# Compute some kinematic quantities defined by U_M to be used in
# pulling-back the Navier-Stokes equations to the reference fluid
# configuration
Grad_U_M = Matrix([[simplify(diff(U_M[0], X)), simplify(diff(U_M[0], Y))],
                   [simplify(diff(U_M[1], X)), simplify(diff(U_M[1], Y))]])
F_M = I + Grad_U_M
J_M = F_M.det()
F_M_inv = F_M.inv()
V_M = Matrix([simplify(diff(U_M[0], t)),
              simplify(diff(U_M[1], t))])

print("-"*72)
print("Fluid problem in the reference configuration (F)")
print("-"*72)

# Define the solution field for the fluid velocity based on the time
# derivative of the solid velocity on the interface to enforce the
# no-slip condition
V_F = Matrix([diff(U_S[0].subs(Y, Rational(1, 2)), t),
              diff(U_S[1].subs(Y, Rational(1, 2)), t)])
print("V_F =\n%s" % V_F)

# Check whether this functional form is divergence-free in the
# reference configuration
Div_term = J_M*F_M_inv*V_F
Div_V_F = simplify(diff(Div_term[0], X) + diff(Div_term[1], Y))
print("check_F_1 =\n%s" % Div_V_F)

# Construct a part of the fluid stress, to determine the fluid
# pressure based on equality with the solid stress at the interface
P_F = symbols('P_F')
N_F = Matrix([0, -1.0])
Grad_V_F = Matrix([[simplify(diff(V_F[0], X)), simplify(diff(V_F[0], Y))],
                   [simplify(diff(V_F[1], X)), simplify(diff(V_F[1], Y))]])

Sigma_F = J_M*(eta*(Grad_V_F*F_M_inv + F_M_inv.T*Grad_V_F.T) - P_F*I)*F_M_inv.T
Sigma_F_int_dot_N = (N_F.T*Sigma_F*N_F).subs(Y, Rational(1, 2))
Sigma_S_int_dot_N = (N_F.T*Sigma_S*N_F).subs(Y, Rational(1, 2))

# Solve for the fluid pressure to satisfy the condition that the solid
# and fluid stresses are equal on the boundary
P_F_sol = solve(Eq(Sigma_F_int_dot_N[0], Sigma_S_int_dot_N[0]), P_F)
print("P_F =\n%s" % simplify(P_F_sol))

# Insert this pressure field into the definition of the fluid stress
Sigma_F = Sigma_F.subs(P_F, simplify(P_F_sol)[0])
print("check_F_2 =")
print(simplify(((N_F.T*Sigma_F*N_F - N_F.T*Sigma_S*N_F)[0].subs(Y, Rational(1, 2)))))

# Construct terms of the Navier-Stokes equations starting with the
# time derivative of the velocity
dV_F_dt = Matrix([simplify(diff(V_F[0], t)), simplify(diff(V_F[1], t))])

# Divergence of the stress field
Div_Sigma_F = Matrix([simplify(diff(Sigma_F[0], X) + diff(Sigma_F[1], Y)),
                      simplify(diff(Sigma_F[2], X) + diff(Sigma_F[3], Y))])

# Use (F) to determine B_F
B_F = rho_F*J_M*(dV_F_dt + Grad_V_F*F_M_inv*(V_F - V_M)) - Div_Sigma_F
print("B_F =\n%s" % B_F)

# Check if (F) is satisfied
check_F_3 = rho_S*d2U_S_dt2 - Div_Sigma_S - B_S
print("check_F_3 =\n%s" % Matrix([simplify(check_F_3[0]), simplify(check_F_3[1])]))
