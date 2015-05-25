#!/usr/bin/env python

import os
import sncosmo

def snanadatafile(snanafileroot, filetype='head', location='./'):
    suffix = '_HEAD.FITS'
    if filetype == 'phot':
        suffix = '_PHOT.FITS'
    fname = snanafileroot + suffix
    return os.path.join(location, fname)
