############################################################################
##        Base image

ARG VARIANT="3.12-bookworm"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
#   gawk: For convenience (mkzip.sh), even though not needed by students
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends gawk \
#     && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# [Add-on; Optional] Uncomment this section to install latest fzf release
# COPY .devcontainer/install-fzf.sh /tmp/install-fzf.sh
# RUN /bin/bash /tmp/install-fzf.sh && rm -f /tmp/install-fzf.sh


############################################################################
##        VSCode user -- additional setup

ARG USERNAME="vscode"
USER ${USERNAME}:${USERNAME}

ARG VENV_PATH="/home/${USERNAME}/venv"

# Create virtualenv and install required packages (via pip)
COPY --chown=${USERNAME}:${USERNAME} requirements.txt .devcontainer/requirements-dev.txt /tmp/pip-tmp/
RUN python -m venv /home/vscode/venv \
    && ${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt -r /tmp/pip-tmp/requirements-dev.txt \
    && rm -rf /tmp/pip-tmp

# Configure git pull.rebase
#   This is a workaround for GitHub Classroom: it occasionally takes a while to set up repo,
#   so if students clone it before the bots are done, pushing back to GitHub will fail...
RUN git config --global pull.rebase true

# [Add-on] Install zsh-autosuggestions plugin
RUN git clone https://github.com/zsh-users/zsh-autosuggestions /home/${USERNAME}/.oh-my-zsh/custom/plugins/zsh-autosuggestions

# [Add-on] Tweak zsh configuration
#   These edits have the be before oh-my-zsh.sh is sourced
RUN sed -i -E 's/^ZSH_THEME=.*$/ZSH_THEME="agnoster"/g' /home/${USERNAME}/.zshrc
RUN sed -i -E 's/^plugins=.*$/plugins=(git zsh-autosuggestions)/g' /home/${USERNAME}/.zshrc \
    && sed -i -E 's/^# (zstyle '"'"':omz:update'"'"' mode disabled.*)$/\1/g' /home/${USERNAME}/.zshrc
#   Additional tweaks can be appended at the end of the file
COPY --chown=${USERNAME}:${USERNAME} .devcontainer/custom.zshrc /tmp/
RUN cat /tmp/custom.zshrc >>/home/${USERNAME}/.zshrc \
    && rm -f /tmp/custom.zshrc
