def transform(legacy_data):
    new_dict = {}
    for key, val in legacy_data.items():
        new_dict.update(zip([char.lower() for char in val],([key]*len(val))))
    return new_dict
