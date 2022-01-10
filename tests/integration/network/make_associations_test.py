# third party
import pytest

# syft absolute
import syft as sy

NETWORK_PORT = 9081
DOMAIN1_PORT = 9082
DOMAIN2_PORT = 9083


@pytest.mark.network
def test_domain1_association_network1() -> None:
    network_guest = sy.login(port=NETWORK_PORT)

    domain = sy.login(
        email="info@openmined.org", password="changethis", port=DOMAIN1_PORT
    )

    domain.apply_to_network(client=network_guest)

    network = sy.login(
        email="info@openmined.org", password="changethis", port=NETWORK_PORT
    )
    associations = network.association.all()
    for association in associations:
        if association["node_address"] == domain.target_id.id.no_dash:
            request_id = int(association["association_id"])

    network.association[request_id].accept()
    assert domain.association.all()[0]["status"] == "ACCEPTED"


@pytest.mark.network
def test_domain2_association_network1() -> None:
    network_guest = sy.login(port=NETWORK_PORT)

    domain = sy.login(
        email="info@openmined.org", password="changethis", port=DOMAIN2_PORT
    )

    domain.apply_to_network(client=network_guest)

    network = sy.login(
        email="info@openmined.org", password="changethis", port=NETWORK_PORT
    )
    associations = network.association.all()
    for association in associations:
        if association["node_address"] == domain.target_id.id.no_dash:
            request_id = int(association["association_id"])

    network.association[request_id].accept()
    assert domain.association.all()[0]["status"] == "ACCEPTED"