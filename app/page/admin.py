from django.contrib import admin

from .models import Page, VideoContent, AudioContent, TextContent


class VideoContentInline(admin.TabularInline):
    model = VideoContent.pages.through
    extra = 1


class AudioContentInline(admin.TabularInline):
    model = AudioContent.pages.through
    extra = 1


class TextContentInline(admin.TabularInline):
    model = TextContent.pages.through
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    inlines = (
        VideoContentInline,
        AudioContentInline,
        TextContentInline,
    )


@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    fields = (
        'title',
        'url',
        'subtitles_url',
        'counter',
    )
    readonly_fields = ('counter',)
    inlines = (
        VideoContentInline,
    )


@admin.register(AudioContent)
class AudioContentAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    fields = (
        'title',
        'bitrate',
        'counter',
    )
    readonly_fields = ('counter',)
    inlines = (
        AudioContentInline,
    )


@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    fields = (
        'title',
        'text',
        'counter',
    )
    readonly_fields = ('counter',)
    inlines = (
        TextContentInline,
    )
