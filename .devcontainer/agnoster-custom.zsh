# Devcontainer sets VIRTUAL_ENV_DISABLE_PROMPT, so no need to check...
# Also, if no virtual env, show warning message (should hopefully reduce dangerous confusion?)
prompt_virtualenv() { 
  if [[ -z "$VIRTUAL_ENV" ]]; then
    prompt_segment red white '\u26a0 \u27e8no python env\u27e9' 
  else
    prompt_segment blue black "(${VIRTUAL_ENV:t:gs/%/%%})"
  fi
}
