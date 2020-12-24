{% extends "layouts/base.html" %}
{% load static %}

{% block content %}
<h1>{{ title }}</h1>
<hr>
<div class="row">
    <div class="col-6">
        <h1>Article List</h1>
        <hr>
        <div class="card">
            <div class="card-body">
                {{ obj.title }}
            </div>
        </div>
    </div>
</div>
{% endblock content %}
