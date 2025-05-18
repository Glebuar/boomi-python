import pytest

from boomi import Boomi, BoomiError
from boomi.resources import Components


def test_from_env(monkeypatch):
    monkeypatch.setenv("BOOMI_ACCOUNT", "acct")
    monkeypatch.setenv("BOOMI_USER", "user")
    monkeypatch.setenv("BOOMI_SECRET", "secret")

    client = Boomi.from_env()
    assert isinstance(client, Boomi)
    assert isinstance(client.components, Components)


def test_from_env_missing(monkeypatch):
    monkeypatch.delenv("BOOMI_ACCOUNT", raising=False)
    monkeypatch.delenv("BOOMI_USER", raising=False)
    monkeypatch.delenv("BOOMI_SECRET", raising=False)

    with pytest.raises(BoomiError):
        Boomi.from_env()
