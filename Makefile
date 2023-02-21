install: test
	pip install -r requirements.txt
    
test:
	pytest

setup:
	python install .

clean:
	rm -rf __pycache__