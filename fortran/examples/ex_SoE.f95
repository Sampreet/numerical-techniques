! Authors: Sampreet Kalita
! Created: 2022-08-03
! Updated: 2022-08-05

program ex_SoE
    ! Program to test SoE module

    ! modules
    use SoE

    implicit none

    ! constants 
    integer     ::  n_i , n_f, &
                    op  = PRINT_PRIMES

    ! variables
    integer,    dimension(:), allocatable   :: primes(:)

    ! input
    write (*, 10) 'Sieve of Eratosthenes: Primes in a given range'
    write (*, 20) 'Initial value: '
    read *, n_i
    write (*, 20) 'Final value: '
    read *, n_f

    ! call function
    call get_primes(n_i, n_f, op, primes)

    ! output formats
    10 format (/, A)
    20 format (T8, A)
    30 format (T12, A)
end program ex_SoE