"""A numba wrapper for the minpack library."""

__version__ = "0.1.0"

from ._chkder import chkder
from ._dpmpar import dpmpar
from ._hybrd import hybrd, hybrd1, hybrd1_, hybrd_
from ._hybrj import hybrj, hybrj1, hybrj1_, hybrj_
from ._lmder import lmder, lmder1, lmder1_, lmder_
from ._lmdif import lmdif, lmdif1, lmdif1_, lmdif_
from ._lmstr import lmstr, lmstr1, lmstr1_, lmstr_

__all__ = [
    "chkder",
    "dpmpar",
    "hybrd",
    "hybrd1",
    "hybrd1_",
    "hybrd_",
    "hybrj",
    "hybrj1",
    "hybrj1_",
    "hybrj_",
    "lmder",
    "lmder1",
    "lmder1_",
    "lmder_",
    "lmdif",
    "lmdif1",
    "lmdif1_",
    "lmdif_",
    "lmstr",
    "lmstr1",
    "lmstr1_",
    "lmstr_",
]
