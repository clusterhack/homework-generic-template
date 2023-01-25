# (c) 2023- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

__all__ = ['weight', 'number', 'visibility', 'tags']

from typing import Callable, Literal

def weight(points: float):
  def decorator(func: Callable) -> Callable:
    func.__weight__ = points
    return func
  return decorator

def number(sortkey):
  def decorator(func: Callable) -> Callable:
    func.__number__ = str(sortkey)
    return func
  return decorator

def visibility(vis: Literal['hidden', 'visible']):
  def decorator(func: Callable) -> Callable:
    func.__visibility__ = vis
    return func
  return decorator

def tags(*args):
  def decorator(func: Callable) -> Callable:
    func.__tags__ = args
    return func
  return decorator
