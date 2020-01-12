# Fortran

## Prerequisites

Install `Fortran95` by installing [Code::Blocks with MinGW-Fortran](http://www.codeblocks.org/downloads/26) for the relevant operating system.

After installation, clone this repository or download and extract it to a preferred location.

## Development

The folder structure of the repository is as follows:

```
fortran/
│───examples/
│   │───group_foo/
│   │   │───ex_ModuleBar.f95
│   │   └───...
│   │   
|   └───...
│   
│───modules/
│   │───group_foo/
│   |   │───ModuleBar.f95
│   │   └───...
│   │   
|   └───...
│
├───.gitignore
└───README.md
```

Navigate to the `fortran` folder (this) inside the repository in command line or terminal (replace `path\to` by the location where the repository is extracted):
```
cd path\to\numerical-techniques-master\fortran
```

> All subsequent operations are to be performed in this directory.

Create folders `bin` and `lib` inside the `fortran` directory.

Execute the desired test file using (replace `group_foo` and `ModuleBar` with the respective folder name and module name):
```
gfortran .\modules\group_foo\ModuleBar.f95 .\examples\group_foo\ex_ModuleBar.f95 -J .\lib\ -o .\bin\out.exe
call .\bin\out.exe
```