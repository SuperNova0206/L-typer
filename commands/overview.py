import typer
from typing import Annotated

App : typer.Typer = typer.Typer(no_args_is_help=True)


@App.command()
def create(user : Annotated[str | None, typer.Argument(help="Creating a user", rich_help_panel="CRUD (create, read, update, delete) option")] = None) -> None : 
    if user : 
        print("The user {} created successfully".format(user))
        return
    print("Something went wrong! we couldn't create the user {}".format(user))


@App.command()
def delete(user_id : Annotated[int | None, typer.Option(help="Deleting a user using his id", rich_help_panel="CRUD (create, read, update, delete)option")] = None) -> None :
    if user_id >= 1 : 
        print("The user {} deleted successfully".format(user_id))
        return
    print("Something went wrong! we couldn't delete the user {}".format(user_id))


if __name__ == "__main__" : App()


