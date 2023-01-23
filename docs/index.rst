.. HeliosVerifier documentation master file, created by
   sphinx-quickstart on Sat Jan 21 11:55:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to HeliosVerifier's documentation!
==========================================

This repository provides an application for a full verification of an election and its components conducted by the
`Helios Voting System <https://vote.heliosvoting.org/>`_
or any equivalent voting system respecting the guidelines defined by the official
`Helios v4 specs <https://documentation.heliosvoting.org/verification-specs/helios-v4/>`_ regarding the data formats
and verification protocols.
The implementation of the core methods in this repository responsible for verifying the different components
of an election is based on and inspired by the `Helios v4 specs <https://documentation.heliosvoting.org/verification-specs/helios-v4/>`_

Source available on https://github.com/domfre/helios_verifier.


.. toctree::
   :maxdepth: 2
   :caption: Verifiers

   verifiers/ProofVerifier
   verifiers/VoteVerifier
   verifiers/ElectionVerifier
   verifiers/BallotVerifier
   verifiers/DecryptionFactorVerifier


.. toctree::
   :maxdepth: 2
   :caption: Data

   data/DataRetriever



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
