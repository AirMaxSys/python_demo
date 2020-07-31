#!/usr/bin/python

# python format output
def main():
    a, b = 10, 20
    print('%d * %d = %d' % (a, b, (a * b)))

    s1 = 'Hello'
    name1='john'
    print('{0}, {1}'.format(s1, name1))

    # after python3.6
    print(f'{s1} {name1}, you are nice')

if __name__ == "__main__":
    main()
