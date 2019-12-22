#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Sampreet Kalita
# Created: 2019-08-07
# Updated: 2019-12-22

"""Module to find the integration of a given function using Runge-Kutta Method using GPU."""

# dependencies 
from pycuda.compiler import SourceModule

import pycuda.autoinit
import pycuda.driver as cuda