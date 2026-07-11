import typer 

app = typer.Typer()

@app.command()
def main(name="world") -> None : 
	print(f"Hello {name.capitalize()}!")

@app.command()
def goodbye(name : str, formal : bool = False) -> None : 
	if formal: 
		print(f"Goodbye Ms. {name.capitalize()}. have a good day.")
	else :
		print(f"Bye {name.capitalize()}!")

if __name__ == "__main__" : app()