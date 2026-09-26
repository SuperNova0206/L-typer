import typer
from rich.console import Console
app : typer.Typer = typer.Typer()
console : Console = Console()

data : list = ["Youssef", "Zineb"]

# add a user
def add_a_user(username : str) -> None :
    if username in data :
        console.print(f"The user {username} already exists!", style="orange_red1")
        raise typer.Exit()
    data.append(username)
    console.print(f"The user {username} added successfully!", style="dark_cyan")
    console.print(data)

# delete a user
def delete_a_user(userid : int) -> None :
    if userid > len(data) :
        console.print(f"User number {userid} doesn't exist!", style="red1")
        raise typer.Exit()
    data.pop(userid - 1)
    console.print(f"The user number {userid} has deleted successfully!", style="dark_cyan")
    console.print(data)


@app.command()
def add(username : str) :
    add_a_user(username=username)

@app.command()
def delete(userid : int) :
    delete_a_user(userid=userid)

if __name__ == "__main__" : app()
