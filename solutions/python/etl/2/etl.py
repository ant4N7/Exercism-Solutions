def transform(legacy_data):
    return {char.lower(): key
           for key, values in legacy_data.items()
           for char in values}
