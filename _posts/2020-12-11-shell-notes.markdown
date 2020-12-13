---
layout: post
title: "Shell scripts: the very basics"
date: 2020-12-11
categories: programming, shell
---

Why do I learn Shell scripts?
Answer: out of curiosity, and, it is super useful, as long as I work in a linux environment.

This post serves as a learning note.

# important
- shell script is sensitive to space, unlike most languages (--python, java, cpp i mean, that's all i know; and R, too). This means you'd better do `x=1` instead of `x = 1`.

# comparison

- `-lt,-le,-gt,-ge` do (almost) what they literally means, if you are a Latex user and familar with `\eq`, etc.
- `-z` determines a variable is null or not

# loop
- if else ` if [ $x -ge 0 ]; then ... ; else ... ; fi`
- while ` while [ ...]; do ...; done `; to increment a variable, say `x`: `x = $((x + 1))`:w

# io
- `read x` ask user for an input, store input as x
- 

