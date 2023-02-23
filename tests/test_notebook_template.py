# (c) 2019-2023 Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.notebook import HomeworkNotebookTestCase
from .hwtest import autograde as grade


class NotebookTests(HomeworkNotebookTestCase):
  __notebookname__ = 'notebook_template.ipynb'  # XXX
  __attrnames__ = ['x', 'y']  # XXX

  @grade.score(10)  # XXX
  def test(self):
    self.assertEqual(5, self.nb.x)
    self.assertAlmostEqual(2.0, self.nb.y, places=5)
