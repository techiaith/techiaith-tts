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
pip install -e .
```

Overview
========
### Usage
#### normaliser_test.py
```python
from techiaith.tts.testun.normaliser import parse_text

while True:
  text = input("prompt: ") 
  clean_text = parse_text(text)
  print(clean_text)
```
#### output
```shell
python normaliser_test.py
prompt: "Y dyddiad heddiw ydi'r 1af Ionawr 2023" 
Y testun cyntaf i lefaru
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
