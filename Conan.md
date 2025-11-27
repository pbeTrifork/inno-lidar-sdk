# Creating a Conan Package

In order to use the inno-lidar-sdk from any project, a conanfile has been
created to allow packaging of the binary sdk, for inclusion using the
[conan](https://conan.io) package manager

## Getting Conan
Getting conan can be done as described in the 
[documentation](https://docs.conan.io/2/installation.html), this guide assumes
that conan is installed and at least a default profile has been set up.

## Creating the package
For local usage of the package  the easiest approach is just to build locally.

When the package has been built on the current machine, the binary package is
available to all other projects on the same machine, given the options match.

The most straight forward way is to just go to the root directory,
that is the directory this file is in, and run the following command:

```shell
conan create .
```

This will create the package given all prerequisites are available, you may
have to build some of the prerequisites, in that case,
just add `--build=missing` to the command line (this is only necessary once).

## Creating multiple configurations

