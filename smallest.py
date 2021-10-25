#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program determines the smallest number

import random


def smallest(num_list):
    # This function determines the smallest number out of the list.
    smallest_num = num_list[0]

    for num in num_list:
        if smallest_num > num:
            smallest_num = num

    return smallest_num


def main():
    # This function is the main function
    number_list = []

    # process & output
    print("Here is a list of random numbers:\n")

    for counter in range(10):
        random_num = random.randint(1, 100)
        number_list.append(random_num)
        print("The random number {0} is: {1}".format(counter + 1, random_num))

    print("\nThe smallest number is {0}".format(smallest(number_list)))

    print("\nDone.")


if __name__ == "__main__":
    main()
