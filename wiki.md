Contributing to [autokey wiki samples](https://github.com/autokey/autokey/wiki/Scripting#advanced-scripts)

### Dynamically assign hotkey actions

**Author**: [tomrule007](https://github.com/tomrule007)

**Description**: Sample script that uses global value to toggle hotkey actions.

Enable script - sets enabled True and passes hotkey through.

```python
store.set_global_value("enabled", True)
keyboard.send_keys("<escape>")
```

Disable script - sets enabled False and passes hotkey through.

```python
store.set_global_value("enabled", False)
keyboard.send_keys(" ")
```

Action script - checks global value to determine action and also handles unset global with a default setting.

```python
try:
    enabled = store.get_global_value("enabled")
except TypeError:
    enabled = True #default setting

if enabled:
    # Do this if enabled.
else:
    # Do this if disabled.
```
