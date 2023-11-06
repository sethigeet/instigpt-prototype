import os
from rich import print


def get_env_var(name: str) -> str:
    try:
        var = os.environ[name]
        return var
    except KeyError:
        print(
            f"[red]Please set the [bold]{name}[/bold] environment variable either through the `.env` file or using your shell!"
        )
        exit(1)
