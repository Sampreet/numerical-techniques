from wave_function import HarmonicOscillator1D as ho

eps_min = 0                 # Starting value of the dimensionless energy, epsilon
eps_max = 8                 # Ending value of epsilon
step_size_eps_ini = 1e-2    # Initial step-size for iteration of epsilon
step_size_eps_max = 1e-6    # Maximum step-size for iteration of epsilon
threshold_eps = 1           # Threshold to decrease step-size of epsilon
threshold_zero = 1e-3       # Threshold to consider a zero of the wavefunction 
range_x = 5                 # Range of the x-axis
step_size_x = 1e-2          # Precision of the x-axis 
display = True              # Option to display the plots during iteration
debug = True                # Option to debug the iteration/plotting process

# get the array containing the solution arrays with elements as psi(0), psi'(0) and epsilon values
sol = ho.get_solutions(eps_min, eps_max, step_size_eps_ini, step_size_eps_max, threshold_eps, threshold_zero, range_x, step_size_x, display, debug)

# plot the wavefunctions for the obtained solutions
ho.display_solutions(sol, range_x, step_size_x)