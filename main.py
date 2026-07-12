import typer 
from rich import print
from typing import TypedDict

class UserData(TypedDict) : 
	name : str
	age : int
	items :  list[dict[str, str], dict[str, str]]
	active : bool
	affiliation : None

data : UserData = {
	"name" : "Rick",
	"age" : 42,
	"items" : [{"name": "Portal Gun"}, {"name": "Plumbus"}],
	"active" : True,
	"affiliation" : None
}

app = typer.Typer()

@app.command()
def hello(name : str = "world" ) -> None : 
	print(f"Hello {name.capitalize()}!")

# I got an error I can't use a costumized type hint.
@app.command()
def info(data : UserData = data) -> None : 
	print("User data: ")
	print(data)

@app.command()
def goodbye(name : str, formal : bool = False) -> None : 
	if formal: 
		print(f"Goodbye Ms. {name.capitalize()}. have a good day.")
	else :
		print(f"Bye {name.capitalize()}!")

if __name__ == "__main__" : app()