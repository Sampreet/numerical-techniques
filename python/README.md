# Python

## Installation

Install `Python 3.7+` using the [Anaconda Distribution](https://www.anaconda.com/distribution/) for the relevant operating system.

## Extraction

After installation, clone this repository or download and extract it to a preferred location.

Navigate to the ```python``` folder (this) inside the repository in command line or terminal (replace ```path\to``` by the location where the repository is extracted):
```
cd path\to\numerical-techniques-master\python\
```

## CPU Execution

The folder structure of the repository is as follows:

```
python/
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

Execute the desired test file using (replace ```group_foo``` and ```test_ModuleBar.py``` with the respective folder name and filename):
```
python -m unittest tests\group_foo\test_ModuleBar.py
```

To run all tests, use
```
python -m unittest discover tests
```

## GPU Execution

A detailed guide to install PyCUDA for the GPU modules can be found in [my guide to GPU-ACCELERATED DEEP LEARNING (Keras, Theano, PyCUDA, Tensorflow)](https://github.com/Sampreet/install-guides/blob/master/languages/python/GPU-accelerated-deep-learning-Keras-Tensorflow-Theano-PyCUDA.md).

