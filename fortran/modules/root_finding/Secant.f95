! Authors: Sampreet Kalita
! Created: 2020-01-12
! Updated: 2020-01-12

module Secant
    ! Module to find roots of function using Secant Method.
    
    ! module parameters
    integer,        parameter       ::  NO_CONFIRMED_ROOT   = 0
    integer,        parameter       ::  FOUND_ROOT          = 1
    integer,        parameter       ::  FOUND_APPROX_ROOT   = 2
    integer,        parameter       ::  MAX_ITER_REACHED    = 3
    integer,        parameter       ::  EQUAL_FUNC_VALUES   = 5

contains 
    subroutine find_root_uni(fn, xi_in, xf_in, et, imax, root, ic, status)
        ! Find the (approximate) root of a univariate function
        ! using the Secant Method.
        ! 
        ! Input
        ! -----
        ! fn : function
        !   Given function in x.
        ! xi_in : real
        !   First initial x-value.
        ! xf_in : real
        !   Second initial x-value.
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
        !       5:  Function values are equal.

        implicit none

        ! input
        interface
            real function fn(x) result(fx)
                real,   intent(in)      ::  x
            end function fn
        end interface 
        real,           intent(in)      ::  xi_in, xf_in, et
        integer,        intent(in)      ::  imax

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
        if (fn(xi) == 0) then
            root = xi
            status = FOUND_ROOT
            return
        end if
        if (fn(xf) == 0) then
            root = xf
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

            ! no root if function values are equal
            if (fn(xi) == fn(xf)) then
                status = EQUAL_FUNC_VALUES
                return
            end if

            ! get intersection point
            xint = xf - fn(xi) * (xf - xi) / (fn(xf) - fn(xi))

            ! check relative error
            curr_diff = abs(xint - xi)
            max_diff = abs(xi) * et
            xi = xf
            xf = xint
            if (curr_diff < max_diff) then
                root = xf
                status = FOUND_APPROX_ROOT
                return
            end if
        
            ! check value at xf
            if (fn(xf) == 0) then
                root = xf
                status = FOUND_ROOT
                return
            endif
        end do

        root = xi
        status = FOUND_ROOT
    end subroutine find_root_uni
end module Secant