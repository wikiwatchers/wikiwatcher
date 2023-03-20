def add_params_to_url(parameter, value, base_url, operator):
    """ adds parameters to URL """
    base_url += parameter
    base_url += value
    base_url += operator
    return base_url
