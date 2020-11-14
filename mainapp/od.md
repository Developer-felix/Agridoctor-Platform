pip install django-ckeditor

model.py 

from ckeditor import RichTextField

body = models.RichTextField(blank=True,null=True)

migrate and push migrations

settings.py
'ckeditor'

templates 
addpost
{{form.media}}
detail
{{post.body|safe}}

<div class="btn-group-vertical" role="group" aria-label="{{">
    <button type="button" class="btn btn-secondary"></button>
    <button type="button" class="btn btn-secondary"></button>
    <div class="btn-group" role="group">
        <button id="dropdownId" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true"
                aria-expanded="false">
            
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownId">
            <a class="dropdown-item" href="#"></a>
            <a class="dropdown-item" href="#"></a>
        </div>
    </div>
</div>