! Authors: Sampreet Kalita
! Created: 2019-12-26
! Updated: 2019-12-27

module func
    ! Module for the demo univariate function for testing.

contains 
    real function fn(x) result(fx)
        ! Demo univariate function for testing.
        
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
        fx = x**3 + 94*x**2 - 389*x + 294
    end function fn
end module func

program main
    ! Program to test root_finding -> Bisection module.

    ! modules
    use Bisection
    use func

    implicit none
    ! constants
    real    ::  xi      = 5e-1, &
                xf      = 2e0, &
                et      = 1e-4, &
                xmin    = -1e3, &
                xmax    = 1e3, &
                step    = 1e0
    ! variables
    real,                           allocatable     ::  root
    real,           dimension(:),   allocatable     ::  roots
    integer,                        allocatable     ::  ic, status
    character(:),                   allocatable     ::  msg

    ! test find_root_in_interval
    write(*, 10) 'Bisection Method: Root in Interval'
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
    if (status /= 0) then
        write(*, 20) xi, xf, msg, root, fn(root), ic 
    else
        write(*, 30) msg, xi, xf
    end if

    ! test find_all_roots
    write(*, 10) 'Bisection Method: All Roots'
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