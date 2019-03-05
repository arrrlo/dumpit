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

### Print object to standard output

```python
from dumpit import pdumpit

pdumpit(__some_object__)
```

### Export object to string as text

```python
from dumpit import fdumpit

my_var = fdumpit(__some_object__)
```

