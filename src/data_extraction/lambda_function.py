from .factory import ExtractorFactory
from kafka import KafkaProducer
import json
from utils import load_config
from logger import logging 


def lambda_handler():

    config=load_config()
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        retries=5,  # Maximum number of retries
        retry_backoff_ms=3000  # Wait time between retries in milliseconds
    )
    # List to keep track of futures
    futures=[]
   

    # Iterate through different data source type. Currently we only have the weather source type
    # TODO: Add other source types in config.json 
    for key in config['API_CONFIG']:
        kafka_message=[]
        for city in config['WEATHER_CONFIG']['cities']:
            messages=[]
            factory=ExtractorFactory()
            handler=factory.get_extractor(key, config['API_CONFIG'][key], params=city)
            data=handler.fetch_data()
            handler.save_raw_data(data)
            messages=handler.process_data(data,city)
            kafka_message.append(messages)
            
        json_data = json.dumps(kafka_message)
        byte_data = json_data.encode('utf-8')
        future = producer.send(config['API_CONFIG'][key]['kafka_topic'], byte_data)
        futures.append(future)

    for future in futures:
        try:
            # Wait for the send to complete with timeout
            result = future.get(timeout=60)
            logging.info(f"KAFKA: Message sent successfully for {result.topic}")
        except Exception as e:
            logging.error(f"Failed to send message after retries: {e}")
    producer.flush()
    producer.close()

    #return kafka_messages





