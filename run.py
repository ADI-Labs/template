import subprocess
import sys

from app import app, db

@app.cli.command()
def setup():
    """Setup the database"""
    db.create_all()


@app.cli.command()
def pgcli():
    """Opens up a pgcli REPL to the database"""
    try:
        from pgcli.main import cli as pgcli
    except ImportError:
        sys.exit("You need to install pgcli for this to work. Try:"
                 "\n    pip install pgcli")
    pgcli.main([str(db.engine.url)])

@app.cli.command()
def develop():
    """Run development server w/ ENV defaults"""
    subprocess.run([
        "flask", "run",
        "--host", app.config["HOST"],
        "--port", str(app.config["PORT"]),
    ])
