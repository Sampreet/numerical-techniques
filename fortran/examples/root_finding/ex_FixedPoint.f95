! Authors: Sampreet Kalita
! Created: 2020-01-02
! Updated: 2020-01-12

module func_FixedPoint
    ! Module for the demo univariate function for testing.

contains 
    real function gn(x) result(gx)
        ! Modified function for the demo function f(x) = x^2 - 5.
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
        gx = 2 + 1 / (x + 2)
    end function gn
end module func_FixedPoint

program main
    ! Program to test root_finding -> FixedPoint module.

    ! modules
    use FixedPoint
    use func_FixedPoint

    implicit none

    ! constants
    real            ::  xi      = 1, &
                        et      = 1e-6
    integer         ::  imax    = 1e6

    ! variables
    real            ::  root
    real,           dimension(:),   allocatable     ::  roots
    integer         ::  ic, status
    character(:),   allocatable     ::  msg

    ! call function
    write(*, 10) 'Fixed Point Method: Univariate'
    call find_root_uni(gn, xi, et, imax, root, ic, status)

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
    end select

    ! display
    if (status == FOUND_ROOT .or. status == FOUND_APPROX_ROOT) then
        write(*, 20) msg, xi, root, gn(root), ic 
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