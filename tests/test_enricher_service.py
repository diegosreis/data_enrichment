import pytest
import pandas as pd

from services.enricher_service import EnricherService


class TestEnricherService:

    @pytest.fixture
    def mock_gleif_service(self, mocker):
        return mocker.MagicMock()

    @pytest.fixture
    def enricher_service(self, mock_gleif_service):
        return EnricherService(gleif_service=mock_gleif_service)

    def test_enrich_data_calculate_transaction_costs(self, enricher_service):
        dataset = pd.DataFrame({
            'lei': ['LEI1', 'LEI2', 'LEI3'],
            'country': ['GB', 'NL', 'Other'],
            'notional': [100, 200, 300],
            'rate': [0.1, 0.2, 0.3]
        })

        enricher_service._calculate_transaction_costs(dataset)

        assert dataset['transaction_costs'].tolist() == [-90, 800, 0]

    def test_calculate_transaction_costs_for_country(self, enricher_service):
        assert enricher_service._calculate_transaction_costs_for_country('GB', 100, 0.1) == -90
        assert enricher_service._calculate_transaction_costs_for_country('NL', 200, 0.2) == 800
        assert enricher_service._calculate_transaction_costs_for_country('Other', 300, 0.3) == 0
