default:
	@echo "Examples:"
	@echo "    make setup        # Setups a virutal environment and installs packages as needed"
	@echo "    make clean        # Cleans all directors"
	@echo "    make test         # Runs unit tests"
	@echo "    make rst          # Autogenerates Sphinx documentation for any new files that may have been added since last autodoc run"

setup:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

clean:
	rm -r *~

test:	
	py.test --cov-report html --cov app tests

rst:
	sphinx-apidoc -f -o docs/source/ app/
