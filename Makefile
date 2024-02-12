.PHONY: es-delete-indexes
es-delete-indexes:
	python -m app.presentation.cli.delete_es_indexes

.PHONY: es-create-indexes
es-create-indexes:
	python -m app.presentation.cli.create_es_indexes

.PHONY: transfer-data-into-es
transfer-data-into-es:
	python -m app.presentation.cli.transfer_data_into_es
