! Authors: Sampreet Kalita
! Created: 2020-01-12
! Updated: 2020-01-12

module func_Secant
    ! Module for the demo univariate function for testing.

contains 
    real function fn(x) result(fx)
        ! Demo univariate function for testing.
        !
        ! Input
        ! -----
        ! x : real
        !   Value of the variable.
        ! 
        ! Output
        ! ------
        ! fx : real
        !   Value of the function at x.

        ! input
        real,   intent(in)  ::  x

        ! function
        fx = exp(2*x) - exp(x) - 2
    end function fn
end module func_Secant

program main
    ! Program to test root_finding -> Secant module.

    ! modules
    use Secant
    use func_Secant

    implicit none

    ! constants
    real            ::  xi      = 0, &
                        xf      = 1, &
                        et      = 1e-6
    integer         ::  imax    = 1e6

    ! variables
    real            ::  root
    integer         ::  ic, status
    character(:),   allocatable     ::  msg

    ! call function
    write(*, 10) 'Secant Method: Univariate'
    call find_root_uni(fn, xi, xf, et, imax, root, ic, status)

    ! get root status
    select case (status)
        case (NO_CONFIRMED_ROOT)
            msg = 'No confirmed root'
        case (FOUND_ROOT)
            msg = 'Found root'
        case (FOUND_APPROX_ROOT)
            msg = 'Found approx. root'
        case (MAX_ITER_REACHED)
            msg = 'Max. iterations reached'
        case (EQUAL_FUNC_VALUES)
            msg = 'Function values are equal'
    end select

    ! display
    if (status == FOUND_ROOT .or. status == FOUND_APPROX_ROOT) then
        write(*, 20) xi, xf, msg, root, fn(root), ic 
    else
        write(*, 30) msg, xi, xf
    end if

    ! formatting for outputs
    10  format(/, A)
    20  format(T8, 'Initial values: ', F0.6, ' and ', F0.6, &
            /, T8, A, ': ', F0.6, &
            /, T8, 'Function value: ', F0.6, &
            /, T8, 'Iterations: ', I0)
    30  format(T8, A, ' with initial values ', F0.6, ' and ', F0.6)
end program main