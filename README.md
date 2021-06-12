# ST-BootstrapAutocomplete

This Sublime Text **4** plugin means to unify other Bootstrap autocompletion plugins.

- [Bootstrap 3 Autocomplete](https://packagecontrol.io/packages/Bootstrap%203%20Autocomplete)
- [Bootstrap 4 Autocomplete](https://packagecontrol.io/packages/Bootstrap%204%20Autocomplete)
- [Bootstrap 4x Autocomplete](https://packagecontrol.io/packages/Bootstrap%204x%20Autocomplete)
- Maybe more implicit ones...

This plugin is design to support various versions of Bootstrap's autocompletion with ease.
At this moment, it supports Bootstrap 3, 4 (default) and 5. If you find a missing class name,
an issue or pull request is always welcome.

![screenshot-st4](https://raw.githubusercontent.com/jfcherng-sublime/ST-BootstrapAutocomplete/main/docs/screenshot-st4.png)

## Installation

This package is available on Package Control by the name of [BootstrapAutocomplete](https://packagecontrol.io/packages/BootstrapAutocomplete).

## Global Settings

From the main menu: `Preferences` -> `BootstrapAutocomplete` -> `Settings`

```js
{
    // scopes that this plugin should activated
    "selectors": ["meta.attribute-with-value.class.html"],
    // targeted Bootstrap versions (available versions are: "3", "4", "5")
    "versions": ["4"],
}
```

## Project Settings

You most likely want to use only a specific version of Bootstrap in a project.
In that case, you can specify the version(s) you want to use in your project settings.

From the main menu: `Project` -> `Edit Project`

```js
{
    "folders":
    [
        // ...
    ],
    "settings": {
        // settings here will override global settings
        "BootstrapAutocomplete": {
            // use Bootstrap 5 for this project.
            "versions": ["5"],
        },
    },
}
```

## Acknowledgment

This plugin's autocompletion lists come from:

### Bootstrap 3 Sources

- [webchun/bootstrap-3-sublime-autocomplete](https://github.com/webchun/bootstrap-3-sublime-autocomplete/blob/b120b45677c31c1530df8a444fe0e4e18d72a555/bootstrap_3_autocomplete.py#L5)

### Bootstrap 4 Sources

- [proficientdesigners/sublime-text-bs4-autocomplete](https://github.com/proficientdesigners/sublime-text-bs4-autocomplete/blob/5f52ecd3724f61922d2fc73085023c7f421e9615/bootstrap_4_autocomplete.py#L4)

### Bootstrap 5 Sources

- [felixboet/bootstrap-5-classes-list](https://gist.github.com/felixboet/3ea836c3fac11b3ddb3efbddab17e957)
