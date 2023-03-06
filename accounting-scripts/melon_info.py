"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    print()

    for melon_name, melon_info in melons_dict.items():

        print(melon_name.upper())
        print(f'{"-"*(len(melon_name))}')
        for attribute, value in melon_info.items():
            print(f'{attribute}: {value}')

        print()


print_melon(melons_dict)
