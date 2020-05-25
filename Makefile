.PHONY: docs clean
# To help manage the document writing
docs:
	sphinx-build docs .doc_build

viewdocs:
	$(BROWSER) .doc_build/index.html

clean:
	rm -r .doc_build
