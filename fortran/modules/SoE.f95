! Authors: Sampreet Kalita
! Created: 2022-08-03
! Updated: 2022-08-05

module SoE
    ! Module to implement sieve of Eratosthenes

    ! module parameters for output
    integer,    parameter   :: PRINT_NONE   = 0
    integer,    parameter   :: PRINT_COUNT  = 1
    integer,    parameter   :: PRINT_PRIMES = 2

contains
    subroutine get_primes(n_i, n_f, op, primes)
        ! Obtain all primes in a given range
        ! using the sieve of Eratosthenes
        ! 
        ! Input
        ! -----
        ! n_i : integer
        !   Initial value of range.
        ! n_f : integer
        !   Final value of range.
        ! op : integer
        !   Option for console output
        !
        ! Output
        ! ------
        ! primes : array
        !   All primes from n_i to n_f
        
        implicit none

        ! input
        integer,    intent(in)      ::  n_i, n_f, op

        ! variables
        integer     ::  i, j, prime_counter
        logical,    dimension(:),   allocatable     :: is_prime
        integer,    dimension(:),   allocatable,    intent(out)     :: primes(:)

        ! initialize values
        i = 2
        allocate(is_prime(n_f))
        is_prime(1) = .false.
        is_prime(2:n_f) = .true.
        prime_counter = n_f - n_i + 1

        ! corner cases
        if (n_f <= 0) then 
            stop 'Final value should be greater than 0'
        end if
        if (n_i > n_f) then
            stop 'Initial value should be less than or equal to final value'
        end if
        if (n_i <= 1) then
            prime_counter = n_f - 1
        end if

        ! main loop
        do while (.true.)
            ! stop if sqrt(n_f) is reached
            if (i > sqrt(real(n_f))) then
                exit
            end if
            ! if not marked
            if (is_prime(i)) then
                ! mark all multiples from 2i to n
                j = 2 * i
                do while (.true.)
                    ! stop if end of array
                    if (j > n_f) then 
                        exit
                    end if
                    ! if not marked
                    if (j >= 1 .and. is_prime(j)) then
                        ! mark
                        is_prime(j) = .false.
                        if (j >= n_i) then
                            ! update prime counter
                            prime_counter = prime_counter - 1
                        end if
                    end if
                    ! update counter
                    j = j + i
                end do
            end if
            ! update counter
            i = i + 1
        end do

        ! initialize list
        allocate(primes(prime_counter))
        ! save all primes
        i = 2
        j = 1
        do while (.true.)
            ! stop if end is reached
            if (i > n_f) then
                exit
            end if
            ! update
            if (i >= n_i .and. is_prime(i)) then
                primes(j) = i
                ! print
                if (op == PRINT_PRIMES) then
                    write (*, 20) j, i
                end if
                ! update counter
                j = j + 1
            end if
            i = i + 1
        end do

        ! print
        if (op == PRINT_COUNT .or. op == PRINT_PRIMES) then
            write (*, 10) n_i, n_f, prime_counter
        end if

        ! output formats
        10 format ('Total primes from ', I0, ' to ', I0, ': ', I0)
        20 format (T8, '#', I0, ': ', I0)
    end subroutine get_primes
end module SoE
