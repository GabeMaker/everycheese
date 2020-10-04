{% extends "base.html" %}

{% block title %}Add Cheese{% endblock title %}

{% block content %}

<h1>Add Cheese</h1>

<form method="post" action="{% url 'cheeses:add' %}">
{% csrf_token %}
{{ form.as_p }}
<button type="submit" class="btn btn-primary">Save</button>
</form>
{% endblock content %}