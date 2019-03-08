from django.contrib import admin
from .models import Summoner, NameChange
from .models import RankCheckpoint, RankPosition


class SummonerAdmin(admin.ModelAdmin):
    list_display = ('name', '_id', 'account_id')
    search_fields = ('name', 'simple_name', 'account_id', '_id', 'puuid')


class NameChangeAdmin(admin.ModelAdmin):
    list_display = ('summoner', 'old_name', 'created_date')
    search_fields = ('old_name', 'summoner__name', 'summoner__simple_name')


class RankCheckpointAdmin(admin.ModelAdmin):
    list_display = ('summoner', 'created_date')
    search_fields = ('summoner__name', 'summoner__simple_name', 'summoner__account_id')
    raw_id_fields = ('summoner',)


class RankPositionAdmin(admin.ModelAdmin):
    list_display = ('queue_type', 'rank', 'tier', 'position')
    search_fields = ('checkpoint__summoner__name', 'checkpoint__summoner__simple_name', 'checkpoint__summoner__account_id')
    raw_id_fields = ('checkpoint',)


admin.site.register(Summoner, SummonerAdmin)
admin.site.register(NameChange, NameChangeAdmin)
admin.site.register(RankCheckpoint, RankCheckpointAdmin)
admin.site.register(RankPosition, RankPositionAdmin)
