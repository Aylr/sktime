# -*- coding: utf-8 -*-
"""BaseEstimator interface to sktime dtw distances in distances module."""

__author__ = ["fkiraly"]

from typing import Union

import numpy as np
from deprecated.sphinx import deprecated

import sktime.dists_kernels.distances.dtw as new_class_loc


# TODO: remove file in v0.15.0
@deprecated(
    version="0.13.4",
    reason="DtwDist has moved and this import will be removed in 0.15.0. Import from sktime.dists_kernels.distances",  # noqa: E501
    category=FutureWarning,
)
class DtwDist(new_class_loc.DtwDist):
    r"""Interface to sktime native dtw distances, with derivative or weighting.

    Interface to simple dynamic time warping (DTW) distance,
    and the following weighted/derivative versions:
    WDTW - weighted dynamic tyme warping
    DDTW - derivative dynamic time warping
    WDDTW - weighted derivative dynamic time warping

    DTW:
    Originally proposed in [1]_, DTW computes the distance between two time series by
    considering their alignments during the calculation. This is done by measuring
    the pointwise distance (normally using Euclidean) between all elements of the two
    time series and then using dynamic programming to find the warping path
    that minimises the total pointwise distance between realigned series.

    DDTW is an adaptation of DTW originally proposed in [2]_. DDTW attempts to
    improve on dtw by better account for the 'shape' of the time series.
    This is done by considering y axis data points as higher level features of 'shape'.
    To do this the first derivative of the sequence is taken, and then using this
    derived sequence a dtw computation is done.

    WDTW was first proposed in [3]_, it adds a multiplicative weight penalty based on
    the warping distance. This means that time series with lower phase difference have
    a smaller weight imposed (i.e less penalty imposed) and time series with larger
    phase difference have a larger weight imposed (i.e. larger penalty imposed).

    WDDTW was first proposed in [3]_ as an extension of DDTW. By adding a weight
    to the derivative it means the alignment isn't only considering the shape of the
    time series, but also the phase.

    Parameters
    ----------
    weighted : bool, optional, default=False
        whether a weighted version of the distance is computed
        False = unmodified distance, i.e., dtw distance or derivative dtw distance
        True = weighted distance, i.e., weighted dtw or derivative weighted dtw
    derivative : bool, optional, default=False
        whether the distance or the derivative distance is computed
        False = unmodified distance, i.e., dtw distance or weighted dtw distance
        True = derivative distance, i.e., derivative dtw distance or derivative wdtw
    window: int, defaults = None
        Integer that is the radius of the sakoe chiba window (if using Sakoe-Chiba
        lower bounding).
    itakura_max_slope: float, defaults = None
        Gradient of the slope for itakura parallelogram (if using Itakura
        Parallelogram lower bounding).
    bounding_matrix: np.ndarray (2d of size mxn where m is len(x) and n is len(y)),
                                    defaults = None)
        Custom bounding matrix to use. If defined then other lower_bounding params
        are ignored. The matrix should be structure so that indexes considered in
        bound should be the value 0. and indexes outside the bounding matrix should
        be infinity.
    g: float, optional, default = 0. Used only if weighted=True.
        Constant that controls the curvature (slope) of the function; that is, g
        controls the level of penalisation for the points with larger phase
        difference.

    References
    ----------
    .. [1] H. Sakoe, S. Chiba, "Dynamic programming algorithm optimization for
           spoken word recognition," IEEE Transactions on Acoustics, Speech and
           Signal Processing, vol. 26(1), pp. 43--49, 1978.
    .. [2] Keogh, Eamonn & Pazzani, Michael. (2002). Derivative Dynamic Time Warping.
        First SIAM International Conference on Data Mining.
        1. 10.1137/1.9781611972719.1.
    .. [3] Young-Seon Jeong, Myong K. Jeong, Olufemi A. Omitaomu, Weighted dynamic time
    warping for time series classification, Pattern Recognition, Volume 44, Issue 9,
    2011, Pages 2231-2240, ISSN 0031-3203, https://doi.org/10.1016/j.patcog.2010.09.022.
    """

    def __init__(
        self,
        weighted: bool = False,
        derivative: bool = False,
        window: Union[int, None] = None,
        itakura_max_slope: Union[float, None] = None,
        bounding_matrix: np.ndarray = None,
        g: float = 0.0,
    ):
        super(DtwDist, self).__init__(
            weighted=weighted,
            derivative=derivative,
            window=window,
            itakura_max_slope=itakura_max_slope,
            bounding_matrix=bounding_matrix,
            g=g,
        )
