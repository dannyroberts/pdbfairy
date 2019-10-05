import collections
import math
import sys

from Bio import PDB
from numpy import linalg
import numpy


MAX_DISTANCE = 4


def main(structure):
    pairs = find_pairs(structure)
    for atom_1, atom_2 in pairs:
        print(format_atom(atom_1), format_atom(atom_2), dist(atom_1, atom_2))


def find_pairs(structure, max_distance=MAX_DISTANCE):
    atoms = list(structure.get_atoms())
    atoms_by_cube = collections.defaultdict(set)
    atoms_by_chain = collections.defaultdict(set)

    def get_cube(atom):
        return numpy.floor(atom.coord / max_distance)

    for atom in atoms:
        atoms_by_cube[tuple(get_cube(atom))].add(atom)
        atoms_by_chain[atom.parent.parent].add(atom)

    for atom in atoms:
        cube = get_cube(atom)
        atoms_in_chain = atoms_by_chain[atom.parent.parent]
        yield from (
            (atom, a)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            for k in [-1, 0, 1]
            for a in atoms_by_cube[tuple(cube + numpy.array([i, j, k]))] - atoms_in_chain
            if dist(a, atom) <= max_distance
        )
        atoms_by_cube[tuple(cube)].remove(atom)


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
