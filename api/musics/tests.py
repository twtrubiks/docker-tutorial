# Create your tests here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from musics.models import Music


class MusicViewTestCase(APITestCase):
    url_reverse = reverse('api:music-list')
    url = '/api/music/'
    url_detail = '/api/music/{}/'
    url_detail_route_reverse = reverse('api:music-detail', kwargs={"pk": 1})
    url_detail_route = '/api/music/{}/detail/'
    url_list_route = '/api/music/all_singer/'

    def setUp(self):
        print('setUp')

        self.client = APIClient()
        # create user
        User.objects.create_user(username='test_user', password='password123')

        self.client.login(username='test_user', password='password123')

        self.request_data = {
            'song': 'song_test',
            'singer': 'singer_test'
        }

        self.music = Music.objects.create(song='song_test', singer='singer_test')

    def test_api_music_create(self):
        print('test_api_music_create')
        self.response = self.client.post(
            self.url,
            self.request_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Music.objects.count(), 2)
        self.assertEqual(Music.objects.get(pk=self.music.id).song, 'song_test')
        self.assertEqual(Music.objects.get(pk=self.music.id).singer, 'singer_test')

    def test_api_music_retrieve(self):
        print('test_api_music_retrieve')
        music = Music.objects.get(pk=self.music.id)
        response = self.client.get(self.url_detail.format(self.music.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('song', None), music.song)
        self.assertEqual(response.data.get('singer', None), music.singer)

    def test_api_music_partial_update(self):
        print('test_api_music_partial_update')
        update_song = {'song': 'song_update'}
        response = self.client.patch(self.url_detail.format(self.music.id), update_song, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('song', None), update_song.get('song', None))

    def test_api_music_update(self):
        print('test_api_music_update')
        update_song = {'song': 'song_update', 'singer': 'singer_update'}
        response = self.client.put(self.url_detail.format(self.music.id), update_song, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('song', None), update_song.get('song'))
        self.assertEqual(response.data.get('singer', None), update_song.get('singer'))

    def test_api_music_delete(self):
        print('test_api_music_delete')
        response = self.client.delete(self.url_detail.format(self.music.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_music_detail_route(self):
        print('test_api_music_detail_route')
        music = Music.objects.get(pk=self.music.id)
        response = self.client.get(self.url_detail_route.format(self.music.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('song', None), music.song)
        self.assertEqual(response.data.get('singer', None), music.singer)

    def test_api_music_list_route(self):
        print('test_api_music_list_route')
        music = Music.objects.values_list('singer', flat=True).distinct()
        response = self.client.get(self.url_list_route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(next(iter(response.data)), next(iter(music)))
