from setuptools import setup

config = {
  "name":         "klassic",
  "version":      "0.1",
  "description":  "Complexity class checking for python.",
  "url":          "http://www.github.com/tuckerman/klassic",
  "author":       "Cameron Jay Tuckerman-Lee",
  "author_email": "cameron@ctuck.com",
  "license":      "MIT"
}

config["packages"] = [ "klassic" ]
config["zip_safe"] = False

setup(**config)
