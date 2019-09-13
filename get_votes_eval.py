def vote_count(klass, id):
    expression = f"Picture.objects.get(id = {id}).{klass}_set.all().count()"
    return eval(expression)