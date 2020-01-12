! Authors: Sampreet Kalita
! Created: 2020-01-12
! Updated: 2020-01-12

module func_NewtonRaphson
    ! Module for the demo univariate function for testing.

contains 
    real function fn(x) result(fx)
        ! Demo function 
        ! f(x) = - D/x^2 - A/B*e^(-x/B) + 6*C/x^7
        !
        ! Input
        ! -----
        ! x : real
        !   Value of the variable.
        ! 
        ! Output
        ! ------
        ! gx : real
        !   Value of the function at x.

        ! input
        real,   intent(in)  ::  x

        ! function
        fx = 8.99 * 1.6 / x**2 - 728.0 / 0.317 * exp(- x / 0.317) + 6 * 0.486 / x**7
    end function fn

    real function df(x) result(dfx)
        ! Derivative of function.
        ! df(x)/dx = 2*D/x^3 + A/B^2*e^(-x/B) - 42*C/x^8
        !
        ! Input
        ! -----
        ! x : real
        !   Value of the variable.
        ! 
        ! Output
        ! ------
        ! gx : real
        !   Value of the function at x.

        ! input
        real,   intent(in)  ::  x

        ! function
        dfx = - 2 * 8.99 * 1.6 / x**3 + 728.0 / 0.317**2 * exp(- x / 0.317) - 42 * 0.486 / x**8
    end function df
end module func_NewtonRaphson

program main
    ! Example program to use root_finding -> NewtonRaphson module.

    ! modules
    use NewtonRaphson
    use func_NewtonRaphson

    implicit none

    ! constants
    real            ::  xi      = 1, &
                        et      = 1e-3
    integer         ::  imax    = 1e6

    ! variables
    real            ::  root
    real,           dimension(:),   allocatable     ::  roots
    integer         ::  ic, status
    character(:),   allocatable     ::  msg

    ! call function
    write(*, 10) 'Newton-Raphson Method: Univariate'
    call find_root_uni(fn, df, xi, et, imax, root, ic, status)

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
        case (DERIVATIVE_ZERO)
            msg = 'Derivative function is zero'
    end select

    ! display
    if (status == FOUND_ROOT .or. status == FOUND_APPROX_ROOT) then
        write(*, 20) msg, xi, root, fn(root), ic 
    else
        write(*, 30) msg, xi
    end if

    ! formatting for outputs
    10  format(/, A)
    20  format(T8, A, ' with initial value ', F0.6, ': ', F0.6, &
            /, T8, 'Function value: ', F0.6, &
            /, T8, 'Iterations: ', I0)
    30  format(T8, A, ' with initial value ', F0.6)
end program main