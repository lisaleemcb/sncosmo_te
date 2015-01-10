DataFiles for SNCosmo unit tests
=================================

The SNANA fits format files were created by 
translating an SNANA 'version photometry' in
ASCII form containing 2 SN light curves into
the SNANA fits format. 

Procedure:
----------

(using SNANA v10_38m)
1. Added files in 1. to $SNDATA_ROOT/lcmerge 
2. Added inputfile to current directory 
3. run the code::

       > snana.exe inputfile

4. The outputfiles are created in the working directory


Files put into $SNDATA_ROOT/lcmerge
######################################
- RB_Test.README
- RB_Test.LIST
- RB_Test.IGNORE

Input File for SNANA
#####################
- inputfile

Actual curve files copied from SNANA/lcmerge
#############################################
These files were in $SNDATA_ROOT/lcmerge/SNLS_Ast06. 
- SNLS_Ast06_03D1ax.dat
- SNLS_Ast06_03D1aw.dat

Output Files defining the FITS format photometry version of SNANA
#################################################################
- snana_fits_PHOT.FITS
- snana_fits_HEAD.FITS
- snana_fits.README
- snana_fits.LIST
- snana_fits.IGNORE

