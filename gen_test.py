import json
import os
import sys

from Bio import PDB

from main import MAX_DISTANCE, dist


def main(structure, max_distance, output_file):
    with open(output_file, 'w') as f:
        json.dump(run_find_pairs_algorithm(
            find_pairs_brute_force, structure, max_distance), f)


def run_find_pairs_algorithm(find_pairs_fn, structure, max_distance):
    sorted_pairs = list()
    for atom_1, atom_2 in find_pairs_fn(structure, max_distance):
        sorted_pairs.append(sorted([atom_1.serial_number, atom_2.serial_number]))
    return sorted(sorted_pairs)


def find_pairs_brute_force(structure, max_distance):
    chains = list(structure.get_chains())
    for c, chain_1 in enumerate(chains):
        for chain_2 in chains[c + 1:]:
            for atom_1 in chain_1.get_atoms():
                for atom_2 in chain_2.get_atoms():
                    if dist(atom_1, atom_2) <= max_distance:
                        yield (atom_1, atom_2)


if __name__ == '__main__':
    pdb_name = sys.argv[1]  # not including .pdb suffix
    try:
        max_distance = float(sys.argv[2])
    except IndexError:
        max_distance = MAX_DISTANCE
    parser = PDB.PDBParser()
    pdb_file = os.path.join(
        'tests', 'data', 'input', '{}.pdb'.format(pdb_name))
    output_file = os.path.join(
        'tests', 'data', 'output', '{}.json'.format(pdb_name))
    structure = parser.get_structure('DATA', pdb_file)
    main(structure, max_distance, output_file=output_file)
