import json
import os

from Bio import PDB


class Loader(object):
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def get_structure(self):
        return PDB.PDBParser().get_structure(
            self.dataset_name, self.pdb_file)

    def get_expected_output(self):
        with open(self.output_file) as f:
            return json.load(f)

    @property
    def pdb_file(self):
        return os.path.join(
            'tests', 'data', 'input', '{}.pdb'.format(self.dataset_name))

    @property
    def output_file(self):
        return os.path.join(
            'tests', 'data', 'output', '{}.json'.format(self.dataset_name))
