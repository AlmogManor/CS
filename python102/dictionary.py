"""
Author: Almog Manor
Example of usage of builtin dict
"""


def main():
    """entry point to the program
    """
    # create with values
    people_to_age = {"Bob":20, "Daniel":17, "Mary":18}
    
    # access value that belongs to ket "Bob"
    print(people_to_age["Bob"])

    # add the key "Mark" with the value 42
    people_to_age["Mark"] = 42

    # amount of entries (entry = key + value) in the dictionary
    print(len(people_to_age))

    # iterate over both the keys and the values (matching pairs)
    for key, value in people_to_age.items():
        print(f"key: {key}, value: {value}")

    # iterate over keys only
    for key in people_to_age:
        print(f"key: {key}")

    # iterate over values only
    for value in people_to_age.values():
        print(f"value: {value}")

    # this will cause an error, the key doesn't exist:
    print(people_to_age["Alfred"])


if __name__ == "__main__":
    main()
