#! /bin/bash
set -e

msg() { echo "$@" 1>&2; }

# Install Python requirements
msg "## Installing Python requirements..."
(
  python -m venv /home/vscode/venv && \
  /home/vscode/venv/bin/pip --disable-pip-version-check --no-cache-dir \
    install -r requirements.txt -r .devcontainer/requirements-dev.txt
)

# Install IPython default profile
msg "## Installing IPython profile configuration"
mkdir -p /home/vscode/.ipython/profile_default
cat >/home/vscode/.ipython/profile_default/ipython_config.py <<"EOF"
c = get_config()

try:
  import hwk.util.ipython
  c.InteractiveShellApp.extensions.append('hwk.util.ipython')
except ImportError:
  pass
EOF
