import difflib

import parameterized

from pdbfairy import main
from pdbfairy.commands import compare_interactions, find_interactions
from pdbfairy import utils
import tests.loader


@parameterized.parameterized([
    '3trz'
])
def test_compare_interactions(dataset_name):
    loader = tests.loader.Loader(dataset_name)
    expected_tsv_output = loader.get_expected_compare_interactions()
    with utils.capture() as out:
        compare_interactions.compare_interactions(
            loader.pdb_file, loader.pdb_file_compare,
            find_interactions.MAX_DISTANCE)

    actual_tsv_output, _ = out
    assert expected_tsv_output == actual_tsv_output, (
        '\n'.join(
            difflib.Differ().compare(
                expected_tsv_output.splitlines(),
                actual_tsv_output.splitlines(),
            )
        )
    )
