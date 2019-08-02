---
    layout: default
    title: Contact
    tagline: Contact
---

## Contact Me

Please feel free to get in touch!



<p>{% if site.email %}<a href="mailto: {{site.email}}"><i class="fa fa-envelope"> // email</i></a> {% endif %}</p>

<p>{% if site.website %}<a href="http://{{site.website}}" target="_blank"><i class="fa fa-globe"></i> // website</a>{% endif %}</p>

    {% if site.academiaedu %}
	   <a href="http://{{site.academiaedu}}" target="_blank"><i class="fa fa-graduation-cap"></i> </a> |
    {% endif %}
    {% if site.linkedin %}
	   <a href="https://in.linkedin.com/in/{{site.linkedin}}" target="_blank"><i class="fa fa-linkedin"></i> </a> |
    {% endif %}
    {% if site.github %}
	   <a href="http://github.com/{{site.github}}" target="_blank"><i class="fa fa-github"></i> </a>
    {% endif %}
</p>

jkerr@uoregon.edu

Joshua Kerr
Department of Philosophy
University of Oregon
Eugene, OR 97403
