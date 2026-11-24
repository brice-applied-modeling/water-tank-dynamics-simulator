# -*- coding: utf-8 -*-

"""Module that stores all engineering conversions necessary for numerical
computations."""

# =========================================
# Unit Conversions for Physical Properties
# =========================================

INCHES_PER_FOOT = 12  # convert feet to inches

# =========================================
# Unit Conversions for Water Properties
# =========================================

FT_PER_PSI = 2.31  # convert psi to ft of water
GAL_PER_CF = 7.48052  # convert cf to gal
GPM_PER_CFS = 448.831  # convert cfs to gpm
GPM_PER_MGD = 694.444  # convert MGD to gpm

# ======================================
# Unit Conversions for Loading
# ======================================

LBM_PER_GAL = 8.34  # convert gal of water to lbm of water
# Mass Loading(lb/day) = Flow(MGD) * Concentration(mg/L) * 8.34
# Chemical Dosing(mg/L) = Mass Loading (lb/day) / (Flow(MGD) * 8.34)
