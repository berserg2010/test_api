from rest_framework import serializers

from page.models import Page, VideoContent, AudioContent, TextContent


class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ('id', 'title', 'counter', 'url', 'subtitles_url',)


class AudioContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioContent
        fields = ('id', 'title', 'counter', 'bitrate',)


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ('id', 'title', 'counter', 'text',)


class PageDetailSerializer(serializers.HyperlinkedModelSerializer):
    videocontent = VideoContentSerializer(source='videocontent_related', many=True, read_only=True)
    audiocontent = AudioContentSerializer(source='audiocontent_related', many=True, read_only=True)
    textcontent = TextContentSerializer(source='textcontent_related', many=True, read_only=True)

    class Meta:
        model = Page
        fields = (
            'url',
            'id',
            'title',
            'videocontent',
            'audiocontent',
            'textcontent',
        )


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = (
            'url',
            'id',
            'title',
        )
