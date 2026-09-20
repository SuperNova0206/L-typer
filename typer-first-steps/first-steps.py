import typer

def main(name : str, last_name : str = "", formal : bool = False) :
    """
        Accepts one argument and two Options\n
        [ + ] name : required\n 
        [ + ] last-name, formal : options\n 
        [ + ] formal default value : False, last-name default value : ""
    """
    if formal :
        print("Good morning Ms. {} {}".format(name, last_name))
    else : 
        print("Hello, {} {}".format(name, last_name))

if __name__ == "__main__" : typer.run(main)