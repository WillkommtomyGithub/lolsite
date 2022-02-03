from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from player.serializers import ReputationSerializer
from player.tests import factories

from match.tests.factories import MatchFactory


User = get_user_model()


class ReputationSerializerTest(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.user = factories.UserFactory()
        slinks = factories.SummonerLinkFactory.create_batch(10, user=self.user)
        self.summoners = [x.summoner for x in slinks]
        self.client.force_login(self.user)
        self.matches = MatchFactory.create_batch(10, participants=10)

    def test_no_match_overlap_fails(self):
        summoner = self.summoners[0]
        for match in self.matches[:5]:
            p1 = match.participants.order_by('pk').first()
            p1.puuid = summoner.puuid
            p1.save()
