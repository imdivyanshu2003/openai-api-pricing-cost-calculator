#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2023, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Provide historical ticker data for selected stocks.

Sourced from public news sources.

This module contains five dicts: ``AAPL``, ``FB``, ``GOOG``, ``IBM``, and ``MSFT``.

Each dictionary has the structure:

.. code-block:: python

    AAPL['date']       # list of date string
    AAPL['open']       # list of float
    AAPL['high']       # list of float
    AAPL['low']        # list of float
    AAPL['close']      # list of float
    AAPL['volume']     # list of int
    AAPL['adj_close']  # list of float

.. bokeh-sampledata-xref:: stocks
'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
import csv
from typing import TypedDict

# Bokeh imports
from ..util.sampledata import external_path, open_csv

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'AAPL',
    'FB',
    'GOOG',
    'IBM',
    'MSFT',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

class StockData(TypedDict):
    date: list[str]
    open: list[float]
    high: list[float]
    low: list[float]
    close: list[float]
    volume: list[int]
    adj_close: list[float]

def _read_data(name: str) -> StockData:
    '''

    '''
    filename = external_path(name + '.csv')
    data = StockData(
        date = [],
        open = [],
        high = [],
        low = [],
        close = [],
        volume = [],
        adj_close = [],
    )
    with open_csv(filename) as f:
        next(f)
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            date, open_price, high, low, close, volume, adj_close = row
            data['date'].append(date)
            data['open'].append(float(open_price))
            data['high'].append(float(high))
            data['low'].append(float(low))
            data['close'].append(float(close))
            data['volume'].append(int(volume))
            data['adj_close'].append(float(adj_close))
    return data

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

AAPL = _read_data('AAPL')
FB   = _read_data('FB')
GOOG = _read_data('GOOG')
IBM  = _read_data('IBM')
MSFT = _read_data('MSFT')
