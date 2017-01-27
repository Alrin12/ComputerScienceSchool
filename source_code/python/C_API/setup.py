from distutils.core import setup, Extension

setup(name = "evaluate", version = "1.0",
      description = "calculate average, variance",
      author = "taehwan yang",
      author_email = "ythwork@gmail.com",
      url = "http://github/ythwork",
      ext_modules = [Extension("evaluate", ["evaluate.c"])]
      )
