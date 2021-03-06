# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Created on March 23, 2018

@authors: A. S. Epiney

This file contains the year dependent data for BOP_TOT_revenueEL to be used in the CashFlow test inputs.
"""

import numpy as np

# =====================================================================================================================
def run(self, Inputs):
  """
    Passes back BOP_TOT_revenueEL scaled with input_scaling
    - In, input_scaling, float, used to scale the data
    - Out, BOP_TOT_revenueEL, vector with scaled data
  """

  self.BOP_TOT_revenueEL = np.array(Inputs["input_scaling"] * [
    1.249121E+08,
    1.635489E+08,
    2.852712E+08,
    2.372164E+08,
    3.475519E+07,
    1.192678E+08,
    9.489876E+07,
    9.939405E+07,
    8.203958E+07,
    3.915993E+07,
    2.463487E+08,
    3.286362E+08,
    1.408756E+08,
    2.688309E+08,
    3.274537E+08,
    2.163818E+08,
    1.364193E+08,
    1.448559E+07,
    1.605577E+08,
    1.528224E+08,
    8.456209E+07,
    6.846224E+07,
    2.651716E+08,
    1.509490E+08,
    1.475763E+08,
    2.441756E+08,
    1.347031E+08,
    3.749905E+06,
    3.070918E+08,
    1.673575E+07,
    1.627071E+08,
    2.061307E+08,
    2.692807E+08,
    3.371990E+08,
    1.691349E+08,
    1.416603E+08,
    6.760374E+07,
    7.506250E+07,
    7.651417E+07,
    9.176476E+07,
    4.838345E+07,
    4.244242E+07,
    2.303090E+08,
    2.461599E+08,
    1.873789E+08,
    1.508936E+08,
    1.215092E+08,
    4.185443E+07,
    3.041879E+07,
    2.910637E+08,
    4.434337E+07,
    2.344291E+08,
    2.105549E+08,
    7.681092E+07,
    3.022794E+08,
    1.262402E+08,
    4.201486E+07,
    3.007466E+08,
    2.105868E+08,
    8.829858E+07,
    1.779761E+08,
])

  self.year = np.array([
   0,
   1,
   2,
   3,
   4,
   5,
   6,
   7,
   8,
   9,
   10,
   11,
   12,
   13,
   14,
   15,
   16,
   17,
   18,
   19,
   20,
   21,
   22,
   23,
   24,
   25,
   26,
   27,
   28,
   29,
   30,
   31,
   32,
   33,
   34,
   35,
   36,
   37,
   38,
   39,
   40,
   41,
   42,
   43,
   44,
   45,
   46,
   47,
   48,
   49,
   50,
   51,
   52,
   53,
   54,
   55,
   56,
   57,
   58,
   59,
   60
])


