from pdbfairy.commands import find_interactions
import parameterized
import tests.loader


@parameterized.parameterized([
    '3trz'
])
def test_find_pairs(dataset_name):
    loader = tests.loader.Loader(dataset_name)
    structure = loader.get_structure()
    expected_pairs = loader.get_expected_output()
    actual_pairs = run_find_pairs_algorithm(
        find_interactions.find_pairs, structure, find_interactions.MAX_DISTANCE)
    assert expected_pairs == actual_pairs, (expected_pairs, actual_pairs)


def run_find_pairs_algorithm(find_pairs_fn, structure, max_distance):
    sorted_pairs = list()
    for atom_1, atom_2 in find_pairs_fn(structure, max_distance):
        sorted_pairs.append(sorted([atom_1.serial_number, atom_2.serial_number]))
    return sorted(sorted_pairs)
