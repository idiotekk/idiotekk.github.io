---
layout: post
title: "C++: some random pieces of knowledge"
date: 2021-09-11
categories: journal
tags: [journal]
---


This article is one of a series about some random facts about C++.


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

# Initialization
## How shall I initialize a variable?
Four kinds of initialization:
```cpp
int x; # no initilizer
int x = 5; # copy initialization
int x(5); # direct initialization
int x{ 5 }; # init in braces; if putting nonthing in {}, the variable is set to 0.
```
The last one is favored because it does not silently convert the input if the input has the wrong type (like `int(4.5)` will convert `4.5` to `4`), and will throw an error.

## Expression, statement, expression statement
Basically expresion = result; statement = action. Expression statement is both (it is a statement by definition), but the "result" is discarded.
```
x = 2
```
Suffixing it with an `;` makes it a expression statement.

## You can't define a fuction inside another function
Unlike many other languages.

## main() should return 0 to indicate it runs successfully
Where `0` is [exit status](https://en.wikipedia.org/wiki/Exit_status).
Other two standard status: `EXIT_SUCCESS` and `EXIT_FAILURE`.


