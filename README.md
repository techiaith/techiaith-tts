# techiaith-tts
*****************


Contents
========


Getting started:

* Installation

  * Installing with "pip"

  * Installing from source

* Overview

* Changelog

  * Unreleased


Installation
============

### Installing with "pip"
```shell
pip install techiaith-tts
```

### Installing from source
```shell
git clone https://github.com/techiaith/techiaith-tts.git
cd techiaith-tts
conda create -n techiaith-tts python=[3.8 <= x.x => 3.12]
conda activate techiaith-tts
pip install -r requirements.txt
pip install -e .
```

Overview
========
The normaliser function `parse_text()` takes a string as an input and expands symbols to their string representation.

The code snippet below, from src/demo.py, runs an infinite loop taking user input and returning the full text representation of the input. 
### Usage
```python
from techiaith.tts.testun.normaliser import parse_text

while True:
  text = input("\nprompt: ")
  clean_text = parse_text(text)
  print("\nresult:", clean_text)
  if clean_text == "exit":
    break
```
#### Output
```
$ python normaliser_test.py

prompt: Y dyddiad heddiw ydi'r 1af o Ionawr 2023
 
result: Y dyddiad heddiw ydi'r cyntaf o Ionawr dwy fil dau ddeg tri
```

Team
====

**techiaith-tts** is developed and maintained by the *Uned Technolegau
Iaith (UTI) <https://techiaith.cymru/>* team, backed by *Prifysgol
Bangor (UTI) <https://bangor.ac.uk/>*. A self-funded research unit
that develops technologies for the Welsh language. To learn more about
who specifically contributed to this codebase, see our contributors
page.


License
=======

**techiaith-tts** is licensed under MIT License. A full copy of the
license can be found on GitHub.


Indices and tables
==================

* Index

* Module Index
