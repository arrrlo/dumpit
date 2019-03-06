# dumpit
## Print python objects like a boss

[![PyPI version](https://badge.fury.io/py/dumpit.svg)](https://badge.fury.io/py/dumpit)
[![Build Status](https://travis-ci.com/arrrlo/dumpit.svg?branch=master)](https://travis-ci.com/arrrlo/dumpit)
![GitHub](https://img.shields.io/github/license/arrrlo/dumpit.svg?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/arrrlo/dumpit.svg?color=blue)

### Installation
Works with python 3.x

```
pip install dumpit
```

### Usage

```python
from dumpit import pdumpit, fdumpit

my_object = ...

# Print object to standard output
pdumpit(my_object)

#Print object to standard output in vertical view
pdumpit(my_object, view_='vertical') # vertical | table

# Export object to string as text
my_var = fdumpit(my_object)

# Disable colors in terminal output
pdumpit(my_object, colors=False) # False | terminal

# Enable colors in string output
my_var = fdumpit(my_object, colors='terminal')
```

# CHANGELOG

## 0.3.0

#### Added:
- Analyse is now view.
- Table view support: Print object contents in table view in terminal.
- Warnings: Prints warnings in terminal if unknown coloring or view is used.

## 0.2.0

#### Added:
- Coloring support: Terminal colors for object attributes.  