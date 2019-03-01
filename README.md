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
>>> from rextester_py.rextester import rextester
>>> rextester.rexec("py3", "print('Hello World')", None)
<rextester_py.rextester.rextester.RextesterResult object at 0x7fd3bebc9f28>
>>> rextester.rexec("py3", "print('Hello World')", None).results
Hello World
```

### Async usage:

```python

>>> from rextester_py.rextester import rextester_aio
>>> import asyncio
>>> async def test():
...     rex = await rextester_aio.rexec("py3", "print('Hello World')", None)
...     print(rex.results)
...
>>> asyncio.get_event_loop().run_until_complete(test())
Hello World

```

## Languages:

```
 ada,  asm,  bash,  brainfuck,  c,  c#,  c++,  c_clang,  c_gcc,  clang,  clang++,  clangplusplus,  clisp,  common_lisp,  cplusplus,  cplusplus_clang,  cplusplus_gcc,  cpp,  cpp_clang,  cpp_gcc,  csharp,  d,  elixir,  erlang,  f#,  fortran,  fpc,  fsharp,  g++,  gcc,  go,  golang,  haskell,  java,  javascript,  js,  kotlin,  lisp,  lua,  msvc,  mysql,  nasm,  node,  objc,  objective_c,  ocaml,  oracle,  pas,  pascal,  perl,  php,  postgresql,  prolog,  py2,  py3,  python,  python2,  python3,  r,  ruby,  scala,  scheme,  sql_server,  swift,  tcl,  v8,  vb,  vb.net,  vc++,  visual_basic_dotnet,  visual_c,  visual_cplusplus,  visual_cpp
 ```
