class Person:
	def __init__(self, name):
		self.name = name

	def greet(self):
		return "Hello, " + self.name


def main():
	p = Person("Alice")
	print(p.greet())


if __name__ == "__main__":
	main()
