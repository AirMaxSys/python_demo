#!/usr/bin/env python

def main():
    manufactures = ['ST', 'samsung', 'atmel', 'microchip']
    m1 = manufactures
    print("m1 is a reference of manufactures:", m1)

    # use operator to copy list
    m1.append('TI')
    print("after m1 add 'TI', m1 is:", m1)
    print("after change m1, manufactures is:", manufactures)

    print()

    # use list method copy to copy list
    m2 = manufactures.copy()
    print("m2 is a copy of manufactures:", m2)
    m2.remove('samsung')
    print("after m2 remove 'samsung', m2 is:", m2)
    print("after change m2, manufactures is:", manufactures)

    print()

    # use slicing to copy list
    m3 = manufactures[:]
    print("m3 is a copy of manufactures:", m3)
    m3.remove('microchip')
    print("after m3 remove 'microchip', m3 is:", m3)
    print("after change m3, manufactures is:", manufactures)

if __name__ == "__main__":
    main()

