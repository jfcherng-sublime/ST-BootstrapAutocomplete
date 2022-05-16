# BootstrapAutocomplete Changelog

## 1.3.6

- revert: refactor: tidy codes

## 1.3.5

- refactor: tidy codes
- chore: update db for 5.2.0-beta1
- refactor: improve type annotations

## 1.3.4

- refactor: simplify `boot.py`

## 1.3.3

- fix: modules should be reloaded when update plugin
- refactor: simplify codes

## 1.3.2

- feat: add a script to download & parse all classes
- refactor: split the db into corresponding versions

## 1.3.1

- fix: plugin not working

## 1.3.0

- feat: add support for Bootstrap `v2`
- chore: update Bootstrap classes for `v3.4.1` and `v5.1.0`

## 1.2.7

- fix: extract BS 5 classes from `bootstrap.css`
- refactor: utilize `AioSettings`
- refactor: allow `versions` like `"5"` if there is only a version used

  ```js
  {
      "versions": "5",
  }
  ```

## 1.2.6

- refactor: simplify codes

## 1.2.5

- refactor: just some internal tidy codes

## 1.2.4

- fix: selector cannot has nested groups

  Actually, I think this is a bug in ST core...

  ```py
  >>> sublime.score_selector('a b', '(a (b))')
  0
  ```

## 1.2.3

- refactor: use singular filename

## 1.2.2

- refactor: simplify codes

## 1.2.1

- chore(ci): add tests

## 1.2.0

- docs: add `CHANGELOG.md`
- refactor: move py files into `plugin/`
- refactor: split `functions.py` into `settings.py` and `completions.py`

## 1.1.0

- feat: merge duplicate AC items for different versions

## 1.0.1

- chore: rename `db.json` to `completion-db.json`
- docs: update readme

## 1.0.0

- init
