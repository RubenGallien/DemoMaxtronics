all:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -U Flask && \
	pip install -U mistralai && \
	flask  run --host=0.0.0.0 --port=5001

fclean:
	rm -rf .venv __pycache__ *.pyc
