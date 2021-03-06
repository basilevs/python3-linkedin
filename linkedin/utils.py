def make_enum(enum_type='enum', base_classes=(), methods={}, **attrs):
    """
    Generates a enumeration with the given attributes.
    """
    # Enumerations can not be initalized as a new instance
    def __init__(instance, *args, **kwargs):
        raise RuntimeError('%s types can not be initialized.' % enum_type)

    base_classes = base_classes + (object,)
    for k, v in methods.items():
        methods[k] = classmethod(v)

    attrs['enums'] = attrs.copy()
    methods.update(attrs)
    methods['__init__'] = __init__
    return type(enum_type, base_classes, methods)


def to_utf8(st):
    if isinstance(st, str):
        return st.encode('utf-8')
    else:
        return str(st)

HTTP_METHODS = make_enum('HTTPMethod', GET='GET', POST='POST',
                         PUT='PUT', DELETE='DELETE', PATCH='PATCH')
