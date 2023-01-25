# (c) 2019-2022 Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkTestCase
from .hwtest import autograde as grade


class NotebookTests(HomeworkTestCase):
  @grade.weight(0)  # XXX
  def test(self):
    with self.runNotebook('notebook_template.ipynb', ('x', 'y')) as nb:
      self.assertEqual(5, nb.x)
      self.assertAlmostEqual(2.0, nb.y, places=5)
