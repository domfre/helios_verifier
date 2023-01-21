import requests

from helios_verifier.domain.CastVote import CastVote
from helios_verifier.domain.Election import Election
from helios_verifier.domain.Trustee import Trustee
from helios_verifier.domain.VoteWithPlaintext import VoteWithPlaintext
from helios_verifier.domain.Voter import Voter
from helios_verifier.data.DataUrls import ELECTION_BASE_URL, VOTERS_BASE_URL_WITH_ELECTION_PLACEHOLDER, \
    BALLOTS_BASE_URL_WITH_ELECTION_AND_VOTER_PLACEHOLDERS, \
    RESULTS_BASE_URL_WITH_ELECTION_PLACEHOLDER, \
    TRUSTEES_BASE_URL_WITH_ELECTION_PLACEHOLDER, AUDITED_BALLOT_WITH_ELECTION_PLACEHOLDER


def retrieve_election_data(election_uuid):
    return Election.from_dict(requests.get(ELECTION_BASE_URL + election_uuid).json())


def retrieve_voters_data(election_uuid):
    voters_json = requests.get(
        VOTERS_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()
    return [Voter.from_dict(voter_json) for voter_json in voters_json]


def retrieve_ballots_data(election_uuid, voters):
    ballots = []
    for voter in voters:
        ballot_url = BALLOTS_BASE_URL_WITH_ELECTION_AND_VOTER_PLACEHOLDERS \
            .replace('election_uuid', election_uuid) \
            .replace('voter_uuid', voter.uuid)
        cast_vote = CastVote.from_dict(requests.get(ballot_url).json())
        if cast_vote.vote is not None:
            ballots.append(cast_vote)
    return ballots


def retrieve_results_data(election_uuid):
    results_json = requests.get(
        RESULTS_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()
    return results_json


def retrieve_trustees_data(election_uuid):
    trustees_json = requests.get(
        TRUSTEES_BASE_URL_WITH_ELECTION_PLACEHOLDER.replace('election_uuid', election_uuid)).json()
    return [Trustee.from_dict(tf) for tf in trustees_json]


def retrieve_audited_ballot_data(election_uuid, vote_hash):
    ballot_url = AUDITED_BALLOT_WITH_ELECTION_PLACEHOLDER\
        .replace('election_uuid', election_uuid)\
        .replace('vote_hash_placeholder', vote_hash)
    audited_ballot_json = requests.get(ballot_url).json()
    return VoteWithPlaintext.from_dict(audited_ballot_json)
