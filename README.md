# Rextester Py

Simple Python interface for rextester.com, using aiohttp/requests

## Instalation
`pip3 install rextester_py`

## Usage:


When executing a code using the library it will return RextesterResult object that holds the following attributes:

- `results` - The result of your code
- `warnings` - Any warnings trown by rextester's compiler
- `errors` - Any errors trown by rextester's compiler
-  `stats` - The compilation stats: absolute running time, cpu time, memory peak and absolute service time

### Non async usage:

```python
>>> from rextester_py import rexec
>>> rexec("python 3", "print('Hello World')", None)
<rextester_py.rextester.rextester.RextesterResult object at 0x7fd3bebc9f28>
>>> rexec("python 3", "print('Hello World')", None).results
Hello World
```

### Async usage:

```python

>>> from rextester_py import rexec_aio
>>> import asyncio
>>> async def test():
...     rex = await rexec_aio("python 3", "print('Hello World')", None)
...     print(rex.results)
...
>>> asyncio.get_event_loop().run_until_complete(test())
Hello World

```

## Languages:


```
c#, vb.net, f#, java, python, c (gcc), c++ (gcc), php, pascal, objective-c, haskell, ruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, scheme, node.js, python 3, octave, c (clang), c++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, bash, ada, erlang, elixir, ocaml, kotlin, brainfuck, fortran

```