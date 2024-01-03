import numpy as np
from scipy.optimize import linprog


def simulate(n_sim : int, ub : int):
    assert ub >= 3, "Upper bound must be at least three by convex hull constraint"
    probs = {}
    for n_points in range(3, ub+1):
        prob = simulate_n(n_points, n_sim)
        probs[n_points] = prob
    return probs

# Returns simulated probability of center being in convex hull
def simulate_n(n_points : int, n_sim : int):
    count = 0
    for i in range(n_sim):
        P = sample(n_points)
        count += center_in_convex_hull(P)
    return count / n_sim


# Returns random sample of n points on unit sphere's surface
def sample(n_points : int):
    # TODO: Pick random point on sphere's surface n times
    P = 0
    return P


# Returns whether center is in the convex hull's center
def center_in_convex_hull(P : np.array):
    n_points = P.shape[0]
    c = np.zeros((n_points))
    A = P.T
    b = np.array([0,0,0])
    lp = linprog(c=c, A_eq=A, b_eq=b, bounds=(0,1))
    return lp.success


if __name__ == "__main__":
    simulate(10, 5)