"""Signatures for the functions passed to the minpack functions."""

from __future__ import annotations

__all__ = [
    "MinpackSignature",
    "hybrd_sig",
    "hybrj_sig",
    "lmder_sig",
    "lmdif_sig",
    "lmstr_sig",
]

from typing import TYPE_CHECKING

from numba import types

if TYPE_CHECKING:
    from numba.core.typing import Signature

_ptr_double = types.CPointer(types.float64)
_ptr_int = types.CPointer(types.int32)


class MinpackSignature:
    """Signatures for the functions passed to the minpack functions."""

    @staticmethod
    def hybrd(udata_type: types.Type = types.voidptr) -> Signature:
        """Signature for `fcn` argument of [hybrd][minpack_numba.hybrd] like functions.

        Parameters
        ----------
        udata_type : types.Type, optional
            The type of the user data, by default types.voidptr

        Returns
        -------
        Signature
            The signature of the function

        """
        return types.void(
            types.int32,  # n
            _ptr_double,  # *x
            _ptr_double,  # *fvec
            _ptr_int,  # *iflag
            udata_type,  # udata
        )

    @staticmethod
    def hybrj(udata_type: types.Type = types.voidptr) -> Signature:
        """Signature for `fcn` argument of [hybrj][minpack_numba.hybrj] like functions.

        Parameters
        ----------
        udata_type : types.Type, optional
            The type of the user data, by default types.voidptr

        Returns
        -------
        Signature
            The signature of the function

        """
        return types.void(
            types.int32,  # n
            _ptr_double,  # *x
            _ptr_double,  # *fvec
            _ptr_double,  # *fjac
            types.int32,  # ldfjac
            _ptr_int,  # *iflag
            udata_type,  # udata
        )

    @staticmethod
    def lmdif(udata_type: types.Type = types.voidptr) -> Signature:
        """Signature for `fcn` argument of [lmdif][minpack_numba.lmdif] like functions.

        Parameters
        ----------
        udata_type : types.Type, optional
            The type of the user data, by default types.voidptr

        Returns
        -------
        Signature
            The signature of the function

        """
        return types.void(
            types.int32,  # m
            types.int32,  # n
            _ptr_double,  # *x
            _ptr_double,  # *fvec
            _ptr_int,  # *iflag
            udata_type,  # udata
        )

    @staticmethod
    def lmder(udata_type: types.Type = types.voidptr) -> Signature:
        """Signature for `fcn` argument of [lmder][minpack_numba.lmder] like functions.

        Parameters
        ----------
        udata_type : types.Type, optional
            The type of the user data, by default types.voidptr

        Returns
        -------
        Signature
            The signature of the function

        """
        return types.void(
            types.int32,  # m
            types.int32,  # n
            _ptr_double,  # *x
            _ptr_double,  # *fvec
            _ptr_double,  # *fjac
            types.int32,  # ldfjac
            _ptr_int,  # *iflag
            udata_type,  # udata
        )

    @staticmethod
    def lmstr(udata_type: types.Type = types.voidptr) -> Signature:
        """Signature for `fcn` argument of [lmstr][minpack_numba.lmstr] like functions.

        Parameters
        ----------
        udata_type : types.Type, optional
            The type of the user data, by default types.voidptr

        Returns
        -------
        Signature
            The signature of the function

        """
        return types.void(
            types.int32,  # m
            types.int32,  # n
            _ptr_double,  # *x
            _ptr_double,  # *fvec
            _ptr_double,  # *fjrow
            _ptr_int,  # *iflag
            udata_type,  # udata
        )


# func
hybrd_sig = MinpackSignature.hybrd()
"""
Signature for `fcn` argument of [hybrd][minpack_numba.hybrd] &
[hybrd1][minpack_numba.hybrd1].

(n: int32, x: float64*, fvec: float64*, iflag: int32*, udata: void*) -> none
"""

# fcn_hybrj
hybrj_sig = MinpackSignature.hybrj()
"""
Signature for `fcn` argument of [hybrj][minpack_numba.hybrj] &
[hybrj1][minpack_numba.hybrj1].

(n: int32, x: float64*, fvec: float64*, fjac: float64*, ldfjac: int32, iflag: int32*,
    udata: void*) -> none
"""

# func2
lmdif_sig = MinpackSignature.lmdif()
"""
Signature for `fcn` argument of [lmdif][minpack_numba.lmdif] &
[lmdif1][minpack_numba.lmdif1].

(m: int32, n: int32, x: float64*, fvec: float64*, iflag: int32*, udata: void*)
    -> none
"""

# fcn_lmder
lmder_sig = MinpackSignature.lmder()
"""
Signature for `fcn` argument of [lmder][minpack_numba.lmder] &
[lmder1][minpack_numba.lmder1].

(m: int32, n: int32, x: float64*, fvec: float64*, fjac: float64*, ldfjac: int32,
    iflag: int32*, udata: void*) -> none
"""

# fcn_lmstr
lmstr_sig = MinpackSignature.lmstr()
"""
Signature for `fcn` argument of [lmstr][minpack_numba.lmstr] &
[lmstr1][minpack_numba.lmstr1].

(m: int32, n: int32, x: float64*, fvec: float64*, fjrow: float64*, iflag: int32*,
    udata: void*) -> none
"""
