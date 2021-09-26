string = "b2b2j9g7i6j3h4i5d8d11c11b13c12c13d12d9f8g9e10f7b7e8b10b11c10d13f11f12h10g11g10j11h11c6e6d7g5h5m2l4i3j4j2k4e7h6c9j5f6k5e12i9i10j7j8k7i8k8h12j10k9i12h13f10e11d10b12a13f9k1j1"
new = "b2b2j9g7i6j3h4i5d8d11c11b13c12c13d12d9f8g9e10f7b7e8b10b11c10d13f11f12h10g11g10j11h11c6e6d7g5h5m2l4i3j4j2k4e7h6c9j5f6k5e12i9i10j7j8k7i8k1i4j1g6k2f9i2f10j6h3h2g3g2f4i7f3f2e4h8e3e2e5d3d6d4c7d2c5c2b6d5a3a2l6k8l8k9l9i11k10h12j12k11l10l11i12m11k12"


def parse_string(string):
	r = ''
	f = False
	for i in range(len(string)):
		if string[i].isdigit():
			if i != len(string) - 1:
				if not string[i + 1].isdigit():
					f = True
		r += string[i]
		if f:
			r += " "
		f = False

	return r





class Stone:
	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.previous = None

	def __str__(self):
		r = ''
		r += self.color + " : "
		r += "(" + str(self.position[0]) + ", " + str(self.position[1]) + ")"
		return r



class Board:
	def __init__(self):
		self._board = []

	def create_board_from_string(self, string):
		def get_position(move):
			symb = [
				"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
			]
			return (symb.index(move[0]) + 1, int(move[1:]))


		string = parse_string(string)
		moves = string.split()
		for move in moves:
			position = get_position(move)
			color = "b" if ((len(self._board) + 1) & 1) == 0 else "w"
			for i in range(len(self._board)):
				if self._board[i].position == position:
					if len(self._board) == 1:
						del self._board[i]
						color = "w"
					else:
						raise Exception
			self._board.append(Stone(color, position))

	def get_neighbors(self, stone):
		color = stone.color
		possible_neighbors =  [
			(stone.position[0] - 1, stone.position[1]),
			(stone.position[0], stone.position[1] - 1),
			(stone.position[0] + 1, stone.position[1] -1),
			(stone.position[0] + 1, stone.position[1]),
			(stone.position[0], stone.position[1] + 1),
			(stone.position[0] - 1, stone.position[1] + 1),
		]
		neighbors = []
		for neighbor in possible_neighbors:
			for elem in self._board:
				if elem.position == neighbor and color == elem.color:
					neighbors.append(elem)
		return neighbors

	def is_game_over(self):
		for i in [0, 1]:
			for j in range(len(self._board)):
				if self._board[j].position[i] == 1:
					explored = []
					explored.append(self._board[j])
					reachable = self.get_neighbors(self._board[j])
					while reachable != []:
						node = reachable.pop()
						if node.position[0] == 13 and node.color == "w":
							print("w")
							return True
						if node.position[1] == 13 and node.color == "b":
							print("b")
							return True
						new_adjacents = self.get_neighbors(node)
						for elem in new_adjacents:
							if elem.position[0] == 13 and elem.color == "w":
								print("w")
								return True
							if elem.position[1] == 13 and elem.color == "b":
								print("b")
								return True
							if not elem in explored:
								reachable.append(elem)
						explored.append(node)
		return False








	def get_board(self):
		for elem in self._board:
			print(elem)


b = Board()
b.create_board_from_string(new)
print(b.is_game_over())

