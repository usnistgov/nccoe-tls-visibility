import argparse
from pyasn1.codec.der import decoder, encoder
from pyasn1.type import univ, useful, namedtype,tag,namedval,constraint
from pyasn1_modules import pem, rfc5915, rfc5958, rfc5652, rfc7906,rfc5280,rfc5480,rfc2459
import base64
from datetime import datetime
class KeyValidityPeriod(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('doNotUseBefore', univ.Integer()),
        namedtype.NamedType('doNotUseAfter', univ.Integer())
    )
class OneAsymmetricKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', rfc5958.Version()),
        namedtype.NamedType('privateKeyAlgorithm', rfc5958.PrivateKeyAlgorithmIdentifier()),
        namedtype.NamedType('privateKey', rfc5958.PrivateKey()),
        namedtype.OptionalNamedType('attributes', rfc5958.Attributes().subtype(
            implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))),
        namedtype.NamedType('publicKey', rfc5958.PublicKey())
    )
def convertTime(utc_time):
    utc_time_format = '%y%m%d%H%M%SZ'
    utc_time = datetime.strptime(utc_time, utc_time_format)
    timestamp = int(utc_time.timestamp())
    return timestamp
def AsymmetricKeyPackage(key_filename):
    asn1Spec = rfc5915.ECPrivateKey()
    with open(key_filename, 'r') as f:
        idx, substrate = pem.readPemBlocksFromFile(f, ('-----BEGIN EC PRIVATE KEY-----', '-----END EC PRIVATE KEY-----'))
    key_data, rest = decoder.decode(substrate, asn1Spec=asn1Spec)
    if rest:
        raise Exception('Input was not completely consumed')
    curve_oid = key_data["parameters"]["namedCurve"]
    validities = key_filename.split('-')
    validFrom = validities[1].replace('iu','')
    validTo = validities[2].replace('.pem','').replace('eu','')
    key_validity_period = KeyValidityPeriod()
    key_validity_period['doNotUseBefore'] = validFrom
    key_validity_period['doNotUseAfter'] = validTo
    attr = rfc5652.Attribute()
    attr['attrType'] = rfc7906.id_kma_keyValidityPeriod
    attr['attrValues'][0] = key_validity_period
    curve_name_oid = univ.ObjectIdentifier(curve_oid)
    one_asymmetric_key = OneAsymmetricKey()
    one_asymmetric_key['version'] = univ.Integer(1)
    one_asymmetric_key['privateKeyAlgorithm']['algorithm'] = rfc5480.id_ecDH
    one_asymmetric_key['privateKeyAlgorithm']['parameters'] = curve_name_oid
    one_asymmetric_key['privateKey'] = key_data['privateKey']
    one_asymmetric_key['publicKey'] = key_data['publicKey']
    one_asymmetric_key['attributes'][0] = attr
    package = rfc5958.AsymmetricKeyPackage()
    package.append(one_asymmetric_key)
    package_substrate = encoder.encode(package)
    return package_substrate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key-filename', dest='key_filename', required=True, help='File containing private key in PEM format')
    parser.add_argument('-d', '--der-filename', dest='der_filename', required=True, help='File for Asymmetric Key Package output in DER format')
    args = parser.parse_args()
    package = AsymmetricKeyPackage(args.key_filename)
    with open(args.der_filename, 'wb') as output:
        output.write(package)
