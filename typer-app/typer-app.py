import typer

app  = typer.Typer()

@app.command()
def hello(first_name : str, last_name : str = "", formal : bool = False) -> None: 
    if formal :
        print(f"Good evening Ms {first_name} {last_name}")
        return
    print("Hello {} 👋".format(first_name))

if __name__ == "__main__" : app()