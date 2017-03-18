all:
	@echo "try 'make txt' or 'make dot' if you have graphviz"

txt:
	python earley_parser.py

dot: 
	python main.py > output.dot
	dot -Tpdf output.dot -o output.pdf
	evince output.pdf 

clean:
	rm *~ *.png *.dot *.pyc *.pdf output output.flat 2> /dev/null || true
