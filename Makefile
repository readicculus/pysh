#.PHONY : docs
#docs :
#	rm -rf docs/build/
#	sphinx-autobuild -b html --watch src/pysh	/ docs/source/ docs/build/

.PHONY : test
test :
	isort --check .
	black --check .
	ruff check .
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ src/pysh/

.PHONY : clean
clean :
	rm -rf src/*.egg-info
	rm -rf build/
	rm -rf dist/
	rm -rf .coverage

.PHONY : build
build :
	rm -rf src/*.egg-info
	python -m build

.PHONY : release
release :
	$(MAKE) clean
	$(MAKE) test
	python -m build