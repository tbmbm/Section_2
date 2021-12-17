<!DOCTYPE html>
<html>
  <head>
  <style>
  ul#menu li {
      display:inline;
  }
  </style>
  {% if title %}
      <title>{{ title }}</title>
      {% else %}
      <title> No title specified</title>
      {% endif %}
  </head>
  <body>
    <ul id="menu">
      <li><a href="{{url_for('UserHomePage')}}">Home</a></li>
      <li><a href="{{url_for('MarkingAsComplete')}}">Uncompleted Task</a></li>
      <li><a href="{{url_for('CreatingNewAssessment')}}">Create New Assessment</a></li>
      <li><a href="{{url_for('Completed')}}">Completed Tasks</a></li>
    </ul>

    <div>
      {% block content %}{% endblock %}
    </div>
  </body>
</html>
