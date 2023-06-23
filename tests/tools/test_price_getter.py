from typer.testing import CliRunner
from src.tools.price_getter import __app_name__, __version__
from tools.price_getter import service


runner = CliRunner()

def test_version():
    result = runner.invoke(service.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout