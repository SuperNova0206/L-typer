from typing import Annotated
import typer 

app : typer.Typer = typer.Typer()


@app.command()
def main(
    user_name : Annotated[str, typer.Argument(help="User name", rich_help_panel="Required argument")],
    last_name : Annotated[str, typer.Option("--lname", "-ln", help="User last name", rich_help_panel="Required option")],
    formal : Annotated[bool, typer.Option("-f", help="Formal greeting or informal greeting", rich_help_panel="Optional option")] = False
) -> None :
    print("Hello {} {}! how are you doing today".format(user_name, last_name)) if not formal else print("Good Morning Mr. {} {}".format(user_name, last_name))


if __name__ == "__main__" : app()