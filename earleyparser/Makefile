all: dot


flat:
	python earley_parser.py > output.flat
	less -R output.flat

dot: 
	python output.py > output.dot
	dot -Tpdf output.dot -o output.pdf
	evince output.pdf 

clean:
	rm *~ *.png *.dot *.pyc *.pdf output output.flat 2> /dev/null || true
