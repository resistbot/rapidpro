from __future__ import unicode_literals, absolute_import

from django.urls import reverse
from temba.tests import TembaTest
from ...models import Channel


class BlackmynaTypeTest(TembaTest):

    def test_claim(self):
        Channel.objects.all().delete()

        url = reverse('channels.claim_blackmyna')

        self.login(self.admin)

        response = self.client.get(reverse('channels.channel_claim'))
        self.assertNotContains(response, url)

        self.org.timezone = "Asia/Kathmandu"
        self.org.save()

        # check that claim page URL appears on claim list page
        response = self.client.get(reverse('channels.channel_claim'))
        self.assertContains(response, url)

        # try to claim a channel
        response = self.client.get(url)
        post_data = response.context['form'].initial

        post_data['country'] = 'NI'
        post_data['number'] = '250788123123'
        post_data['username'] = 'user1'
        post_data['password'] = 'pass1'

        response = self.client.post(url, post_data)

        channel = Channel.objects.get()

        self.assertEquals('NI', channel.country)
        self.assertEquals(post_data['username'], channel.config_json()['username'])
        self.assertEquals(post_data['password'], channel.config_json()['password'])
        self.assertEquals('+250788123123', channel.address)
        self.assertEquals('BM', channel.channel_type)

        config_url = reverse('channels.channel_configuration', args=[channel.pk])
        self.assertRedirect(response, config_url)

        response = self.client.get(config_url)
        self.assertEquals(200, response.status_code)

        self.assertContains(response, reverse('handlers.blackmyna_handler', args=['status', channel.uuid]))
        self.assertContains(response, reverse('handlers.blackmyna_handler', args=['receive', channel.uuid]))

        Channel.objects.all().delete()

        response = self.client.get(url)
        post_data = response.context['form'].initial

        post_data['country'] = 'NI'
        post_data['number'] = '20050'
        post_data['username'] = 'user1'
        post_data['password'] = 'pass1'

        response = self.client.post(url, post_data)

        channel = Channel.objects.get()

        self.assertEquals('NI', channel.country)
        self.assertEquals(post_data['username'], channel.config_json()['username'])
        self.assertEquals(post_data['password'], channel.config_json()['password'])
        self.assertEquals('20050', channel.address)
        self.assertEquals('BM', channel.channel_type)