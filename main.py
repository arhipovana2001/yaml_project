def decorated(func):
    """decorator function"""
    import functools
    import yaml

    @functools.wraps(func)
    def wrapped(*args):
        """function shows information on the screen in yaml format"""
        result = func(*args)
        result = yaml.dump(result)
        return result

    return wrapped
