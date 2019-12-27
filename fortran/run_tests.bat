:: Authors: Sampreet Kalita
:: Created: 2019-12-27
:: Updated: 2019-12-27

:: Batch file to run tests.

@ECHO off

:: Create 'bin' and 'lib'
if not exist .\bin mkdir .\bin
if not exist .\lib mkdir .\lib

:: Tests for root finding methods
if not exist .\bin\root_finding mkdir .\bin\root_finding
if not exist .\lib\root_finding mkdir .\lib\root_finding

:: test Bisection Method
gfortran .\modules\root_finding\Bisection.f95 .\tests\root_finding\test_Bisection.f95 -J .\lib\root_finding\ -o .\bin\root_finding\out_Bisection.exe
call .\bin\root_finding\out_Bisection.exe