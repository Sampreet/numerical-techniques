# Fortran

## Installation

Install `Fortran95` by installing [Code::Blocks with MinGW-Fortran](http://www.codeblocks.org/downloads/26) for the relevant operating system.

## Extraction

After installation, clone this repository or download and extract it to a preferred location.

Navigate to the ```fortran``` folder (this) inside the repository in command line or terminal (replace ```path\to``` by the location where the repository is extracted):
```
cd path\to\numerical-techniques-master\fortran\
```

## Execution

The folder structure of the repository is as follows:

```
fortran/
│───modules/
│   │───group_foo/
│   │   │───ModuleBar.f95
│   │   └───...
│   │   
|   └───...
│   
│───tests/
│   │───group_foo/
│   |   │───test_ModuleBar.f95
│   │   └───...
│   │   
|   └───...
│
├───.gitignore
├───README.md
└───run_tests.bat
```

Execute the desired test file using (replace ```group_foo``` and ```ModuleBar``` with the respective folder name and module name):
```
gfortran .\modules\group_foo\ModuleBar.f95 .\tests\group_foo\test_ModuleBar.f95 -J .\lib\group_foo\ -o .\bin\group_foo\out_ModuleBar.exe
call .\bin\group_foo\out_ModuleBar.exe
```

To run all tests, use
```
run_tests.bat
```