# pdbfairy

## Install

To install, enter the directory you want to house it, and run
```
git clone https://github.com/dannyroberts/pdbfairy.git
cd pdbfairy
python3 -m venv pdbfairy
source ./pdbfairy/bin/activate
pip install -r requirements.txt
```

## Run

## Set up for each new terminal window
Every time you open a new terminal and want to run it, first run

```
cd pdbfairy
source ./pdbfairy/bin/activate
```
once per terminal window.

## Running the code

For a pdb file called `<filename>` and a max distance in Angstroms called `<max_distance>` (which is optional), you can run it like this:

```
python main.py <filename> [<max_distance>]
```

The output will be something you can paste into a spreadsheet (Google Spreadsheets, etc., Excel)
