"""Main module for test project."""

def hello(name: str = "World") -> str:
    """Return a friendly greeting.

    Args:
        name: Name to greet.

    Returns:
        Greeting string.
    """
    return f"Hello, {name}!"
