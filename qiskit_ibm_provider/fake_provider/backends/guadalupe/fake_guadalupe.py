# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Fake Guadalupe device (5 qubit).
"""

import os

from qiskit_ibm_provider.fake_provider import fake_pulse_backend, fake_backend


class FakeGuadalupeV2(fake_backend.FakeBackendV2):
    """A fake 16 qubit backend."""

    dirname = os.path.dirname(__file__)  # type: ignore
    conf_filename = "conf_guadalupe.json"  # type: ignore
    props_filename = "props_guadalupe.json"  # type: ignore
    defs_filename = "defs_guadalupe.json"  # type: ignore
    backend_name = "fake_guadalupe"  # type: ignore


class FakeGuadalupe(fake_pulse_backend.FakePulseBackend):
    """A fake 16 qubit backend."""

    dirname = os.path.dirname(__file__)  # type: ignore
    conf_filename = "conf_guadalupe.json"  # type: ignore
    props_filename = "props_guadalupe.json"  # type: ignore
    defs_filename = "defs_guadalupe.json"  # type: ignore
    backend_name = "fake_guadalupe"  # type: ignore
