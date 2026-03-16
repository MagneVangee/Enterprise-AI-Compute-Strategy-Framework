# MLOps Makefile for Enterprise AI Strategy Framework

.PHONY: install test lint docker-build analyze-roi help

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 advisory_engine/ compute_stack/

docker-build:
	docker build -t magne-ai-framework:latest .

analyze-roi:
	python advisory_engine/tco_calculator.py --nodes 32 --power_kwh 0.12

help:
	@echo "Enterprise AI Compute Strategy Framework Commands:"
	@echo "  make install      Install dependencies"
	@echo "  make analyze-roi  Run 32-node TCO/ROI analysis"
	@echo "  make docker-build Build executive container"
