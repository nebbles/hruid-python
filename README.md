<p  align="center">
  <strong>HRUID</strong>
  <br>
  <code>Human Readable Unique Identifier for Python</code>
  <br><br>
  <!-- <a href="https://badge.fury.io/py/conventional-commit"><img src="https://badge.fury.io/py/conventional-commit.svg" alt="PyPI version" height="18"></a>
  <a href="https://travis-ci.org/nebbles/gitcommit/branches"><img src="https://travis-ci.org/nebbles/gitcommit.svg?branch=master" alt="Travis CI build" height="18"></a> -->
</p>

## Usage

Install
```
pip install hruid
```

Use in Python code
```python
import hruid

generator = hruid.Generator()
phrase = generator.random()
print(phrase)
```

Use on the command line
```
$ hruid generate

11-suspicious-owls-consume-eagerly
```

## Overview

This Python package implements human readable ID generation based on the [Asanablog post by Greg
Slovacek](https://blog.asana.com/2011/09/6-sad-squid-snuggle-softly/).

In it, he describes how a unique phrase can be generated in lieu of a confusing and complex
alphanumeric ID.

> Imagine representing 32 bits of information (numbers up to 4 billion) as a sentence instead of a jumble of digits. Each sentence can have the same predictable structure, and the number will be used to choose words from a dictionary to fill in that structure—like Mad Libs.
> 
> One possible sentence structure can be: count + adjective + plural noun + verb + adverb, e.g. “6 sad squid snuggle softly.” We can divide the bit-space of the number like so:
> 
> - 5 bits for the count (2-33, so it is always plural)  
> - 7 bits for the adjective (one of 128 possibilities)  
> - 7 bits for the plural noun (one of 128 possibilities, which we made all animals just for fun)  
> - 7 bits for the verb (one of 128 possibilities)  
> - 6 bits for the adverb (one of 64 possibilities)  
>
> Now, given a dictionary containing words categorized in this way, we can generate 4 billion unique (and sometimes very memorable) sentences. In Asana, the ID used to generate the error phrase is random, so the same sentence is unlikely to occur twice.

## Develop

Install dependencies
```
poetry install
```

Run `example.py` which does some basic things with the package
```
poetry run python example.py
```

Run the package in CLI mode
```
poetry run python -m hruid
```

To run tests
```
poetry run tests
```

## License

[GNU GPLv3](./LICENSE)
