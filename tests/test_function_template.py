# (c) 2020 Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkModuleTestCase
from .hwtest import autograde as grade

from typing import Callable

function: Callable  # XXX


class FunctionTests(HomeworkModuleTestCase):  # XXX
  # pylint: disable=not-callable
  __scriptname__ = "function_template.py"  # XXX
  __modulename__ = "function_template"  # XXX
  __attrnames__ = ["function"]  # XXX

  @grade.score(10)  # XXX
  def test_function(self):
    self.assertIsNotNone(function())  # XXX
