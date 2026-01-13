def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

def main():
    """Main function"""
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")

if __name__ == "__main__":
    main()