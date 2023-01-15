from helios_verifier.data.DataRetriever import retrieve_election_data, retrieve_audited_ballot_data
from helios_verifier.data.DataRetriever import retrieve_voters_data
from helios_verifier.data.DataRetriever import retrieve_trustees_data
from helios_verifier.data.DataRetriever import retrieve_results_data
from helios_verifier.data.DataRetriever import retrieve_ballots_data
from helios_verifier.verifiers.ElectionVerifier import retally_election
from helios_verifier.verifiers.BallotVerifier import verify_ballot_audit


def verify_election(election_uuid):
    # retrieve data from the election source server
    election = retrieve_election_data(election_uuid)
    voters = retrieve_voters_data(election_uuid)
    ballots = retrieve_ballots_data(election_uuid, voters)
    results = retrieve_results_data(election_uuid)
    trustees = retrieve_trustees_data(election_uuid)

    # retally election
    retally_election(election, voters, results, ballots, trustees)


def verify_audited_ballot(election_uuid, vote_hash):
    # verify an audited ballot
    audited_ballot = retrieve_audited_ballot_data(election_uuid, vote_hash)
    election = retrieve_election_data(election_uuid)
    verify_ballot_audit(audited_ballot, election)


if __name__ == '__main__':
    verify_election('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9')
    verify_audited_ballot('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9', '3RI3O1oDWOr1EeLKTm3r5WWm2knnpwLWXMuhFKavR50')
