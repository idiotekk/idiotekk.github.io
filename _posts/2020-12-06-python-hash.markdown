---
layout: post
title: "Immutable vs hashable objects in python"
date: 2020-12-07
categories: python
---
If you click on this article because of the title, you'll be disappointed. This article is not (only) about immutable and hashable objects in python. 
The reason is that I was struck by something else at the moment I started writing.

## Falling tree and garbage collection

I believes most people know the famous question:
> If a tree falls in a forest...

I came up with a similar question for python:
If a value gets destroyed and no name is referring to it, does it make a sound?

Values do not make a sound anyways. I guess the real question is, how do we know the value is destroyed if it is no longer referenced?

Well, I don't know. But pro pythoners say so. I better believe it.

There is, however, a way to check reference count:

```
import sys
a = 8
sys.getrefcount(a)
```
But you'll never see the moment when "the tree falls" -- I mean you got never got a chance to ref-count an object with no reference. 
