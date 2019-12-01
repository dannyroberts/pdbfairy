# pdbfairy

[![Build Status](https://travis-ci.com/dannyroberts/pdbfairy.svg?branch=master)](https://travis-ci.com/dannyroberts/pdbfairy)

`pdbfairy` is a small command-line tool that does interaction analysis on PDB files.

## Install
The cleanest install option is to use [pipx](https://pipxproject.github.io/pipx/).

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

To update to the latest version later, use

```
pipx upgrade pdbfairy
```

#### Note for csh/tcsh users

To check your shell, use `echo $SHELL` if it's csh or tcsh, you'll need to follow these steps. If you are using bash, you can skip them. If you're using zsh or fish it'll probably work, but it hasn't been tested.

If you are using CSH (or TCSH) as your shell, then you will need to manually add "$HOME/.local/bin" to your "path". Open `~/.cshrc` and add the following line anywhere in the file:

```
echo 'set path = ($path $HOME/.local/bin)' >> ~/.cshrc
```

Then open a new terminal window (or run `source ~/.cshrc` in the current window)

After installing `pdbfairy` with `pipx` above, you may have to open a new terminal window again before being able to run it.

## Run

For a pdb file called `<filename>` and a max distance in Angstroms called `<max_distance>` (which is optional), you can run it like this:

```
pdbfairy find-interactions <filename> [--max-distance=<max_distance>]
```

The output will be something you can paste into a spreadsheet (Google Spreadsheets, etc., Excel).

To see all commands run `pdbfairy --help`.

To see help for a particular command run `pdbfairy <command> --help`.
