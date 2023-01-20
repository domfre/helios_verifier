Welcome to helios_verifier's documentation!
===========================================

This repository provides an application for a full verification of an election and its components conducted by the
`Helios Voting System <https://vote.heliosvoting.org/>`_
or any equivalent voting system respecting the guidelines defined by the official
`Helios v4 specs <https://documentation.heliosvoting.org/verification-specs/helios-v4/>`_ regarding the data formats
and verification protocols.
The implementation of the core methods in this repository responsible for verifying the different components
of an election is based on and inspired by the `Helios v4 specs <https://documentation.heliosvoting.org/verification-specs/helios-v4/>`_

Source available on https://github.com/domfre/helios_verifier.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Verifiers

   verifiers/ProofVerifier
   verifiers/VoteVerifier
   verifiers/ElectionVerifier
   verifiers/BallotVerifier

.. toctree::
   :maxdepth: 2
   :caption: Data

   data/DataReceiver

