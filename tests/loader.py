import json
import os

from Bio import PDB


class Loader(object):
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

    def get_structure(self):
        return PDB.PDBParser().get_structure(
            self.dataset_name, self.pdb_file)

    @property
    def pdb_file(self):
        return os.path.join(
            'tests', 'data', 'input', '{}.pdb'.format(self.dataset_name))

    def get_expected_find_pairs(self):
        with open(self.find_pairs_file) as f:
            return json.load(f)

    @property
    def find_pairs_file(self):
        return os.path.join(
            'tests', 'data', 'find_pairs', '{}.json'.format(self.dataset_name))

    def get_expected_find_interactions(self):
        with open(self.find_interactions_file) as f:
            return f.read()

    @property
    def find_interactions_file(self):
        return os.path.join(
            'tests', 'data', 'find-interactions',
            '{}.tsv'.format(self.dataset_name))

    def get_expected_compare_interactions(self):
        with open(self.compare_interactions_file) as f:
            return f.read()

    @property
    def compare_interactions_file(self):
        return os.path.join(
            'tests', 'data', 'compare-interactions',
            '{}.tsv'.format(self.dataset_name))

    @property
    def pdb_file_compare(self):
        return os.path.join(
            'tests', 'data', 'input',
            '{}-compare.pdb'.format(self.dataset_name))
