from django.contrib import admin
from .models import Test
from .models import Profile
from .models import Test_hard
from .models import Test_eng
from .models import Test_hard_eng
from .models import Test_datastructure
from .models import Test_hard_datastructure


class TestAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


class Test_hardAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


class Test_engAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


class Test_hard_engAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")

class Test_datastructureAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")


class Test_hard_datastructureAdmin(admin.ModelAdmin):
    list_display = ('question', "option_1", "option_2", 'option_3', 'option_4', "answer")



admin.site.register(Test, TestAdmin)
admin.site.register(Test_hard , Test_hardAdmin)
admin.site.register(Test_eng, Test_engAdmin)
admin.site.register(Test_hard_eng , Test_hard_engAdmin)
admin.site.register(Test_datastructure, Test_datastructureAdmin)
admin.site.register(Test_hard_datastructure, Test_hard_datastructureAdmin)


admin.site.register(Profile)



