# cli/securestack/aws/destroy.py
import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
def destroy(env: str):
    tf_dir = ROOT / "terraform" / "envs" / env
    subprocess.check_call(["terraform", "destroy", "-auto-approve"], cwd=tf_dir)
