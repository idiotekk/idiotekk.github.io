---
layout: post
title: "Python tricks that make life easier"
date: 2021-08-07
categories: journal
tags: [journal]
---

Some python trick that saves time/code.

## Walrus operator (or more formally, the Assignment Expression)
This is new in 3.8.
The operator allows you to define and use a variable in one line.
[PEP 572](https://www.python.org/dev/peps/pep-0572/) has every detail of the operator.

In if, while etc.:
```python
x = some_function()
if x is True:
    raise

## writen with walrus operator:
if (x := some_function()) is True:
    raise
```

List comprehension
```python
x = some_function()
my_list = [x, x + 1, x + 2]

## writen with walrus operator:
my_list = [x := some_function(), x + 1, x + 2]
```

## Reverse a dict using zip
Not a new thing, but could be helpful in cases
```python
reversed_dict = dict(zip(old_dict.values(), old_dict.keys()))
```
Be careful of collision of values, as a dictionary may not be one-to-one.

## Print with saparator
Print is too useful so it's good make the most ouf ot it.
```python
print(*arg, sep=",")
```

## Iterrate through a tree
Yes you can construct an iterator recursive. The key is `yield from`.
```python
def iter_values(root):
    if root is None: return # return will yield nothing
    yield from iter_values(root.left)
    yield root.val
    yield from iter_values(root.right)
```

## To Be Continued
