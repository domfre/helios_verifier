from helios_verifier.DataRetriever import retrieve_election_data
from helios_verifier.DataRetriever import retrieve_voters_data
from helios_verifier.DataRetriever import retrieve_trustees_data
from helios_verifier.DataRetriever import retrieve_results_data
from helios_verifier.DataRetriever import retrieve_ballots_data
from helios_verifier.verifiers.ElectionVerifier import retally_election


def verify(election_uuid):

    # retrieve data from the election source server
    election = retrieve_election_data(election_uuid)
    voters = retrieve_voters_data(election_uuid)
    ballots = retrieve_ballots_data(election_uuid, voters)
    results = retrieve_results_data(election_uuid)
    trustees = retrieve_trustees_data(election_uuid)

    # retally election
    retally_election(election, voters, results, ballots)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
