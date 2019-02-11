#! /usr/bin/env python3

def main():
    list1 = [1, 2, 3, 0, 5, 6]

    print(any(list1))

    print(all(list1))
    
    print(min(list1))
    print(max(list1))

    print(sum(list1))

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysfr = ["Dim", "lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    it = iter(days)
    print(next(it))
    print(next(it))

    for index, day in enumerate(days, start=1):
        print(index, day)

    for i, m in enumerate(zip(days, daysfr), start=1):
        print(i, m[0], "=", m[1])

if __name__ == "__main__":
    main()