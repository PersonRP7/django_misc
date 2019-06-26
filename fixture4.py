def generate(app, model, rng):
    import random
    from django.apps import apps
    django_model = apps.get_model(app, model)
    text_data = [
        'William', 'Washington', 'Internet', 'Radio',
        'Django', 'Something', 'Plane', 'Snow', 'Rain',
        'Water', 'Blue', 'Yellow', 'Horse'
    ]
    integer_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    string_fields = []
    integer_fields = []
    for i in django_model._meta.get_fields():
        if i.get_internal_type() == 'CharField':
            string_fields.append(i.name)
        elif i.get_internal_type() == 'IntegerField':
            integer_fields.append(i.name)
    string_container = []
    integer_container = []
    for i in range(rng):
        string_container.append({key:random.choice(text_data) for key in string_fields})
        integer_container.append({key:random.choice(integer_data) for key in integer_fields})
    for string in string_container:
        for integer in integer_container:
            string.update(integer)
    for i in string_container:
        django_model.objects.create(**i)
