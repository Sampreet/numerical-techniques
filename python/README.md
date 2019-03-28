# Python

## Installation

Install Python using the [Anaconda Distribution](https://www.anaconda.com/distribution/) for the relevant operating system.

## Extraction

After installation, download this repository as .zip and extract it to a preferred location.

Navigate to the ```python``` folder (this) inside the repository in command line or terminal (replace ```path\to``` by the location where the repository is extracted):
```
cd path\to\numerical-techniques-master\python\
```

## Execution

The folder structure of the repository is as follows:

```
--| module-group
    --| modules
        -- __init__.py
        -- module_foo.py
        -- ...
    --  demo_module_foo.py
    --  ...
```

Execute the desired test file using (replace ```test_module_foo.py``` with the test filename):
```
python module-group\test_module_foo.py
```