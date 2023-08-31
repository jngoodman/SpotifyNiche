In python 3, if you're using `unittest.TestCase`:

https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory

-   You must have an empty (or otherwise) `__init__.py` file in your test directory (must be named test/)

-   Your test files inside test/ match the pattern `test_*.py`.

    -   They can be inside a subdirectory under `test/`. Those subdirectories can be named as anything, but they all need to have an `__init__.py` file in them

-   Then, you can run all the tests with:

```bash
python -m unittest
```
