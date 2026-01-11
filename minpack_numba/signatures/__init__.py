"""Signatures for functions passed to minpack functions."""

__all__ = [
    "MinpackSignature",
    "hybrd_sig",
    "hybrj_sig",
    "lmder_sig",
    "lmdif_sig",
    "lmstr_sig",
]

from minpack_numba.src.signatures import (
    MinpackSignature,
    hybrd_sig,
    hybrj_sig,
    lmder_sig,
    lmdif_sig,
    lmstr_sig,
)
