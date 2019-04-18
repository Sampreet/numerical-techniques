from modules import HarmonicOscillator

range_x = 5             # Range of the x-axis
range_psi_0 = 1         # Range of the initial value psi(0)
range_dpsidx_0 = 1      # Range of the initial value psi'(0)
range_eps = 10          # Range of the dimensionless energy
step_size_x = 1e-2      # Precision of the x-axis 
step_size_psi_0 = 1     # Step size for iteration of the initial value psi(0) 
step_size_dpsidx_0 = 1  # Step size for iteration of the initial value psi'(0)
step_size_eps = 1e-2    # Step size for iteration of the dimensionless energy 
margin_zero = 1e-2      # Margin of error to consider while checking the zero of the wavefunction 
display = True          # Option to display the plots during iteration
debug = True            # Option to debug the iteration/plotting process

# get the array containing the solution arrays with elements as psi(0), psi'(0) and epsilon values
sol = HarmonicOscillator.get_solutions(range_x, range_psi_0, range_dpsidx_0, range_eps, step_size_x, step_size_psi_0, step_size_dpsidx_0, step_size_eps, margin_zero, display, debug)

# plot the wavefunctions for the obtained solutions
HarmonicOscillator.display_solutions(sol, range_x, step_size_x, debug)