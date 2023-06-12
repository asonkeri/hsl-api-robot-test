import pytest
from HslApiLibrary import HslApiLibrary


@pytest.fixture(autouse=True)
def mock_api_key(monkeypatch):
    monkeypatch.setenv("HSL_API_KEY", "test_api_key")


def test_should_have_default_url():
    lib = HslApiLibrary()
    assert lib.url == 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'


def test_should_accept_custom_url():
    lib = HslApiLibrary(url='http://example.com')
    assert lib.url == 'http://example.com'


def test_should_raise_error_on_missing_api_key(monkeypatch):
    monkeypatch.delenv("HSL_API_KEY", raising=False)
    with pytest.raises(Exception) as exinfo:
        HslApiLibrary()
    assert 'HSL_API_KEY environment variable is not set' in str(exinfo.value)


def test_should_send_query(mocker):
    spy = mocker.patch('requests.Session.post')
    lib = HslApiLibrary()
    lib.query('stops(name: "Kamppi") { name }')
    spy.assert_called_once_with(
        lib.url, json={"query": "{stops(name: \"Kamppi\") { name }}"})
