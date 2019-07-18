<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/pipreqs_update.svg?longCache=True)](https://pypi.org/project/pipreqs_update/)
[![](https://img.shields.io/pypi/v/pipreqs_update.svg?maxAge=3600)](https://pypi.org/project/pipreqs_update/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/pipreqs-update.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/pipreqs-update.py/)

#### Installation
```bash
$ [sudo] pip install pipreqs_update
```

#### Functions
function|`__doc__`
-|-
`pipreqs_update.update(path)` |update pip requirements file with latest versions

#### Executable modules
usage|`__doc__`
-|-
`python -m pipreqs_update path` |update pip requirements file with latest versions

#### Scripts usage
command|`usage`
-|-
`pipreqs-update` |`usage: pipreqs-update path`

#### Examples
```bash
$ pipreqs-update requirements.txt
```

```bash
$ python -m pipreqs_update requirements.txt
```

```python
>>> import pipreqs_update
>>> pipreqs_update.update('requirements.txt')
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>