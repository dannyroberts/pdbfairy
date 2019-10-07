import difflib

import parameterized

from pdbfairy import main
from pdbfairy.commands import find_interactions
from pdbfairy import utils
import tests.loader


@parameterized.parameterized([
    '3trz'
])
def test_find_interactions(dataset_name):
    loader = tests.loader.Loader(dataset_name)
    expected_tsv_output = loader.get_expected_find_interactions()
    with utils.capture() as out:
        find_interactions.find_interactions(
            loader.pdb_file, find_interactions.MAX_DISTANCE)

    actual_tsv_output, _ = out
    assert expected_tsv_output == actual_tsv_output, (
        '\n'.join(
            difflib.Differ().compare(
                expected_tsv_output.splitlines(),
                actual_tsv_output.splitlines(),
            )
        )
    )
