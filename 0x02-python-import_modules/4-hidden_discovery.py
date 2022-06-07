#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for i in range(len(names)):
        if names[i][0] and names[i][1] != "_":
            print(names[i])
