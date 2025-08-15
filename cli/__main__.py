# cli/securestack/__main__.py
import typer
from .aws.provision import provision
from .aws.destroy import destroy

app = typer.Typer(help="SecureStack Ops CLI")

@app.command()
def up(env: str = typer.Option("sandbox", help="Environment name")):
    """Provision the secure app stack."""
    provision(env)

@app.command()
def down(env: str = typer.Option("sandbox", help="Environment name")):
    """Tear down the app stack."""
    destroy(env)

if __name__ == "__main__":
    app()
