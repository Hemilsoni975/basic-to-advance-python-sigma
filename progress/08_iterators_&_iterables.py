# iterable is an object that one can iterate over.
# iterator is generated from the iterable when passes with iter() method.
# syntax:
# iter() or __iter__()
# iterator is an object that can iterate over an iterable object using next() method.
# syntax:
# next() or __next__()

# iterator object using string

s = "HEMIL"
s = iter(s)
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# iterator object using list

mylist = ["hemil","sanju","kesar","aman"]
s = iter(mylist)
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# iterable = iter()
# iterator = next()

b = iter(range(100))
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
