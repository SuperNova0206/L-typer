import typer
from typing import Annotated

# documenting your command using the traditional way
def main_v1(name : str, lastname : str, formal : bool) -> None : 
    """
    Say hi to 'name', optionally with a --lastname
    if --formal is used, say hi very formally
    """

    if formal :
        print(f"Good day Ms {name} {lastname}")
    else :
        print(f"Hello {name} {lastname}")

# using help command
def main_v2(name : Annotated[str, typer.Argument(help="The name of the user to great")]) -> None :
    """
    Say hi to the 'name' very gently, like Dirk.
    """
    print("Hello {}".format(name))


if __name__ == "__main__" : typer.run(main_v2)