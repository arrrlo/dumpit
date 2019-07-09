# dumpit  

## List all python object attributes with descriptions

[![PyPI version](https://badge.fury.io/py/dumpit.svg)](https://badge.fury.io/py/dumpit)
[![Build Status](https://travis-ci.com/arrrlo/dumpit.svg?branch=master)](https://travis-ci.com/arrrlo/dumpit)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bac341f96271404883c9df270492c962)](https://www.codacy.com/app/arrrlo/dumpit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=arrrlo/dumpit&amp;utm_campaign=Badge_Grade)

![GitHub issues](https://img.shields.io/github/issues/arrrlo/dumpit.svg)
![GitHub closed issues](https://img.shields.io/github/issues-closed/arrrlo/dumpit.svg)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/arrrlo/dumpit.svg)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dumpit.svg)
![GitHub](https://img.shields.io/github/license/arrrlo/dumpit.svg?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/arrrlo/dumpit.svg?color=blue)

![Terminal view](docs/images/terminal.png?3)

### Installation

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

# Don't show dunder methods (magic methods)
pdumpit(my_object, all_=False)
```

# Changelog

## 0.6.0

#### Fixed in 0.6.0
-   all_ parameter default value is now False
-   code formatting 

## 0.5.0

#### Fixed in 0.5.0
-   Python 3 compatibility

## 0.4.2

#### Fixed in 0.4.2
-   Dependency version changed: Click 6.7 -> Click 7.0

## 0.4.1

#### Fixed in 0.4.1
-   Dunder methods description formatting and new lines.

## 0.4.0

#### Added in 0.4.0
-   Descriptions for every objects attribute.
-   Separate dunders from other attributes. 

## 0.3.0

#### Added in 0.3.0
-   Analyse is now view.
-   Table view support: Print object contents in table view in terminal.
-   Warnings: Prints warnings in terminal if unknown coloring or view is used.

## 0.2.0

#### Added 0.2.0
-   Coloring support: Terminal colors for object attributes.  
