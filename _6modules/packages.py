# dotted module names

# a.b --> submodule B in a package named A

# use of modules saves the authors of different modules from having the other's global variable
# names

# use of dotted modules saves the authors of multi-module packages like NumPy or the
# Python Imaging Library from each other's module names

# collection of modules = a package

# example for uniform handling of sound files and sound data


##sound/                          Top-level package
##      __init__.py               Initialize the sound package
##      formats/                  Subpackage for file format conversions
##              __init__.py   --> required to
##              wavread.py
##              wavwrite.py
##              aiffread.py
##              aiffwrite.py
##              auread.py
##              auwrite.py
##              ...
##      effects/                  Subpackage for sound effects
##              __init__.py
##              echo.py
##              surround.py
##              reverse.py
##              ...
##      filters/                  Subpackage for filters
##              __init__.py
##              equalizer.py
##              vocoder.py
##              karaoke.py
##              ...

import sound.effects.echo
sound.effects.echo(input, output, delay=0.7, atten=4)
# or
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)




