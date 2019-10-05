import collections
import math
import sys

from Bio import PDB
import memoized
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
    atom_store = AtomStore(atoms, max_distance=max_distance)
    for atom in atoms:
        yield from atom_store.find_neighbors(atom)
        atom_store.remove(atom)


class AtomStore(object):
    def __init__(self, atoms=(), max_distance=MAX_DISTANCE):
        # max distance for two atoms to be considered "neighbors"
        self.max_distance = max_distance
        self._atoms_by_cube = collections.defaultdict(set)
        self._atoms_by_chain = collections.defaultdict(set)
        for atom in atoms:
            self.add(atom)

    def add(self, atom):
        self._atoms_by_cube[tuple(self._get_cube(atom))].add(atom)
        self._atoms_by_chain[self._get_chain(atom)].add(atom)

    def remove(self, atom):
        self._atoms_by_cube[tuple(self._get_cube(atom))].remove(atom)
        self._atoms_by_chain[self._get_chain(atom)].remove(atom)

    def find_neighbors(self, atom):
        cube = self._get_cube(atom)
        atoms_in_chain = self._atoms_by_chain[self._get_chain(atom)]
        yield from (
            (atom, a)
            for offset in self._offsets
            for a in self._atoms_by_cube[tuple(cube + offset)] - atoms_in_chain
            if dist(a, atom) <= self.max_distance
        )

    @memoized.memoized
    def _get_cube(self, atom):
        return numpy.floor(atom.coord / self.max_distance)

    @memoized.memoized
    def _get_chain(self, atom):
        return atom.parent.parent

    _offsets = [
        numpy.array([i, j, k])
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        for k in [-1, 0, 1]
    ]


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
