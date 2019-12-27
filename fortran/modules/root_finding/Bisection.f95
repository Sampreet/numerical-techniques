! Authors: Sampreet Kalita
! Created: 2019-12-26
! Updated: 2019-12-27

module Bisection
    ! Module to find roots of a univariate function using Bisection Method.
    
    ! module parameters
    integer,    parameter   :: NO_CONFIRMED_ROOT    = 0
    integer,    parameter   :: FOUND_ROOT           = 1
    integer,    parameter   :: FOUND_APPROX_ROOT    = 2

contains 
    subroutine find_root_in_interval(fn, xi_in, xf_in, et_in, root, ic, status)
        ! Find the (approximate) root of a univariate function in a given interval using the Bisection Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! xi_in : real
        !   Initial x-value of the selected bracket.
        ! xf_in : real
        !   Final x-value of the selected bracket.
        ! et_in : real
        !   Relative error threshold.
        !
        ! Output
        ! ------
        ! root : real
        !   Found (approximate) root of the function.
        ! ic : integer
        !   Total count of iterations.
        ! status : integer
        !   Status of the root:
        !       0:  No confirmed root.
        !       1:  Found root.
        !       2:  Found approx. root.
        
        implicit none
        ! input
        interface
            real function fn(x) result(fx)
                real,   intent(in)      ::  x
            end function fn
        end interface 
        real,           intent(in)                      ::  xi_in, xf_in, et_in
        ! variables
        real,                           allocatable     ::  xi, xf, xm, et, curr_diff, max_diff
        ! output
        real,           intent(out),    allocatable     ::  root
        integer,        intent(out),    allocatable     ::  ic, status
        
        ! extract variabels
        xi  = xi_in
        xf  = xf_in
        et  = et_in

        ! initialize values
        ic  = 0
        status = 0

        ! check initial values
        if (fn(xi) * fn(xf) > 0.0) then
            status = 0
            return
        else if (fn(xi) == 0.0) then
            root = xi
            status = 1
            return
        else if (fn(xf) == 0.0) then
            root = xf
            status = 1
            return
        end if

        ! iterate till relative error reaches threshold
        do while (.true.)
            ! increment counter
            ic = ic + 1

            ! get mean
            xm = (xi + xf) / 2.0

            ! check relative error
            curr_diff = abs(xm - xi)
            max_diff = abs(xi) * et
            if (curr_diff < max_diff) then
                root = xi
                status = 2
                return
            end if

            ! update interval
            if (fn(xi) * fn(xm) < 0.0) then
                xf = xm
            else if (fn(xm) == 0.0) then
                xi = xm
                root = xi
                status = 1
                return
            else 
                xi = xm
            end if
        end do
        
        root = xi
        status = 1
    end subroutine find_root_in_interval

    subroutine find_all_roots(fn, xmin_in, xmax_in, step_in, et_in, roots, ic)
        ! Find the (approximate) roots of a univariate function in a given interval using the Bisection Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! xmin_in : real
        !   Minimum value of x to check for roots.
        ! xmax_in : real
        !   Maximum value of x to check for roots.
        ! step : float (optional)
        !   Step-size for the x-axis interval.
        ! et_in : real
        !   Relative error threshold.
        !
        ! Output
        ! ------
        ! roots : array
        !   Found (approximate) roots of the function.
        ! ic : integer
        !   Total count of iterations.
        
        implicit none
        ! input
        interface
            real function fn(x) result(fx)
                real,   intent(in)      ::  x
            end function fn
        end interface 
        real,           intent(in)                      ::  xmin_in, xmax_in, step_in, et_in
        ! variables
        real,                           allocatable     ::  xmin, xmax, step, et, xi, xf, root
        integer,                        allocatable     ::  ii, status, rc
        character(:),                   allocatable     ::  msg
        ! output
        real,           dimension(:),   allocatable     ::  roots, temp_roots
        integer,        intent(out),    allocatable     ::  ic
    
        ! initialize values
        xmin    = xmin_in
        xmax    = xmax_in
        step    = step_in
        et      = et_in

        ! initialize values
        xi      = xmin
        xf      = xmin + step - step * et
        rc      = 0
        allocate(roots(rc))
        ic      = 0

        do while (.true.)
            ! search for root in interval
            call find_root_in_interval(fn, xi, xf, et, root, ii, status)

            ! get root status
            select case (status)
                case (NO_CONFIRMED_ROOT)
                    msg = 'No confirmed root'
                case (FOUND_ROOT)
                    msg = 'Found root'
                case (FOUND_APPROX_ROOT)
                    msg = 'Found approx. root'
            end select

            ! update roots array if root found
            if (status /= 0) then
                allocate(temp_roots(rc + 1))
                temp_roots(1:rc) = roots
                temp_roots(rc + 1) = root
                deallocate(roots)
                allocate(roots(rc + 1))
                roots = temp_roots
                deallocate(temp_roots)
                rc = rc + 1
                ic = ic + ii
                write(*, 10) msg, xi, xf, root
            else
                ic = ic + 1
            end if

            ! stop if maximum value of x is reached
            if (xi >= xmax) then
                exit
            end if

            ! update interval
            xi = xi + step
            xf = xf + step
        end do

        ! formatting for outputs
        10  format(T8, A, ' in [', F0.6, ', ', F0.6, '] : ', F0.6)
    end subroutine find_all_roots
end module Bisection