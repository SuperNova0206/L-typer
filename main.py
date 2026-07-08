import typer as tp

def main(name="world") -> None : 
	print(f"Hello {name.capitalize()}!")

if __name__ == "__main__" : tp.run(main)