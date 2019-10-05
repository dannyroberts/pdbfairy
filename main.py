import collections
import math
import sys

from Bio import PDB
from numpy import linalg
import numpy


MAX_DISTANCE = 4


def main(structure, max_distance):
    atom_pairs = find_pairs(structure, max_distance)
    res_pairs = set()
    for atom_1, atom_2 in atom_pairs:
        res_pairs.add((atom_1.parent, atom_2.parent))

    for res_1, res_2 in res_pairs:
        print('{}\t{}'.format(format_res(res_1), format_res(res_2)))
        print('{}\t{}'.format(format_res(res_2), format_res(res_1)))


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
            for a in (atoms_by_cube[tuple(cube + numpy.array([i, j, k]))]
                      - atoms_in_chain)
            if dist(a, atom) <= max_distance
        )
        atoms_by_cube[tuple(cube)].remove(atom)


def dist(atom_1, atom_2):
    return linalg.norm(atom_1.coord - atom_2.coord)


def format_res(res):
    return '{}\t{}'.format(res.parent.id, res.id[1])


if __name__ == '__main__':
    pdb_file = sys.argv[1]
    try:
        max_distance = float(sys.argv[2])
    except IndexError:
        max_distance = MAX_DISTANCE
    parser = PDB.PDBParser()
    structure = parser.get_structure('DATA', pdb_file)
    main(structure, max_distance)
