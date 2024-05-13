from factory import ExtractorFactory
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import API_CONFIG


def lambda_handler(event, context):
    source_type = event['source_type']
    api_url = event['api_url']
    endpoint = event['endpoint']

    factory = ExtractorFactory()
    extractor = factory.get_extractor(source_type, api_url)
    data = extractor.fetch_data(endpoint)
    processed_data = extractor.process_data(data)

    return processed_data
