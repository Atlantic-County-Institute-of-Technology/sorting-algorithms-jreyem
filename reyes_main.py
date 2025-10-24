from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
import random

outer_pass = 0
inner_pass = 0


def main():
    global values

    while True:
        print("[-] 0. Exit\n"
              "[-] 1. Generate Random List\n"
              "[-] 2. Bubble Sort\n"
              "[-] 3. Selection Sort\n"
              "[-] 4. Insertion Sort")

        selection = int(input("[-] Please select an option: "))

        if selection == 0:
            print("Boom, program closing.")
        elif selection == 1:
            min_value = int(input(f"Insert Minimum Value: "))
            max_value = int(input(f"Insert Maximum Value: "))
            size = int(input(f"Insert Value Size: "))
            values = [random.randint(min_value, max_value) for _ in range(size)]
            print(f"Generated List: {values}")

        elif selection == 2:
            bubble_sort(values)
            print(values)
            print(f"Outer Pass: {outer_pass}\n"
                  f"Inner Pass: {inner_pass}")

        elif selection == 3:
            selection_sort(values)
            print(values)
            print(f"Outer Pass: {outer_pass}\n"
                  f"Inner Pass: {inner_pass}")

        elif selection == 4:
            insertion_sort(values)
            print(values)
            print(f"Outer Pass: {outer_pass}\n"
                  f"Inner Pass: {inner_pass}")

        else:
            print("Bro that isn't an option. Try again lil bro. 🕊️")


if __name__ == "__main__":
    main()
