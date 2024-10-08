# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from hwk.test.unittest import HomeworkModuleTestCase
from hwk.test import autograde as grade

from typing import Callable

function: Callable  # XXX

@grade.max_score(10)
class FunctionExtraTests(HomeworkModuleTestCase):  # XXX
  __scriptname__ = "function_template.py"  # XXX
  __modulename__ = "function_template"  # XXX
  __attrnames__ = [ "function" ] # XXX

  @grade.score(-10)
  def test_function(self):
    self.assertIsNotNone(function())  # XXX
