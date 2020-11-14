from django.contrib import admin
from .models import Post,Test,Comment,MarketPost,AgriComment,PostAgriProblem

admin.site.site_header="Agridoctor"
admin.site.site_title="Agridoctor"

admin.site.register(Post)
admin.site.register(MarketPost)
admin.site.register(Test)
admin.site.register(Comment)
admin.site.register(AgriComment)
admin.site.register(PostAgriProblem)
