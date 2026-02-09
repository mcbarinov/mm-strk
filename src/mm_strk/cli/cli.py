"""CLI entry point for mm-strk."""

from typing import Annotated

import typer
from mm_clikit import TyperPlus

from mm_strk.cli import commands

app = TyperPlus(package_name="mm-strk", no_args_is_help=True, pretty_exceptions_enable=False, add_completion=False)


@app.command(name="node", aliases=["n"], help="Checks RPC URLs for availability and status")
def node_command(
    urls: Annotated[list[str], typer.Argument()],
    proxy: Annotated[str | None, typer.Option("--proxy", "-p", help="Proxy")] = None,
) -> None:
    """Check RPC node availability and status."""
    commands.node.run(urls, proxy)
