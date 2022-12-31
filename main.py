import base64
import hashlib

import requests

from helios_verifier.domain.CastVote import CastVote
from helios_verifier.domain.Election import Election
from helios_verifier.domain.Trustee import Trustee
from helios_verifier.domain.Voter import Voter
from helios_verifier.util.UrlUtil import ELECTION_BASE_URL, VOTERS_BASE_URL_WITH_ELECTION_PLACEHOLDER, \
    BALLOTS_BASE_URL_WITH_ELECTION_AND_VOTER_PLACEHOLDERS, \
    RESULTS_BASE_URL_WITH_ELECTION_PLACEHOLDER, \
    TRUSTEES_BASE_URL_WITH_ELECTION_PLACEHOLDER
from helios_verifier.verifiers.ElectionVerifier import retally_election


def verify(election_uuid):
    # deserialize jsons
    election = Election.from_dict(requests.get(ELECTION_BASE_URL + election_uuid).json())

    voters_json = requests.get(
        VOTERS_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()
    voters = [Voter.from_dict(voter_json) for voter_json in voters_json]

    ballots = []
    for voter in voters:
        ballot_url = BALLOTS_BASE_URL_WITH_ELECTION_AND_VOTER_PLACEHOLDERS \
            .replace('election_uuid', election_uuid) \
            .replace('voter_uuid', voter.uuid)
        cast_vote = CastVote.from_dict(requests.get(ballot_url).json())
        if cast_vote.vote is not None:
            ballots.append(cast_vote)

    results_json = requests.get(
        RESULTS_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()

    trustees_json = requests.get(
        TRUSTEES_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()
    trustees = [Trustee.from_dict(trustee_json) for trustee_json in trustees_json]

    # retally election
    retally_election(election, voters, results_json[0], ballots)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
