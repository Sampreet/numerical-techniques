! Authors: Sampreet Kalita
! Created: 2020-01-12
! Updated: 2020-01-12

module NewtonRaphson
    ! Module to find roots of function using Newton-Raphson Method.
    
    ! module parameters
    integer,        parameter       ::  NO_CONFIRMED_ROOT   = 0
    integer,        parameter       ::  FOUND_ROOT          = 1
    integer,        parameter       ::  FOUND_APPROX_ROOT   = 2
    integer,        parameter       ::  MAX_ITER_REACHED    = 3
    integer,        parameter       ::  DERIVATIVE_ZERO     = 4

contains 
    subroutine find_root_uni(fn, df, xi_in, et, imax, root, ic, status)
        ! Find the (approximate) root of a univariate function
        ! using the Newton-Raphson Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! df : function
        !   Derivative of the function in x.
        ! xi_in : real
        !   Initial x-value of the selected bracket.
        ! et : real
        !   Relative error threshold.
        ! imax : int
        !   Maximum number of iterations to consider.
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
        !       3:  Max. iterations reached.
        !       4:  Derivative function is zero.

        implicit none

        ! input
        interface
            real function fn(x) result(fx)
                real,   intent(in)      ::  x
            end function fn
            real function df(x) result(dfx)
                real,   intent(in)      ::  x
            end function df
        end interface 
        real,           intent(in)      ::  xi_in, et
        integer,        intent(in)      ::  imax

        ! variables
        real            ::  xi
        real            ::  xint, curr_diff, max_diff

        ! output
        real,           intent(out)     ::  root
        integer,        intent(out)     ::  ic, status

        ! initialize values
        xi = xi_in
        ic = 0
        status = NO_CONFIRMED_ROOT

        ! check initial values
        if (fn(xi) == 0) then
            root = xi
            status = FOUND_ROOT
            return
        end if

        ! iterate till maximum iterations is reached or
        ! relative error reaches threshold
        do while (.true.)
            ! increment counter
            ic = ic + 1

            ! check iteration threshold
            if (ic >= imax) then
                status = MAX_ITER_REACHED
                return
            end if

            ! no root if derivative is zero
            if (df(xi) == 0) then
                status = DERIVATIVE_ZERO
                return
            end if

            ! get intersection point
            xint = xi - fn(xi) / df(xi)

            ! check relative error
            curr_diff = abs(xint - xi)
            max_diff = abs(xi) * et
            xi = xint
            if (curr_diff < max_diff) then
                root = xi
                status = FOUND_APPROX_ROOT
                return
            end if
        
            ! check value at xi
            if (fn(xi) == 0) then
                root = xi
                status = FOUND_ROOT
                return
            endif
        end do

        root = xi
        status = FOUND_ROOT
    end subroutine find_root_uni
end module NewtonRaphson