from .extractors import WeatherExtractor, CountryExtractor

class ExtractorFactory:
    def get_extractor(self, source_type, *args, **kwargs):
        if source_type == 'weather':
            return WeatherExtractor(*args, **kwargs)
        elif source_type == 'country':
            return CountryExtractor(*args, **kwargs)
        else:
            raise ValueError("Unsupported source type")