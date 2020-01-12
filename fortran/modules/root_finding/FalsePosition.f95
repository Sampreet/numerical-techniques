! Authors: Sampreet Kalita
! Created: 2020-01-02
! Updated: 2020-01-12

module FalsePosition
    ! Module to find roots of a univariate function using False Position Method.
    
    ! module parameters
    integer,        parameter       ::  NO_CONFIRMED_ROOT   = 0
    integer,        parameter       ::  FOUND_ROOT          = 1
    integer,        parameter       ::  FOUND_APPROX_ROOT   = 2

contains 
    subroutine find_root_in_interval(fn, xi_in, xf_in, et, root, ic, status)
        ! Find the (approximate) root of a univariate function in a given interval
        ! using the False Position Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! xi_in : real
        !   Initial x-value of the selected bracket.
        ! xf_in : real
        !   Final x-value of the selected bracket.
        ! et : real
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
        real,           intent(in)      ::  xi_in, xf_in, et

        ! variables
        real            ::  xi, xf
        real            ::  xint, curr_diff, max_diff

        ! output
        real,           intent(out)     ::  root
        integer,        intent(out)     ::  ic, status

        ! initialize values
        xi = xi_in
        xf = xf_in
        ic = 0
        status = NO_CONFIRMED_ROOT

        ! check initial values
        if (fn(xi) * fn(xf) > 0.0) then
            status = NO_CONFIRMED_ROOT
            return
        else if (fn(xi) == 0.0) then
            root = xi
            status = FOUND_ROOT
            return
        else if (fn(xf) == 0.0) then
            root = xf
            status = FOUND_ROOT
            return
        end if

        ! iterate till relative error reaches threshold
        do while (.true.)
            ! increment counter
            ic = ic + 1

            ! get intersection point
            xint = xi - fn(xi) * (xi - xf) / (fn(xi) - fn(xf))

            ! check relative error
            curr_diff = abs(xint - xi)
            max_diff = abs(xi) * et
            if (curr_diff < max_diff) then
                root = xi
                status = FOUND_APPROX_ROOT
                return
            end if

            ! update interval
            if (fn(xi) * fn(xint) < 0.0) then
                xf = xint
            else if (fn(xint) == 0.0) then
                xi = xint
                root = xi
                status = FOUND_ROOT
                return
            else 
                xi = xint
            end if
        end do
        
        root = xi
        status = FOUND_ROOT
    end subroutine find_root_in_interval

    subroutine find_all_roots(fn, xmin, xmax, step, et, roots, ic)
        ! Find the (approximate) roots of a univariate function in a given interval
        ! using the False Position Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! xmin : real
        !   Minimum value of x to check for roots.
        ! xmax : real
        !   Maximum value of x to check for roots.
        ! step : float (optional)
        !   Step-size for the x-axis interval.
        ! et : real
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
        real,           intent(in)      ::  xmin, xmax, step, et

        ! variables
        real            ::  xi, xf, root
        integer         ::  ii, status, rc
        character(:),   allocatable     ::  msg
        real,           dimension(:),   allocatable     ::  temp_roots

        ! output
        real,           intent(out),    dimension(:),   allocatable     ::  roots
        integer,        intent(out)     ::  ic

        ! initialize values
        xi = xmin
        xf = xmin + step - step * et
        rc = 0
        allocate(roots(rc))
        ic = 0

        do while (.true.)
            ! stop if maximum value of x is reached
            if (xi >= xmax) then
                exit
            end if
        
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
            if (status == FOUND_ROOT .or. status == FOUND_APPROX_ROOT) then
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

            ! update interval
            xi = xi + step
            xf = xf + step
            if (xf >= xmax) then
                xf = xmax
            end if 
        end do

        ! formatting for outputs
        10  format(T8, A, ' in [', F0.6, ', ', F0.6, '] : ', F0.6)
    end subroutine find_all_roots
end module FalsePosition