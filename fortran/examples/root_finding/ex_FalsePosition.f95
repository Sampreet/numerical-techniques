! Authors: Sampreet Kalita
! Created: 2020-01-02
! Updated: 2020-01-12

module func_FalsePosition
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
end module func_FalsePosition

program main
    ! Program to test root_finding -> FalsePosition module.

    ! modules
    use FalsePosition
    use func_FalsePosition

    implicit none

    ! constants
    real            ::  xi      = 0, &
                        xf      = 1, &
                        et      = 1e-6, &
                        xmin    = -1e1, &
                        xmax    = 1e1, &
                        step    = 1e0

    ! variables
    real            ::  root
    real,           dimension(:),   allocatable     ::  roots
    integer         ::  ic, status
    character(:),   allocatable     ::  msg

    ! call function
    write(*, 10) 'False Position Method: Root in Interval'
    call find_root_in_interval(fn, xi, xf, et, root, ic, status)

    ! get root status
    select case (status)
        case (NO_CONFIRMED_ROOT)
            msg = 'No confirmed root'
        case (FOUND_ROOT)
            msg = 'Found root'
        case (FOUND_APPROX_ROOT)
            msg = 'Found approx. root'
    end select

    ! display
    if (status == FOUND_ROOT .or. status == FOUND_APPROX_ROOT) then
        write(*, 20) xi, xf, msg, root, fn(root), ic 
    else
        write(*, 30) msg, xi, xf
    end if

    ! call function
    write(*, 10) 'False Position Method: All Roots'
    call find_all_roots(fn, xmin, xmax, step, et, roots, ic)

    ! display
    if (size(roots) /= 0) then
        write(*, 40) ic
    else 
        write(*, 30) 'No root found', xmin, xmax
    end if

    ! formatting for outputs
    10  format(/, A)
    20  format(T8, 'Interval: [', F0.6, ', ', F0.6, ']', &
            /, T8, A, ': ', F0.6, &
            /, T8, 'Function value: ', F0.6, &
            /, T8, 'Iterations: ', I0)
    30  format(T8, A, ' in [', F0.6, ', ', F0.6, ']')
    40  format(T8, 'Iterations: ', I0)
end program main