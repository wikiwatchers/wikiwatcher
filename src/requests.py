def get_base_URL():
    return "http://127.0.0.1:5000/"

def update_URL(parameter, value, base_URL, operator):
    base_URL += parameter
    base_URL += value
    base_URL += operator
    return base_URL