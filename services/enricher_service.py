import logging


class EnricherService:
    chunk_size = 10

    def __init__(self, gleif_service):
        self.gleif_service = gleif_service

    def enrich_data(self, dataset):
        lei_values = dataset['lei'].unique().tolist()

        dataset['legalName'] = ''
        dataset['bic'] = ''
        dataset['transaction_costs'] = None

        lei_chunks = [lei_values[i:i + self.chunk_size] for i in range(0, len(lei_values), self.chunk_size)]

        logging.info("Start processing chunks.")

        for i, lei_chunk in enumerate(lei_chunks, start=1):
            logging.info(f"Processing Chunk {i} with {len(lei_chunk)} LEIs...")

            api_data = self.gleif_service.call_gleif_api(lei_chunk, self.chunk_size)
            self._process_lei_entries(api_data, dataset)

            logging.info(f"Chunk {i} processed successfully.")

        logging.info("All chunks processed.")
        self._calculate_transaction_costs(dataset)
        logging.info("Transaction costs calculated successfully.")
        return dataset

    @staticmethod
    def _process_lei_entries(entries, dataset):
        for entry in entries:
            lei = entry['attributes']['lei']
            legal_name = entry['attributes']['entity']['legalName']['name']
            bic = entry['attributes']['bic']
            country = entry['attributes']['entity']['legalAddress']['country']

            mask = dataset['lei'] == lei
            dataset.loc[mask, 'legalName'] = legal_name
            dataset.loc[mask, 'bic'] = ', '.join(map(str, bic))
            dataset.loc[mask, 'country'] = country

    def _calculate_transaction_costs(self, dataset):
        for index, row in dataset.iterrows():
            country = row['country']
            notional = float(row['notional'])
            rate = float(row['rate'])

            transaction_costs = self._calculate_transaction_costs_for_country(country, notional, rate)
            dataset.at[index, 'transaction_costs'] = transaction_costs

    @staticmethod
    def _calculate_transaction_costs_for_country(country, notional, rate):
        if country == 'GB':
            return notional * rate - notional
        elif country == 'NL':
            return abs(notional * (1 / rate) - notional)
        else:
            return 0
