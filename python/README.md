# Python

## Prerequisites

Install `Python 3.7+` using the [Anaconda Distribution](https://www.anaconda.com/distribution/) for the relevant operating system.

After installation, clone this repository or download and extract it to a preferred location.

## Development

The folder structure of the repository is as follows:

```
python/
│───examples/
│   │───group_foo/
│   |   │───ex_ModuleBar.py
│   │   └───...
│   │   
|   └───...
│
│───modules/
│   │───group_foo/
│   │   │───ModuleBar.py
│   │   └───...
│   │   
|   └───...
│   
│───tests/
│   │───group_foo/
│   |   │───test_ModuleBar.py
│   │   └───...
│   │   
|   └───...
│
├───.gitignore
└───README.md
```

Navigate to the `python` folder (this) inside the repository in command line or terminal (replace `path\to` by the location where the repository is extracted):
```
cd path\to\numerical-techniques-master\python
```

> All subsequent operations are to be performed in this directory.

To run all unittests, use
```
python -m unittest discover tests
```

To run a specific example (replace `group_foo` and `ModuleBar` by the specific group and module names), use
```
python examples\group_foo\ex_ModuleBar.py
```

