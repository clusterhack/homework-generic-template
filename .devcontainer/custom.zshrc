
###############################################################
# Appended to end of .zshrc upon container setup

# Customizations for agnoster theme

if [[ -n $GITHUB_USER ]]; then
  prompt_context() { prompt_segment black default "$GITHUB_USER" }
else
  prompt_context() { } # Not very useful in a container otherwise...
fi

if [[ -n $WORKSPACE_ROOT ]]; then
  WORKSPACE_ROOT_BASE="$(basename "$WORKSPACE_ROOT")"
  prompt_dir() {
    local dir
    if [[ $PWD == $WORKSPACE_ROOT* ]]; then
      # prompt_segment magenta $CURRENT_FG "\ueb45 $WORKSPACE_ROOT_BASE"  # Requires NerdFont..
      prompt_segment magenta $CURRENT_FG "\U1f5bf $WORKSPACE_ROOT_BASE"
      prompt_segment blue $CURRENT_FG "${PWD/#"$WORKSPACE_ROOT"/}/"
    else
      prompt_segment red white '\u26a0 \u27e8out of workspace folder\u27e9'
      prompt_segment blue $CURRENT_FG '%~/'
    fi
  }
fi

if [[ -z "$VIRTUAL_ENV" ]]; then
  # Show warning message (should hopefully reduce dangerous confusion?)
  prompt_virtualenv() { prompt_segment red white '\u26a0 \u27e8no python env\u27e9' }
else
  # Devcontainer sets VIRTUAL_ENV_DISABLE_PROMPT, so no need to check...
  prompt_virtualenv() { prompt_segment blue black "(${VIRTUAL_ENV:t:gs/%/%%})" }
fi
