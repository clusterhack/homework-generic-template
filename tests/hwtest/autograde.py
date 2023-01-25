# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

"""
Module that loads unittest decorators suitable for the environment
under which the tests are being executed. Specifically:
- If gradescope_utils module is installed, those are used
- If GITHUB_ACTIONS env var is true, those from .github_autograde are used
- If neither of above, then all decorators are set to no-op (i.e., identity function)
This allows students to run tests locally, without having to install any other packages.
"""
# TODO Move github_autograde to a separate project

import os
from typing import Literal, Optional

runner: Optional[Literal['gradescope', 'github', 'local']] = None

# Case 1: Running under GradeScope
try:
  from gradescope_utils.autograder_utils.decorators import weight, number, visibility, tags
  runner = 'gradescope'
except ImportError:
  pass

# Case 2: Running under GitHub Actions
if runner is None and os.getenv('GITHUB_ACTIONS') == 'true':
  from .github_autograde import weight, number, visibility, tags
  runner = 'github'

# Case 3: "local" (i.e., neither GradeScope nor GitHub VM)
if runner is None:
  def __noop_decorator(*args, **kwargs):
    def decorator(func):
      return func
    return decorator

  weight = number = visibility = tags = __noop_decorator
  runner = 'local'


# Exported names
__all__ = ['weight', 'number', 'visibility', 'tags']
