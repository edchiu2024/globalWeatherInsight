from .extractors import WeatherExtractor, CountryExtractor


class ExtractorFactory:
    def get_extractor(self, event, *args, **kwargs):
        
        if event == 'weather':
            return WeatherExtractor(*args, **kwargs)
        elif event =='country':
            return CountryExtractor(*args, **kwargs)
        else:
            raise ValueError("Unsupported source type")
