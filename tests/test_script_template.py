# (c) 2017-2022 Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from hwk.test.unittest import HomeworkTestCase
from hwk.test import autograde as grade


class ScriptTests(HomeworkTestCase):
  @grade.score(10)  # XXX
  def test_script(self):
    result = self.runScript("script_template.py")  # XXX
    self.assertEqual('Hello, world!\n', result.stdout)
