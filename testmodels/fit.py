#!/usr/bin/env python

import sncosmo 
import os
from astropy.table import Table, Column
from astropy.io import fits
import numpy as np

def lc(SNID, filename, location="./"):
        
    summaryfile = os.path.join(location, filename + "_HEAD.FITS")
    photofile = os.path.join(location, filename + "_PHOT.FITS")

                
    summary = Table(fits.open(summaryfile)[1].data)
    snpointers = summary[np.array(map(int,summary["SNID"]))==SNID]
    z = snpointers['REDSHIFT_FINAL']
    ptrobs_min = snpointers["PTROBS_MIN"]
    ptrobs_max = snpointers["PTROBS_MAX"]
                                        
    lc = Table(fits.open(photofile)[1].data[ptrobs_min - 1: ptrobs_max])
    lc.rename_column("FLUXCAL", "flux")
    lc.rename_column("FLUXCALERR","fluxerr")
    lc.rename_column("ZEROPT","ZP")
    lc.rename_column('FLT', 'band')
    zpsys = Column(['ab']*len(lc), name='ZPSYS') 
    lc.add_column(zpsys)
    #lc = photofile
    return z, lc

lcmerge = os.getenv('lcmerge')
print lcmerge
meta, lc = lc('2007nc', 'SDSS_allCandidates+BOSS', lcmerge)
print meta 
print lc.meta
print lc

model = sncosmo.Model('s11-2006jl')
model.set(z=meta)
res, fitted_model = sncosmo.fit_lc(lc, model, ['t0', 'amplitude'])
print fitted_model

