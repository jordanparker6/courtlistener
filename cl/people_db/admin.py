from django.contrib import admin

from cl.people_db.models import (
    Education, School, Person, Position, RetentionEvent, 
    Race, PoliticalAffiliation, Source, ABARating
)


class RetentionEventInline(admin.TabularInline):
    model = RetentionEvent
    extra = 1


class PositionAdmin(admin.ModelAdmin):
    list_filter = (
        'court__jurisdiction',
    )
    inlines = (
        RetentionEventInline,
    )


class PositionInline(admin.StackedInline):
    model = Position
    extra = 1
    fk_name = 'person'
    raw_id_fields = ('court',)


class EducationAdmin(admin.ModelAdmin):
    search_fields = (
        'school__name',
        'school__ein',
    )


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    raw_id_fields = ('school',)

class PoliticalAffiliationInline(admin.TabularInline):
    model = PoliticalAffiliation
    extra = 1


class SourceInline(admin.TabularInline):
    model = Source
    extra = 1


class ABARatingInline(admin.TabularInline):
    model = ABARating
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name_first', 'name_middle', 'name_last',
                                    'name_suffix']}
    inlines = (
        PositionInline,
        EducationInline,
        PoliticalAffiliationInline,
        SourceInline,
        ABARatingInline,
    )
    search_fields = (
        'name_last',
        'name_first',
        'fjc_id',
    )
    list_filter = (
        'gender',
    )
    list_display = (
        'name_full',
        'gender',
        'fjc_id',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(School)
admin.site.register(Position, PositionAdmin)
admin.site.register(PoliticalAffiliation)
admin.site.register(RetentionEvent)
admin.site.register(Race)
admin.site.register(Source)
admin.site.register(ABARating)
