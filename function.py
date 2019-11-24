#  Copyright 2019, Pedro Gomes.
#
#  This file is part of FADO.
#
#  FADO is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  FADO is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with FADO.  If not, see <https://www.gnu.org/licenses/>.

import variable as var


# Class to define functions
class Function:
    def __init__(self,outVar,valEval,gradEval):
        self._outVar = outVar
        self._valEval = valEval
        self._gradEval = gradEval

    def evalValue(self):
        pass

    def evalGradient(self):
        pass

    def value(self):
        return self._outVar.getVal()

    def gradient(self):
        return self._outVar.getGrad()
#end
