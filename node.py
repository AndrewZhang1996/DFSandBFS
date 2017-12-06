class node():

	def __init__(self, name, hasPrevious, hasNext):
		self.name = name
		self.previous = None
		self.next = None
		self.hasPrevious = hasPrevious
		self.hasNext = hasNext

	def set_previous(self, _previous):
		if self.hasPrevious==1:
			self.previous = _previous

	def set_next(self, _next):
		if self.hasNext==1:
			self.next = _next
