---
library: cli
language: python
---

# Command Line Interfaces

CLIs are fun to write, but there's a lot of boilerplate. The snippets outlined
here scaffold a CLI and take away some of the thinking necessary for working
with them.

## Argument Parser

Create an argument parser that takes in various command line arguments.
Pre-populated with a verbosity argument.

<!-- cli-parse -->

```python
from argparse import ArgumentParser
import logging

logger = logging.getLogger(__name__)

def _parse_args():
    parser = ArgumentParser()
    $0
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Starting script in verbose mode...")
    return args
```

## Add Argument to Parser

Add an argument to the argument parser.

<!-- cli-arg -->

```python
${1:parser}.add_argument("-${2:f}", "--${3:flag}", type=${4:str}, default=${5:None})
```

## Add Multi-parameter Argument to Parser

Add an argument with multiple parameters to the argument parser.

<!-- cli-arg-multi -->

```python
${1:parser}.add_argument("-${2:f}", "--${3:flag}", type=${4:str}, action="append", default=${5:[None]})
```
