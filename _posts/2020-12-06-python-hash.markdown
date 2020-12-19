---
layout: post
title: "Falling tree and garbage collection"
date: 2020-12-07
categories: python
tags: [programming, python]
---
## Falling tree and garbage collection

I believes most people know the famous koan:
> If a tree falls in a forest...

I came up with a similar question for python: If a value gets destroyed and no name is referring to it, does it make a sound?

Values do not make a sound anyways, but they are destoyed if no longer referenced to, which is done implicitly by the memory management in Python. I guess the real question is, how do we know the value is destroyed if it is no longer referenced?

There is a way to check reference count:

```
import sys
a = 8
sys.getrefcount(a)
```
But you'll never see the moment when "the tree falls" -- I mean you got never got a chance to ref-count an object with no reference. 
