# -*- coding: utf-8 -*-

"""Module that stores all engineering constants and conversions necessary for
numerical computations."""

# =================================
# Physical Constants
# =================================

GRAVITY_CONSTANT = 32.2 # f/sec^2
ATM_PRESSURE = 14.7 # lbf/sq-in


# ================================
# Water Properties
# ================================

DENSITY_WATER = 62.4 # lbm/cf
DENSITY_SEAWATER = 62.0 # lbm/cf


# ===============================
# Conversions
# ===============================

PSI_FT = 2.31 # convert psi to ft of water
CF_GAL = 7.48 # convert cf to gal
GAL_LBM = 8.34 # convert gal of water to lbm of water
# Mass Loading(lb/day) = Flow(MGD) * Concentration(mg/L) * 8.34
# Chemical Dosing(mg/L) = Mass Loading (lb/day) / (Flow(MGD) * 8.34)
CFS_GPM = 448.831 # convert cfs to gpm 
