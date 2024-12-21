from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Optional, Tuple, Union


def generate_selfsigned_cert(
    hostname: str,
    public_ip: "Optional[Union[IPv4Address, IPv4Network, IPv6Address, IPv6Network]]" = None,
    private_ip: "Optional[Union[IPv4Address, IPv4Network, IPv6Address, IPv6Network]]" = None,
) -> "Tuple[bytes, bytes]":
    """
    Generate a self-signed X509 certificate.
    :param hostname:  Must provide a hostname
    :param public_ip:  Can optionally provide a public IP
    :param private_ip:  Can optionally provide a private IP
    :return: A tuple of the certificate PEM and the key PEM
    """

    # Generate our key
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, hostname)])

    # Setup our alt names.
    alt_names_list = [
        # Best practice seem to be to include the hostname in the SAN, which *SHOULD* mean COMMON_NAME is ignored.
        x509.DNSName(hostname)
    ]

    # Allow addressing by IP, for when you don't have real DNS (common in most testing scenarios)
    if public_ip is not None:
        # openssl wants DNSnames for ips...
        alt_names_list.append(x509.DNSName(public_ip))
        # ... whereas golang's crypto/tls is stricter, and needs IPAddresses
        alt_names_list.append(x509.IPAddress(public_ip))
    if private_ip is not None:
        # openssl wants DNSnames for ips...
        alt_names_list.append(x509.DNSName(private_ip))
        # ... whereas golang's crypto/tls is stricter, and needs IPAddresses
        alt_names_list.append(x509.IPAddress(private_ip))

    alt_names = x509.SubjectAlternativeName(alt_names_list)

    # path_len=0 means this cert can only sign itself, not other certs.
    basic_contraints = x509.BasicConstraints(ca=True, path_length=0)

    now = datetime.utcnow()
    print(now)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(1000)
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=10 * 365))
        .add_extension(basic_contraints, False)
        .add_extension(alt_names, False)
        .sign(key, hashes.SHA256(), default_backend())
    )

    print(cert)

    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

    print(cert_pem)
    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    print(key_pem)

    return cert_pem, key_pem

generate_selfsigned_cert("google.com")