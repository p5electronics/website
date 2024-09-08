---
title: "Lissajou Curves"
layout: "post.njk"
date: "2024-09-02"
tags: ["post", "math"]
---

Ever since I started my undergraduate degree, I've always looked forward to the day where I'd start drawing patterns on an analog oscilliscope for funsies. Today seems like just the right day to start experimenting and there's no better place to start than the fundamentals. I introduce to you, the *Lissajou curve*.

<div class="picture-container">
  <img src="lissajou.gif" alt="Lissajou Curve Light" class="theme-image light-mode">
  <img src="lissajou-dark.gif" alt="Lissajou Curve Dark" class="theme-image dark-mode">
</div>

## What are Lissajou Curves?
Lissajou curves, also known as Bowditch curves, are a special family of curves described by the linear set of parametric equations:

 <div id="lissajou-equations">
    \[
    \begin{cases}
    x(t) = A \sin(at + \delta) \\
    y(t) = B \sin(bt)
    \end{cases}
    \]
</div>

First investigated by Nathaniel Bowditch and later refined by its namesake Jules Antoine Lissajous (get mogged), these curves model the behavior that results from when two sinusoids lying on both the x-axis and y-axis directions of the cartesian plane are superposed.

Over time, this figure has been proven to be a useful tool with a variety of applications such as signal processing, orbital mechanics, music theory, and art. 

Personally, I only had discovered the name of this pattern through one of my previous internships over at MIT Lincoln Laboratory because they had it as their logo (they are rather enthusiastic about explaining its history and you can read more about it [here](https://www.ll.mit.edu/about/history/lincoln-laboratory-logo)).

[...] and you can find the Python script that I used to generate all the animations within this article on my [GitHub page]().

Stay tuned for more!