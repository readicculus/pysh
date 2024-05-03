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
	rm -rf src/pysh/*.egg-info/
	rm -rf build/
	rm -rf dist/

.PHONY : build
build :
	rm -rf src/pysh/*.egg-info/
	python -m build

.PHONY : release
release :
	$(MAKE) clean
	$(MAKE) test
	python -m build