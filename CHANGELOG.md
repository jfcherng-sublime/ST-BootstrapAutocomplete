# Changelog

All notable changes to this project will be documented in this file.

## [1.2.6] - 2021-07-17

- refactor: simplify codes

## [1.2.5] - 2021-07-09

- refactor: just some internal tidy codes

## [1.2.4] - 2021-06-17

- fix: selector cannot has nested groups

  Actually, I think this is a bug in ST core...

  ```py
  >>> sublime.score_selector('a b', '(a (b))')
  0
  ```

## [1.2.3] - 2021-06-12

- refactor: use singular filename

## [1.2.2] - 2021-06-12

- refactor: simplify codes

## [1.2.1] - 2021-06-12

- chore(ci): add tests

## [1.2.0] - 2021-06-12

- docs: add `CHANGELOG.md`
- refactor: move py files into `plugin/`
- refactor: split `functions.py` into `settings.py` and `completions.py`

## [1.1.0] - 2021-06-12

- feat: merge duplicate AC items for different versions

## [1.0.1] - 2021-06-12

- chore: rename `db.json` to `completion-db.json`
- docs: update readme

## [1.0.0] - 2021-06-06

- init
