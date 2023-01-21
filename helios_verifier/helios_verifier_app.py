from helios_verifier.data.DataRetriever import retrieve_election_data, retrieve_audited_ballot_data
from helios_verifier.data.DataRetriever import retrieve_voters_data
from helios_verifier.data.DataRetriever import retrieve_trustees_data
from helios_verifier.data.DataRetriever import retrieve_results_data
from helios_verifier.data.DataRetriever import retrieve_ballots_data
from helios_verifier.verifiers.ElectionVerifier import retally_election
from helios_verifier.verifiers.BallotVerifier import verify_ballot_audit

import sys


def verify_election(election_uuid):
    print(f'###################################################################################################\n')
    print(f'Start verifying election {election_uuid}\n')
    print(f'###################################################################################################\n')

    # retrieve all necessary data from the election source server
    print(f'Loading necessary data for verifying election from the server...')

    election = retrieve_election_data(election_uuid)
    voters = retrieve_voters_data(election_uuid)
    ballots = retrieve_ballots_data(election_uuid, voters)
    results = retrieve_results_data(election_uuid)
    trustees = retrieve_trustees_data(election_uuid)

    print(f'Successfully received all necessary data for:')
    print(f'    - Election \'{election.name}\' with...')
    print(f'            ...{len(voters)} voters')
    print(f'            ...{len(ballots)} ballots')
    print(f'            ...{len(trustees)} trustees')
    print(f'            ...and results {results}\n')

    # verify election
    print(f'Start of verification process for election {election_uuid}')
    success = retally_election(election, voters, results, ballots, trustees)
    if success:
        print(f'Successfully finished verification process for election {election_uuid}')
    else:
        print(f'Verification process for election {election_uuid} failed')
    print(f'\n\n')


def verify_audited_ballot(election_uuid, vote_hash):
    print(f'###################################################################################################\n')
    print(f'Start verifying audited ballot {vote_hash} from election {election_uuid}\n')
    print(f'###################################################################################################\n')

    # retrieve all necessary data from the election source server
    print(f'Loading necessary data for verifying audited ballot from server...')

    audited_ballot = retrieve_audited_ballot_data(election_uuid, vote_hash)
    election = retrieve_election_data(election_uuid)

    print(f'Successfully received all necessary data for:')
    print(f'    - Ballot {vote_hash}')
    print(f'    - Election \'{election.name}\'\n')

    # verify the audited ballot
    print(f'Start of verification process for ballot {vote_hash}')
    success = verify_ballot_audit(audited_ballot, election)
    if success:
        print(f'Successfully finished verification process for ballot {vote_hash}')
    else:
        print(f'Verification process for ballot {vote_hash} failed')
    print(f'\n\n')


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print(f'WARNING: election_uuid missing, running in default mode')
        verify_election('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9')
    else:
        verify_election(args[1])

    if len(args) < 3:
        print(f'WARNING: Either election_uuid or vote_hash missing or both, running in default mode')
        verify_audited_ballot('d020e5ca-69b5-11ed-ab96-0ea78f2ee8c9', '3RI3O1oDWOr1EeLKTm3r5WWm2knnpwLWXMuhFKavR50')
    else:
        verify_audited_ballot(args[1], args[2])
