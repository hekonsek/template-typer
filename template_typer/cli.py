import typer


app = typer.Typer()

@app.command(name="helloworld")
def helloworld():
    typer.echo("Hello World")

def main():
    app()

if __name__ == "__main__":
    main()