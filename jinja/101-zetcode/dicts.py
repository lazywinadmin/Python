#!/usr/bin/env python3

from jinja2 import Template

person = {
    'name': 'Person',
    'age': 34
}

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
msg = tm.render(per=person)

print(msg)