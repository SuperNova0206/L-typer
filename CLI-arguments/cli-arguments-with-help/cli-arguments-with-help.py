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

# default value, help and docstring
def main_v3(name : Annotated[str, typer.Argument(metavar="👤 name")] = "World") -> None :
    """
    Display the message hello 'name'
    """
    print("Hello {}".format(name))

# rich help panel 
def main_v4(
        name : Annotated[str, typer.Argument(metavar="🧑 Username", rich_help_panel="Required arguments")],
        age : Annotated[int, typer.Argument(help="User age", rich_help_panel="Required arguments")],
        zib_code : Annotated[int, typer.Argument(help="User zib code", rich_help_panel="Secondary argument")] = 3000,
        info : bool = False
) -> None :
    if info :
        print("Hello {} 👋\nAge : {}\nZib code : {}".format(name, age, zib_code))
        return
    print("Hello {}👋".format(name))

if __name__ == "__main__" : typer.run(main_v4)