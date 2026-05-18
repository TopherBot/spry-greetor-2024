#!/usr/bin/env python3
"""spry-greetor-2024
A tiny CLI that prints a friendly greeting.
Usage:
  python greet.py            # => Hello, World!
  python greet.py <name>    # => Hello, <name>!
"""
import sys

def main() -> None:
    # Determine the name to greet; default is "World"
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    # Simple safety: strip surrounding whitespace
    name = name.strip()
    # Print the greeting
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
