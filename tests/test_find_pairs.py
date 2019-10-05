import main
import parameterized
import tests.loader
import gen_test


@parameterized.parameterized([
    '3trz'
])
def test_find_pairs(dataset_name):
    loader = tests.loader.Loader(dataset_name)
    structure = loader.get_structure()
    expected_pairs = loader.get_expected_output()
    actual_pairs = gen_test.run_find_pairs_algorithm(
        main.find_pairs, structure, main.MAX_DISTANCE)
    assert expected_pairs == actual_pairs, (expected_pairs, actual_pairs)
