#!/usr/bin/env python

# python list pass to function, like c array

def put_fruit_in_bucket(fruits):
    bucket = []
    for fruit in fruits:
        bucket.append(fruit)
    return bucket

def add_fruit(bucket, fruit):
    bucket.append(fruit)

def display_fruit_bucket(bucket):
    for fruit in bucket:
        print(fruit)

def main():
    fruits = ['apple', 'orange', 'peer']
    bucket = put_fruit_in_bucket(fruits)
    print("Before add fruit in bucket:")
    display_fruit_bucket(bucket)
    add_fruit(bucket, 'watermelon')
    print("After add fruit in bucket:")
    display_fruit_bucket(bucket)

if __name__ == "__main__":
    main()

