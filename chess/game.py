# -*- coding: utf-8 -*-
#
# This file is part of the python-chess library.
# Copyright (C) 2012 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from position import Position
from game_header_bag import GameHeaderBag

import game_node

class Game(game_node.GameNode):
    """The root node of a game."""
    def __init__(self, start_comment="", headers=None):
        game_node.GameNode.__init__(self, None, None, (), start_comment)

        if headers is None:
            self.__headers = GameHeaderBag(self)
        else:
            if not headers.game == self:
                raise ValueError("Header bag assigned to a different game.")
            self.__headers = headers

    @property
    def headers(self):
        """A `chess.GameHeaderBag` holding the headers of the game."""
        return self.__headers

    @property
    def position(self):
        """A copy of the initial position of the game."""
        if "FEN" in self.__headers:
            return Position(self.__headers["FEN"])
        else:
            return Position()

    def game_score(self):
        # Iterate thru all game nodes to produce a 'score sheet'
        for v in self.__variations:
            print v.move