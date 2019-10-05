import collections
import math
import sys

from Bio import PDB
from numpy import linalg


MAX_DISTANCE = 4


def main(structure):
    pairs = find_pairs(structure)
    for atom_1, atom_2 in pairs:
        print(format_atom(atom_1), format_atom(atom_2), dist(atom_1, atom_2))


def find_pairs(structure, max_distance=MAX_DISTANCE):
    atoms = list(structure.get_atoms())
    atoms_by_i = collections.defaultdict(list)

    def get_i(atom):
        return math.floor(atom.coord[0] / MAX_DISTANCE)

    for atom in atoms:
        atoms_by_i[get_i(atom)].append(atom)

    for atom in atoms:
        i = get_i(atom)
        yield from (
            (atom, a)
            for offset in [-1, 0, 1]
            for a in atoms_by_i[i + offset]
            if a.parent.parent != atom.parent.parent
            and dist(a, atom) <= max_distance
        )
        atoms_by_i[i].remove(atom)


def dist(atom_1, atom_2):
    return linalg.norm(atom_1.coord - atom_2.coord)


def format_atom(atom):
    return "{chain}{res}{atom}".format(
        chain=atom.parent.parent,
        res=atom.parent,
        atom=atom,
    )


if __name__ == '__main__':
    pdb_file = sys.argv[1]
    parser = PDB.PDBParser()
    structure = parser.get_structure('DATA', pdb_file)
    main(structure)
