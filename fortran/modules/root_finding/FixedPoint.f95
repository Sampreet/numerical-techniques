! Authors: Sampreet Kalita
! Created: 2020-01-02
! Updated: 2020-01-12

module FixedPoint
    ! Module to find roots of a function using FixedPoint Method.
    
    ! module parameters
    integer,        parameter       ::  NO_CONFIRMED_ROOT   = 0
    integer,        parameter       ::  FOUND_ROOT          = 1
    integer,        parameter       ::  FOUND_APPROX_ROOT   = 2
    integer,        parameter       ::  MAX_ITER_REACHED    = 3

contains 
    subroutine find_root_uni(gn, xi_in, et, imax, root, ic, status)
        ! Find the (approximate) root of a univariate function
        ! using the Fixed Point Method.
        ! 
        ! Input
        ! -----
        ! gn : function
        !   Modified function prepared as g(x) = x modified
        !   from the given function f(x).
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
        
        implicit none

        ! input
        interface
            real function gn(x) result(gx)
                real,   intent(in)      ::  x
            end function gn
        end interface 
        real,           intent(in)      ::  xi_in, et
        integer,        intent(in)      ::  imax

        ! variables
        real            ::  xi
        real            ::  xnew, curr_diff, max_diff

        ! output
        real,           intent(out)     ::  root
        integer,        intent(out)     ::  ic, status

        ! initialize values
        xi = xi_in
        ic = 0
        status = NO_CONFIRMED_ROOT

        ! check initial values
        if (gn(xi) == xi) then
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

            ! update value
            xnew = gn(xi)

            ! check relative error
            curr_diff = abs(xnew - xi)
            max_diff = abs(xi) * et
            xi = xnew
            if (curr_diff < max_diff) then
                root = xi
                status = FOUND_APPROX_ROOT
                return
            end if
        
            ! check value at xi
            if (gn(xi) == xi) then
                root = xi
                status = FOUND_ROOT
                return
            endif
        end do
        
        root = xi
        status = FOUND_ROOT
    end subroutine find_root_uni
end module FixedPoint