.PHONY: tests
tests:
	uv run python -m unittest discover -s tests -v
