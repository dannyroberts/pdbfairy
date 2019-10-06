# pdbfairy

[![Build Status](https://travis-ci.com/dannyroberts/pdbfairy.svg?branch=master)](https://travis-ci.com/dannyroberts/pdbfairy)

## Install

### Recommended option: install using pipx.

To just access the executable, the cleanest install option is to use [pipx](https://pipxproject.github.io/pipx/).

First, install pipx:
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# see note for csh/tcsh users below
```

Then use it to install pdbfairy:

```
pipx install pdbfairy
```

#### Note for csh/tcsh users

If you are using CSH (or TCSH) as your shell, then you will need to manually add "$HOME/.local/bin" to your "path". Open `~/.cshrc` and add the following line anywhere in the file:

```
echo 'set path = ($path $HOME/.local/bin)' >> ~/.cshrc
```

Then open a new terminal window (or run `source ~/.cshrc` in the current window)

After installing `pdbfairy` with `pipx` above, you may have to open a new terminal window again before being able to run it.

### Option 2: Install in a virtualenv

If your goal is to run the `pdbfairy` executable, you should skip this section.

If you want to install the package in such a way that you can write your own python code using it as a library, you can use this method instead.

First, make sure your virtualenv is python >= 3.4. Then you can install it as you would any other package:

```
pip install pdbfairy
```

## Run

For a pdb file called `<filename>` and a max distance in Angstroms called `<max_distance>` (which is optional), you can run it like this:

```
pdbfairy find-interactions <filename> [--max-distance=<max_distance>]
```

The output will be something you can paste into a spreadsheet (Google Spreadsheets, etc., Excel).

To see all commands run `pdbfairy --help`.

To see help for a particular command run `pdbfairy <command> --help`.