# cli/securestack/aws/provision.py
import subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]

def provision(env: str):
    tf_dir = ROOT / "terraform" / "envs" / env
    subprocess.check_call(["terraform", "init"], cwd=tf_dir)
    subprocess.check_call(["terraform", "apply", "-auto-approve"], cwd=tf_dir)
