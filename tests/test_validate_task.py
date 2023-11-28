import pytest

from validate_task_string import validate_ver


@pytest.mark.parametrize(
    'version_string',
    [
        '1helloabch'
    ]
)
def test_validate_ver(version_string):
    assert validate_ver(version_string)