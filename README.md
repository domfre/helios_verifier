# Helios Verifier

This repository provides an application for a full verification of an election and its components conducted by the 
[Helios Voting System](https://vote.heliosvoting.org/)
or any equivalent voting system respecting the guidelines defined by the official 
[Helios v4 specs](https://documentation.heliosvoting.org/verification-specs/helios-v4) regarding the data formats 
and verification protocols. <br>

The [Helios v4 specs](https://documentation.heliosvoting.org/verification-specs/helios-v4) also provides the basis for 
the implementation of the core methods in this repository responsible for verifying 
the different components of an election.

***

## Usage
In order to run the verifier with the predefined configuration navigate into /helios_verifier (root of the project) and run
```
python3.10 -m helios_verifier.helios_verifier_app $election_uuid $vote_hash
```
Adjust the command for your python installation. <br>
If no election_uuid is passed, the verifier runs in default mode, verifying an example election. Same holds true for the vote_hash, <br>
which is the hash of an audited ballot to perform audited ballot verification.

***

## Remarks 

Currently, the verifier only works for elections hosted on the helios server. This can be easily changed by adjusting the host url <br>
in DataUrls module.