---
layout: post
title: "C++: some random pieces of knowledge"
date: 2021-09-11
categories: journal
tags: [journal]
---


This article is one of an series about some random facts about C++.


# Virtual function

Why do we need virtual function?? I have no clue just by looking at the definition.

# What the m_ ?
`m_` is a prefix for class **m**embers. Not syntactically mandatory but widely accepted convention.
```cpp
class A
{
    private m_value;
}
```

# Disable a function by =delete
```cpp
Class ABC{
 Int d;
 Public:
  ABC& operator= (const ABC& obj) =delete;
};
```
# [delete[]](https://www.cplusplus.com/reference/new/operator%20delete[]/) vs delete
They are different operators. `delete[]` is for deleting arrays, `delete` for other cases. 
[Why do we even need `delete[]`](https://stackoverflow.com/a/252830/10437558)
```cpp
int* set = new int[100];
// do stuff
delete [] set;
```

# Dot dot dot...?
`...` means [unknown number of variables](https://en.wikipedia.org/wiki/Variadic_function#In_C++).
It is seen in most popular languages, however not so strightforward in cpp as in pythong/R.



