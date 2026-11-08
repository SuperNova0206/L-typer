from typing import Annotated
import typer

# initialzing the app
app = typer.Typer()

namesAvailable : list = ["Youssef", "Zineb", "Amir"]
def names(name : str) -> list :
    completed_name = []
    for name in namesAvailable :
        if name.startswith(name) : 
            completed_name.append(name)
    return completed_name 
    

@app.command("hello")
def greeting(
    name : Annotated[str, typer.Option(help="User name (Say hello to [NAME])", autocompletion=names)] = "World"
) -> None : 
    print("Hello {}".format(name))



if __name__ == "__main__" : app()