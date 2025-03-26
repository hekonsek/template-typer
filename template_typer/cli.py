import typer

# Root command

app = typer.Typer(no_args_is_help=True)

# Some subcommands section 

app_some_command = typer.Typer(no_args_is_help=True)
app.add_typer(app_some_command, name="some-command")

@app_some_command.command(name="subcommand")
def subcommand():
    typer.echo("Hello world!")

# Main section

def main():
    app()

if __name__ == "__main__":
    main()