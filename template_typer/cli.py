import typer
from typer import colors
from termcolor import colored

# Root command

app = typer.Typer(no_args_is_help=True)

# Subcommands 

app_some_command = typer.Typer(no_args_is_help=True)
app.add_typer(app_some_command, name="some-command")

@app_some_command.command(name="subcommand")
def subcommand():
    typer.echo("Hello world!")

# Colors

@app.command()
def styles():
   # Typer.style
    typer.echo(f"I'm {typer.style("bold and italic", bold=True, italic=True)}.")

    # Typer.secho
    typer.secho("I'm cyan text.", fg=colors.CYAN)
    typer.secho("I'm bright magnetta background!", bg=colors.BRIGHT_MAGENTA)

    # Termcolor
    typer.echo(f"I'm {colored("green text by termcolor", "green")} without Typer dependency.")

# Main section

def main():
    app()

if __name__ == "__main__":
    main()