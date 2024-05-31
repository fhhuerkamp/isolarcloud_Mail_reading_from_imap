import pytest
from imap_reading.helper.get_env import get_env

def test_get_env():
    imap_user = get_env("TEST_IMAPUSER",source="dotenv")
    assert imap_user == "fhh@huerkamp.de"
