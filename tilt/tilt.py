# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = tilt_from_dict(json.loads(json_string))

from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class AdministrativeFee:
    """The fee that refers to several copies."""
    """The amount of money to be paid for a copy."""
    amount: float
    """The currency in which the amount of money for one copy has to be provided acc. to ISO
    4217.
    """
    currency: str

    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    @staticmethod
    def from_dict(obj: Any) -> 'AdministrativeFee':
        assert isinstance(obj, dict)
        amount = from_float(obj.get("amount"))
        currency = from_str(obj.get("currency"))
        return AdministrativeFee(amount, currency)

    def to_dict(self) -> dict:
        result: dict = {}
        result["amount"] = to_float(self.amount)
        result["currency"] = from_str(self.currency)
        return result


class AccessAndDataPortability:
    """Defining the right to access and data portability."""
    """The fee that refers to several copies."""
    administrative_fee: Optional[AdministrativeFee]
    """The information is subject to the requirements of Art. 20 (right to data portability)
    GDPR.
    """
    available: bool
    """An explanation about the data format(s) the data is provided in."""
    data_formats: Optional[List[str]]
    """Description of the requirements according to Art. 20 GDPR."""
    description: Optional[str]
    """Contact email address"""
    email: Optional[str]
    """ID evidences"""
    identification_evidences: Optional[List[str]]
    """URL to relevant resources such as access portals."""
    url: Optional[str]

    def __init__(self, administrative_fee: Optional[AdministrativeFee], available: bool, data_formats: Optional[List[str]], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], url: Optional[str]) -> None:
        self.administrative_fee = administrative_fee
        self.available = available
        self.data_formats = data_formats
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'AccessAndDataPortability':
        assert isinstance(obj, dict)
        administrative_fee = from_union([AdministrativeFee.from_dict, from_none], obj.get("administrativeFee"))
        available = from_bool(obj.get("available"))
        data_formats = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dataFormats"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        url = from_union([from_str, from_none], obj.get("url"))
        return AccessAndDataPortability(administrative_fee, available, data_formats, description, email, identification_evidences, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["administrativeFee"] = from_union([lambda x: to_class(AdministrativeFee, x), from_none], self.administrative_fee)
        result["available"] = from_bool(self.available)
        result["dataFormats"] = from_union([lambda x: from_list(from_str, x), from_none], self.data_formats)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class AutomatedDecisionMaking:
    """Automated decision making and potentially involved logic. Does include profiling."""
    """Is automated decision making in use?"""
    in_use: Optional[bool]
    """An explanation about the logic involved to automated decision making."""
    logic_involved: Optional[str]
    """Scope and intended effects of such processing for the data subject."""
    scope_and_intended_effects: Optional[str]

    def __init__(self, in_use: Optional[bool], logic_involved: Optional[str], scope_and_intended_effects: Optional[str]) -> None:
        self.in_use = in_use
        self.logic_involved = logic_involved
        self.scope_and_intended_effects = scope_and_intended_effects

    @staticmethod
    def from_dict(obj: Any) -> 'AutomatedDecisionMaking':
        assert isinstance(obj, dict)
        in_use = from_union([from_bool, from_none], obj.get("inUse"))
        logic_involved = from_union([from_str, from_none], obj.get("logicInvolved"))
        scope_and_intended_effects = from_union([from_str, from_none], obj.get("scopeAndIntendedEffects"))
        return AutomatedDecisionMaking(in_use, logic_involved, scope_and_intended_effects)

    def to_dict(self) -> dict:
        result: dict = {}
        result["inUse"] = from_union([from_bool, from_none], self.in_use)
        result["logicInvolved"] = from_union([from_str, from_none], self.logic_involved)
        result["scopeAndIntendedEffects"] = from_union([from_str, from_none], self.scope_and_intended_effects)
        return result


class ChangesOfPurposeElement:
    """Data categories that are affected from the change of purpose."""
    affected_data_categories: Optional[List[str]]
    """Description of the change of purpose."""
    description: Optional[str]
    """Specify the planned date to the changes as ISO 8601 string."""
    planned_date_of_change: Optional[str]
    """URL points to a document of the same as this one. That creates a chain of information
    requirements for seamless recognition of transparency information even over a longer
    period of time.
    """
    url_of_new_version: Optional[str]

    def __init__(self, affected_data_categories: Optional[List[str]], description: Optional[str], planned_date_of_change: Optional[str], url_of_new_version: Optional[str]) -> None:
        self.affected_data_categories = affected_data_categories
        self.description = description
        self.planned_date_of_change = planned_date_of_change
        self.url_of_new_version = url_of_new_version

    @staticmethod
    def from_dict(obj: Any) -> 'ChangesOfPurposeElement':
        assert isinstance(obj, dict)
        affected_data_categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("affectedDataCategories"))
        description = from_union([from_str, from_none], obj.get("description"))
        planned_date_of_change = from_union([from_str, from_none], obj.get("plannedDateOfChange"))
        url_of_new_version = from_union([from_str, from_none], obj.get("urlOfNewVersion"))
        return ChangesOfPurposeElement(affected_data_categories, description, planned_date_of_change, url_of_new_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["affectedDataCategories"] = from_union([lambda x: from_list(from_str, x), from_none], self.affected_data_categories)
        result["description"] = from_union([from_str, from_none], self.description)
        result["plannedDateOfChange"] = from_union([from_str, from_none], self.planned_date_of_change)
        result["urlOfNewVersion"] = from_union([from_str, from_none], self.url_of_new_version)
        return result


class ControllerRepresentative:
    """The representative is a responsible real person that represents the controller."""
    """Email address of the controller's representative."""
    email: str
    """Name of the controller's representative."""
    name: str
    """Phone number of the controller's representative."""
    phone: Optional[str]

    def __init__(self, email: str, name: str, phone: Optional[str]) -> None:
        self.email = email
        self.name = name
        self.phone = phone

    @staticmethod
    def from_dict(obj: Any) -> 'ControllerRepresentative':
        assert isinstance(obj, dict)
        email = from_str(obj.get("email"))
        name = from_str(obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        return ControllerRepresentative(email, name, phone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_str(self.email)
        result["name"] = from_str(self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        return result


class Controller:
    """The responsible controller is defined in here."""
    """Address of the controller."""
    address: str
    """All country codes follow the established ones ISO 3166 country abbreviation standard."""
    country: str
    """Serves to differentiate between different areas of a company; particularly relevant for
    large companies.
    """
    division: Optional[str]
    """Name of the controller."""
    name: str
    """The representative is a responsible real person that represents the controller."""
    representative: ControllerRepresentative

    def __init__(self, address: str, country: str, division: Optional[str], name: str, representative: ControllerRepresentative) -> None:
        self.address = address
        self.country = country
        self.division = division
        self.name = name
        self.representative = representative

    @staticmethod
    def from_dict(obj: Any) -> 'Controller':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        country = from_str(obj.get("country"))
        division = from_union([from_str, from_none], obj.get("division"))
        name = from_str(obj.get("name"))
        representative = ControllerRepresentative.from_dict(obj.get("representative"))
        return Controller(address, country, division, name, representative)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["country"] = from_str(self.country)
        result["division"] = from_union([from_str, from_none], self.division)
        result["name"] = from_str(self.name)
        result["representative"] = to_class(ControllerRepresentative, self.representative)
        return result


class AnyOfSchemaForTheLegalBasesOfTheDataDisclosed:
    """An explanation about the legal basis used."""
    description: Optional[str]
    """This field refers to the reference in legal regulations (laws, orders, declaration etc.).
    The format is set to uppercase letters for the legal text followed by hyphened numbers
    and lowercase letters for the exact location.
    """
    reference: str

    def __init__(self, description: Optional[str], reference: str) -> None:
        self.description = description
        self.reference = reference

    @staticmethod
    def from_dict(obj: Any) -> 'AnyOfSchemaForTheLegalBasesOfTheDataDisclosed':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        reference = from_str(obj.get("reference"))
        return AnyOfSchemaForTheLegalBasesOfTheDataDisclosed(description, reference)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_union([from_str, from_none], self.description)
        result["reference"] = from_str(self.reference)
        return result


class AnyOfSchemaForLegitimateInterests:
    """The legitimate interest only has to be stated if the processing is carried out in
    accordance with Art. 13 (1d). This field refers to the existence of such an interest.
    """
    exists: Optional[bool]
    """If the legitimate interest has to be stated because the processing is carried out in
    accordance with Art. 13 (1d), it is described in here.
    """
    reasoning: Optional[str]

    def __init__(self, exists: Optional[bool], reasoning: Optional[str]) -> None:
        self.exists = exists
        self.reasoning = reasoning

    @staticmethod
    def from_dict(obj: Any) -> 'AnyOfSchemaForLegitimateInterests':
        assert isinstance(obj, dict)
        exists = from_union([from_bool, from_none], obj.get("exists"))
        reasoning = from_union([from_str, from_none], obj.get("reasoning"))
        return AnyOfSchemaForLegitimateInterests(exists, reasoning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exists"] = from_union([from_bool, from_none], self.exists)
        result["reasoning"] = from_union([from_str, from_none], self.reasoning)
        return result


class NonDisclosure:
    """This schema refers to the necessity and consequences of non-disclosure of personal data.
    According to Art. 13 (2e), this refers to the information whether the provision of the
    personal data is required by law or contract or is required for the conclusion of a
    contract, whether the data subject is obliged to provide the personal data and the
    possible consequences of not providing it.
    """
    """Description of the consequences in the case of non-disclosure."""
    consequences: str
    """Is there a contractual regulation to collect these data?"""
    contractual_regulation: bool
    """Is there a legal requirement to collect these data?"""
    legal_requirement: bool
    """Is there an obligation for the data subject to provide these data?"""
    obligation_to_provide: bool

    def __init__(self, consequences: str, contractual_regulation: bool, legal_requirement: bool, obligation_to_provide: bool) -> None:
        self.consequences = consequences
        self.contractual_regulation = contractual_regulation
        self.legal_requirement = legal_requirement
        self.obligation_to_provide = obligation_to_provide

    @staticmethod
    def from_dict(obj: Any) -> 'NonDisclosure':
        assert isinstance(obj, dict)
        consequences = from_str(obj.get("consequences"))
        contractual_regulation = from_bool(obj.get("contractualRegulation"))
        legal_requirement = from_bool(obj.get("legalRequirement"))
        obligation_to_provide = from_bool(obj.get("obligationToProvide"))
        return NonDisclosure(consequences, contractual_regulation, legal_requirement, obligation_to_provide)

    def to_dict(self) -> dict:
        result: dict = {}
        result["consequences"] = from_str(self.consequences)
        result["contractualRegulation"] = from_bool(self.contractual_regulation)
        result["legalRequirement"] = from_bool(self.legal_requirement)
        result["obligationToProvide"] = from_bool(self.obligation_to_provide)
        return result


class AnyOfSchemaForThePurposes:
    """This schema refers to an exact description of the purpose the data is processed for."""
    description: str
    """In this schema the purpose is specified (i.e. a headline or purpose category)."""
    purpose: str

    def __init__(self, description: str, purpose: str) -> None:
        self.description = description
        self.purpose = purpose

    @staticmethod
    def from_dict(obj: Any) -> 'AnyOfSchemaForThePurposes':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        purpose = from_str(obj.get("purpose"))
        return AnyOfSchemaForThePurposes(description, purpose)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["purpose"] = from_str(self.purpose)
        return result


class RecipientRepresentative:
    """The representative of the third party (recipient)."""
    """The email address of the representative of the third party (recipient)."""
    email: Optional[str]
    """The name of the representative of the third party (recipient)."""
    name: Optional[str]
    """The phone number of the representative of the third party (recipient)."""
    phone: Optional[str]

    def __init__(self, email: Optional[str], name: Optional[str], phone: Optional[str]) -> None:
        self.email = email
        self.name = name
        self.phone = phone

    @staticmethod
    def from_dict(obj: Any) -> 'RecipientRepresentative':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        name = from_union([from_str, from_none], obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        return RecipientRepresentative(email, name, phone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_union([from_str, from_none], self.email)
        result["name"] = from_union([from_str, from_none], self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        return result


class Recipient:
    """The address of the third party (recipient)."""
    address: Optional[str]
    """The category of the the recipient.
    
    This category has to be given, even if the controller is not mentioned explicitly.
    """
    category: str
    """The country in which the recipient is located at. Attention: This explictly specifies
    third country transfers!
    """
    country: Optional[str]
    """The division of the third party (recipient) for structuring controllers into smaller
    entities.
    """
    division: Optional[str]
    """The name of the third party (recipient)."""
    name: Optional[str]
    """The representative of the third party (recipient)."""
    representative: Optional[RecipientRepresentative]

    def __init__(self, address: Optional[str], category: str, country: Optional[str], division: Optional[str], name: Optional[str], representative: Optional[RecipientRepresentative]) -> None:
        self.address = address
        self.category = category
        self.country = country
        self.division = division
        self.name = name
        self.representative = representative

    @staticmethod
    def from_dict(obj: Any) -> 'Recipient':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("address"))
        category = from_str(obj.get("category"))
        country = from_union([from_str, from_none], obj.get("country"))
        division = from_union([from_str, from_none], obj.get("division"))
        name = from_union([from_str, from_none], obj.get("name"))
        representative = from_union([RecipientRepresentative.from_dict, from_none], obj.get("representative"))
        return Recipient(address, category, country, division, name, representative)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([from_str, from_none], self.address)
        result["category"] = from_str(self.category)
        result["country"] = from_union([from_str, from_none], self.country)
        result["division"] = from_union([from_str, from_none], self.division)
        result["name"] = from_union([from_str, from_none], self.name)
        result["representative"] = from_union([lambda x: to_class(RecipientRepresentative, x), from_none], self.representative)
        return result


class AggregationFunction(Enum):
    """The aggregation function describes the calculation basis when specifying several time
    intervals. For example, if there is storage for 2 weeks for technical reasons (e.g.
    backup), but there is a legally longer retention period, the maximum aggregation function
    (max) would be selected (standard case). Aggregation functions available: min, max, sum,
    avg
    """
    AVG = "avg"
    MAX = "max"
    MIN = "min"
    SUM = "sum"


class TemporalElement:
    """The description why the data has to be stored.."""
    description: str
    """The TTL (Time-to-Live) specifies the lifetime of this data (category). It follows the ISO
    8601 for time spans.
    """
    ttl: str

    def __init__(self, description: str, ttl: str) -> None:
        self.description = description
        self.ttl = ttl

    @staticmethod
    def from_dict(obj: Any) -> 'TemporalElement':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        ttl = from_str(obj.get("ttl"))
        return TemporalElement(description, ttl)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["ttl"] = from_str(self.ttl)
        return result


class StorageElement:
    """The aggregation function describes the calculation basis when specifying several time
    intervals. For example, if there is storage for 2 weeks for technical reasons (e.g.
    backup), but there is a legally longer retention period, the maximum aggregation function
    (max) would be selected (standard case). Aggregation functions available: min, max, sum,
    avg
    """
    aggregation_function: AggregationFunction
    """If the storage is required by law, the respective one has to specified in here."""
    legal_basis_conditional: List[str]
    """Specifies the purpose that requires data storage."""
    purpose_conditional: List[str]
    """This schema serves to specify a temporal description of how long the data is stored and
    for what exactly.
    """
    temporal: List[TemporalElement]

    def __init__(self, aggregation_function: AggregationFunction, legal_basis_conditional: List[str], purpose_conditional: List[str], temporal: List[TemporalElement]) -> None:
        self.aggregation_function = aggregation_function
        self.legal_basis_conditional = legal_basis_conditional
        self.purpose_conditional = purpose_conditional
        self.temporal = temporal

    @staticmethod
    def from_dict(obj: Any) -> 'StorageElement':
        assert isinstance(obj, dict)
        aggregation_function = AggregationFunction(obj.get("aggregationFunction"))
        legal_basis_conditional = from_list(from_str, obj.get("legalBasisConditional"))
        purpose_conditional = from_list(from_str, obj.get("purposeConditional"))
        temporal = from_list(TemporalElement.from_dict, obj.get("temporal"))
        return StorageElement(aggregation_function, legal_basis_conditional, purpose_conditional, temporal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["aggregationFunction"] = to_enum(AggregationFunction, self.aggregation_function)
        result["legalBasisConditional"] = from_list(from_str, self.legal_basis_conditional)
        result["purposeConditional"] = from_list(from_str, self.purpose_conditional)
        result["temporal"] = from_list(lambda x: to_class(TemporalElement, x), self.temporal)
        return result


class DataDisclosedElement:
    """The description of data disclosed."""
    """The id of a data item that is disclosed. The id is necessary to distinguish several
    processing tasks of the same data item (locally unique ID that can be based on the
    database implementation).
    """
    id: str
    """The data (category) the data disclosed is referred to."""
    category: str
    """An explanation about the legal bases for the processing of personal data disclosed."""
    legal_bases: List[AnyOfSchemaForTheLegalBasesOfTheDataDisclosed]
    """An explanation about the legitimate interests for the processing of data disclosed."""
    legitimate_interests: List[AnyOfSchemaForLegitimateInterests]
    """This schema refers to the necessity and consequences of non-disclosure of personal data.
    According to Art. 13 (2e), this refers to the information whether the provision of the
    personal data is required by law or contract or is required for the conclusion of a
    contract, whether the data subject is obliged to provide the personal data and the
    possible consequences of not providing it.
    """
    non_disclosure: NonDisclosure
    """The purpose for which a data item is processed for."""
    purposes: List[AnyOfSchemaForThePurposes]
    """An explanation about the recipients of the data disclosed."""
    recipients: List[Recipient]
    """In this section, the duration of storage or storage criteria are given."""
    storage: List[StorageElement]

    def __init__(self, id: str, category: str, legal_bases: List[AnyOfSchemaForTheLegalBasesOfTheDataDisclosed], legitimate_interests: List[AnyOfSchemaForLegitimateInterests], non_disclosure: NonDisclosure, purposes: List[AnyOfSchemaForThePurposes], recipients: List[Recipient], storage: List[StorageElement]) -> None:
        self.id = id
        self.category = category
        self.legal_bases = legal_bases
        self.legitimate_interests = legitimate_interests
        self.non_disclosure = non_disclosure
        self.purposes = purposes
        self.recipients = recipients
        self.storage = storage

    @staticmethod
    def from_dict(obj: Any) -> 'DataDisclosedElement':
        assert isinstance(obj, dict)
        id = from_str(obj.get("_id"))
        category = from_str(obj.get("category"))
        legal_bases = from_list(AnyOfSchemaForTheLegalBasesOfTheDataDisclosed.from_dict, obj.get("legalBases"))
        legitimate_interests = from_list(AnyOfSchemaForLegitimateInterests.from_dict, obj.get("legitimateInterests"))
        non_disclosure = NonDisclosure.from_dict(obj.get("nonDisclosure"))
        purposes = from_list(AnyOfSchemaForThePurposes.from_dict, obj.get("purposes"))
        recipients = from_list(Recipient.from_dict, obj.get("recipients"))
        storage = from_list(StorageElement.from_dict, obj.get("storage"))
        return DataDisclosedElement(id, category, legal_bases, legitimate_interests, non_disclosure, purposes, recipients, storage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_str(self.id)
        result["category"] = from_str(self.category)
        result["legalBases"] = from_list(lambda x: to_class(AnyOfSchemaForTheLegalBasesOfTheDataDisclosed, x), self.legal_bases)
        result["legitimateInterests"] = from_list(lambda x: to_class(AnyOfSchemaForLegitimateInterests, x), self.legitimate_interests)
        result["nonDisclosure"] = to_class(NonDisclosure, self.non_disclosure)
        result["purposes"] = from_list(lambda x: to_class(AnyOfSchemaForThePurposes, x), self.purposes)
        result["recipients"] = from_list(lambda x: to_class(Recipient, x), self.recipients)
        result["storage"] = from_list(lambda x: to_class(StorageElement, x), self.storage)
        return result


class DataProtectionOfficer:
    """The Data Protection Officer (DPO) of the controller."""
    """Address of the DPO."""
    address: str
    """The country in which the Data Protection officer is located at."""
    country: str
    """The contact email address of the Data Protection Officer."""
    email: str
    """The full name of the Data Protection Officer."""
    name: str
    """The phone number of the Data Protection Officer (may include country prefix)."""
    phone: Optional[str]

    def __init__(self, address: str, country: str, email: str, name: str, phone: Optional[str]) -> None:
        self.address = address
        self.country = country
        self.email = email
        self.name = name
        self.phone = phone

    @staticmethod
    def from_dict(obj: Any) -> 'DataProtectionOfficer':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        country = from_str(obj.get("country"))
        email = from_str(obj.get("email"))
        name = from_str(obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        return DataProtectionOfficer(address, country, email, name, phone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["country"] = from_str(self.country)
        result["email"] = from_str(self.email)
        result["name"] = from_str(self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        return result


class Meta:
    """Meta information for the identification and verification of the document."""
    """The hash is based on one SHA256 calculation of the document."""
    hash: str
    """The ID follows the database-specific implementation and does not have to be set in
    advance; but should offer as much entropy as possible for globally unique identifiers.
    """
    id: str
    """Creation date of the document as an ISO-8601 time code."""
    created: str
    """All language abbreviation codes follow the established ISO 639-1 standard as identifiers
    for names of languages.
    """
    language: str
    """Last modified date of the document as an ISO-8601 time code."""
    modified: str
    """Name of the data controller."""
    name: str
    """The status of an instance can be active or inactive depending on the policy's legal force."""
    status: str
    """URL to this schema."""
    url: str
    """This number serves to version documents of a controller."""
    version: int

    def __init__(self, hash: str, id: str, created: str, language: str, modified: str, name: str, status: str, url: str, version: int) -> None:
        self.hash = hash
        self.id = id
        self.created = created
        self.language = language
        self.modified = modified
        self.name = name
        self.status = status
        self.url = url
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        hash = from_str(obj.get("_hash"))
        id = from_str(obj.get("_id"))
        created = from_str(obj.get("created"))
        language = from_str(obj.get("language"))
        modified = from_str(obj.get("modified"))
        name = from_str(obj.get("name"))
        status = from_str(obj.get("status"))
        url = from_str(obj.get("url"))
        version = from_int(obj.get("version"))
        return Meta(hash, id, created, language, modified, name, status, url, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_hash"] = from_str(self.hash)
        result["_id"] = from_str(self.id)
        result["created"] = from_str(self.created)
        result["language"] = from_str(self.language)
        result["modified"] = from_str(self.modified)
        result["name"] = from_str(self.name)
        result["status"] = from_str(self.status)
        result["url"] = from_str(self.url)
        result["version"] = from_int(self.version)
        return result


class SupervisoryAuthority:
    """Defines the supervisory authority that has to be contacted in order to complain about the
    data controller's practices.
    """
    """Adress of the supervisory authority."""
    address: Optional[str]
    """Country of the supervisory authority."""
    country: Optional[str]
    """Email adress of the supervisory authority."""
    email: Optional[str]
    """Name of the supervisory authority."""
    name: str
    """Phone number of the supervisory authority."""
    phone: Optional[str]

    def __init__(self, address: Optional[str], country: Optional[str], email: Optional[str], name: str, phone: Optional[str]) -> None:
        self.address = address
        self.country = country
        self.email = email
        self.name = name
        self.phone = phone

    @staticmethod
    def from_dict(obj: Any) -> 'SupervisoryAuthority':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("address"))
        country = from_union([from_str, from_none], obj.get("country"))
        email = from_union([from_str, from_none], obj.get("email"))
        name = from_str(obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        return SupervisoryAuthority(address, country, email, name, phone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([from_str, from_none], self.address)
        result["country"] = from_union([from_str, from_none], self.country)
        result["email"] = from_union([from_str, from_none], self.email)
        result["name"] = from_str(self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        return result


class RightToComplain:
    """This schema refers to the right to complain."""
    """Is this right available?"""
    available: Optional[bool]
    description: Optional[str]
    email: Optional[str]
    identification_evidences: Optional[List[str]]
    """Defines the supervisory authority that has to be contacted in order to complain about the
    data controller's practices.
    """
    supervisory_authority: Optional[SupervisoryAuthority]
    url: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], supervisory_authority: Optional[SupervisoryAuthority], url: Optional[str]) -> None:
        self.available = available
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.supervisory_authority = supervisory_authority
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RightToComplain':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        supervisory_authority = from_union([SupervisoryAuthority.from_dict, from_none], obj.get("supervisoryAuthority"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RightToComplain(available, description, email, identification_evidences, supervisory_authority, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["supervisoryAuthority"] = from_union([lambda x: to_class(SupervisoryAuthority, x), from_none], self.supervisory_authority)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class RightToDataPortability:
    """The right to data portability as stated in Art. 20 GDPR."""
    available: Optional[bool]
    description: Optional[str]
    email: Optional[str]
    identification_evidences: Optional[List[str]]
    url: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], url: Optional[str]) -> None:
        self.available = available
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RightToDataPortability':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RightToDataPortability(available, description, email, identification_evidences, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class RightToInformation:
    """Refers to the right of information."""
    """Possibility available?"""
    available: Optional[bool]
    """Description of the right."""
    description: Optional[str]
    email: Optional[str]
    identification_evidences: Optional[List[str]]
    """URL to an online portal."""
    url: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], url: Optional[str]) -> None:
        self.available = available
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RightToInformation':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RightToInformation(available, description, email, identification_evidences, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class RightToRectificationOrDeletion:
    """This schema refers to the right to rectification or deletion (Art. 16 GDPR)."""
    """Possibility available?"""
    available: Optional[bool]
    description: Optional[str]
    email: Optional[str]
    identification_evidences: Optional[List[str]]
    url: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], url: Optional[str]) -> None:
        self.available = available
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RightToRectificationOrDeletion':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RightToRectificationOrDeletion(available, description, email, identification_evidences, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class RightToWithdrawConsent:
    """This schema refers to the right to withdraw consent."""
    available: Optional[bool]
    description: Optional[str]
    email: Optional[str]
    identification_evidences: Optional[List[str]]
    url: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str], email: Optional[str], identification_evidences: Optional[List[str]], url: Optional[str]) -> None:
        self.available = available
        self.description = description
        self.email = email
        self.identification_evidences = identification_evidences
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'RightToWithdrawConsent':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        email = from_union([from_str, from_none], obj.get("email"))
        identification_evidences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("identificationEvidences"))
        url = from_union([from_str, from_none], obj.get("url"))
        return RightToWithdrawConsent(available, description, email, identification_evidences, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        result["email"] = from_union([from_str, from_none], self.email)
        result["identificationEvidences"] = from_union([lambda x: from_list(from_str, x), from_none], self.identification_evidences)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


class SourceSource:
    """Description of the source the data is taken from."""
    description: str
    """Are these data publicly available?"""
    publicly_available: bool
    """URL (reference) where the data is taken from."""
    url: str

    def __init__(self, description: str, publicly_available: bool, url: str) -> None:
        self.description = description
        self.publicly_available = publicly_available
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'SourceSource':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        publicly_available = from_bool(obj.get("publiclyAvailable"))
        url = from_str(obj.get("url"))
        return SourceSource(description, publicly_available, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["publiclyAvailable"] = from_bool(self.publicly_available)
        result["url"] = from_str(self.url)
        return result


class Source:
    """This refers to an locally unique ID in an arbitrary but deterministic format."""
    id: str
    """The category the data refer to."""
    data_category: str
    """Specify the source(s) where the data come from."""
    sources: List[SourceSource]

    def __init__(self, id: str, data_category: str, sources: List[SourceSource]) -> None:
        self.id = id
        self.data_category = data_category
        self.sources = sources

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        id = from_str(obj.get("_id"))
        data_category = from_str(obj.get("dataCategory"))
        sources = from_list(SourceSource.from_dict, obj.get("sources"))
        return Source(id, data_category, sources)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_str(self.id)
        result["dataCategory"] = from_str(self.data_category)
        result["sources"] = from_list(lambda x: to_class(SourceSource, x), self.sources)
        return result


class AdequacyDecision:
    """Adequacy decision by the European commission exists?"""
    available: Optional[bool]
    """Description of the adequacy decision by the European commission."""
    description: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str]) -> None:
        self.available = available
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'AdequacyDecision':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        return AdequacyDecision(available, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


class AppropriateGuarantees:
    """Suitable guarantees according to Art. 45"""
    """Do suitable guarantees according to Art. 45 exist?"""
    available: Optional[bool]
    """Description of suitable guarantees according to Art. 45"""
    description: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str]) -> None:
        self.available = available
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'AppropriateGuarantees':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        return AppropriateGuarantees(available, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


class PresenceOfEnforceableRightsAndEffectiveRemedies:
    """Presence of enforceable rights and effective remedies"""
    """Presence of enforceable rights and effective remedies?"""
    available: Optional[bool]
    """Description of enforceable rights and effective remedies."""
    description: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str]) -> None:
        self.available = available
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'PresenceOfEnforceableRightsAndEffectiveRemedies':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        return PresenceOfEnforceableRightsAndEffectiveRemedies(available, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


class StandardDataProtectionClause:
    """Schema on Standard Data Protection clauses."""
    """Does a standard data protection clause exist?"""
    available: Optional[bool]
    """An explanation about the standard data protection clause (may include link)."""
    description: Optional[str]

    def __init__(self, available: Optional[bool], description: Optional[str]) -> None:
        self.available = available
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'StandardDataProtectionClause':
        assert isinstance(obj, dict)
        available = from_union([from_bool, from_none], obj.get("available"))
        description = from_union([from_str, from_none], obj.get("description"))
        return StandardDataProtectionClause(available, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["available"] = from_union([from_bool, from_none], self.available)
        result["description"] = from_union([from_str, from_none], self.description)
        return result


class ThirdCountryTransferElement:
    adequacy_decision: Optional[AdequacyDecision]
    """Suitable guarantees according to Art. 45"""
    appropriate_guarantees: Optional[AppropriateGuarantees]
    """The country code of the third country."""
    country: Optional[str]
    """Presence of enforceable rights and effective remedies"""
    presence_of_enforceable_rights_and_effective_remedies: Optional[PresenceOfEnforceableRightsAndEffectiveRemedies]
    """Schema on Standard Data Protection clauses."""
    standard_data_protection_clause: Optional[StandardDataProtectionClause]

    def __init__(self, adequacy_decision: Optional[AdequacyDecision], appropriate_guarantees: Optional[AppropriateGuarantees], country: Optional[str], presence_of_enforceable_rights_and_effective_remedies: Optional[PresenceOfEnforceableRightsAndEffectiveRemedies], standard_data_protection_clause: Optional[StandardDataProtectionClause]) -> None:
        self.adequacy_decision = adequacy_decision
        self.appropriate_guarantees = appropriate_guarantees
        self.country = country
        self.presence_of_enforceable_rights_and_effective_remedies = presence_of_enforceable_rights_and_effective_remedies
        self.standard_data_protection_clause = standard_data_protection_clause

    @staticmethod
    def from_dict(obj: Any) -> 'ThirdCountryTransferElement':
        assert isinstance(obj, dict)
        adequacy_decision = from_union([AdequacyDecision.from_dict, from_none], obj.get("adequacyDecision"))
        appropriate_guarantees = from_union([AppropriateGuarantees.from_dict, from_none], obj.get("appropriateGuarantees"))
        country = from_union([from_str, from_none], obj.get("country"))
        presence_of_enforceable_rights_and_effective_remedies = from_union([PresenceOfEnforceableRightsAndEffectiveRemedies.from_dict, from_none], obj.get("presenceOfEnforceableRightsAndEffectiveRemedies"))
        standard_data_protection_clause = from_union([StandardDataProtectionClause.from_dict, from_none], obj.get("standardDataProtectionClause"))
        return ThirdCountryTransferElement(adequacy_decision, appropriate_guarantees, country, presence_of_enforceable_rights_and_effective_remedies, standard_data_protection_clause)

    def to_dict(self) -> dict:
        result: dict = {}
        result["adequacyDecision"] = from_union([lambda x: to_class(AdequacyDecision, x), from_none], self.adequacy_decision)
        result["appropriateGuarantees"] = from_union([lambda x: to_class(AppropriateGuarantees, x), from_none], self.appropriate_guarantees)
        result["country"] = from_union([from_str, from_none], self.country)
        result["presenceOfEnforceableRightsAndEffectiveRemedies"] = from_union([lambda x: to_class(PresenceOfEnforceableRightsAndEffectiveRemedies, x), from_none], self.presence_of_enforceable_rights_and_effective_remedies)
        result["standardDataProtectionClause"] = from_union([lambda x: to_class(StandardDataProtectionClause, x), from_none], self.standard_data_protection_clause)
        return result


class Tilt:
    """This schema defines the Transparency Information Language"""
    """Defining the right to access and data portability."""
    access_and_data_portability: AccessAndDataPortability
    """Automated decision making and potentially involved logic. Does include profiling."""
    automated_decision_making: AutomatedDecisionMaking
    """Notification of change of purpose."""
    changes_of_purpose: List[ChangesOfPurposeElement]
    """The responsible controller is defined in here."""
    controller: Controller
    """A detailed explanation about which data is disclosed in the processing tasks."""
    data_disclosed: List[DataDisclosedElement]
    """The Data Protection Officer (DPO) of the controller."""
    data_protection_officer: DataProtectionOfficer
    """Meta information for the identification and verification of the document."""
    meta: Meta
    """This schema refers to the right to complain."""
    right_to_complain: RightToComplain
    """The right to data portability as stated in Art. 20 GDPR."""
    right_to_data_portability: RightToDataPortability
    """Refers to the right of information."""
    right_to_information: RightToInformation
    """This schema refers to the right to rectification or deletion (Art. 16 GDPR)."""
    right_to_rectification_or_deletion: RightToRectificationOrDeletion
    """This schema refers to the right to withdraw consent."""
    right_to_withdraw_consent: RightToWithdrawConsent
    """This duty to provide information is limited to the collection of personal data that does
    not take place from the data subject (Art. 14).
    """
    sources: List[Source]
    """This schema refers to the adequacy decisions of any third country transfers."""
    third_country_transfers: List[ThirdCountryTransferElement]

    def __init__(self, access_and_data_portability: AccessAndDataPortability, automated_decision_making: AutomatedDecisionMaking, changes_of_purpose: List[ChangesOfPurposeElement], controller: Controller, data_disclosed: List[DataDisclosedElement], data_protection_officer: DataProtectionOfficer, meta: Meta, right_to_complain: RightToComplain, right_to_data_portability: RightToDataPortability, right_to_information: RightToInformation, right_to_rectification_or_deletion: RightToRectificationOrDeletion, right_to_withdraw_consent: RightToWithdrawConsent, sources: List[Source], third_country_transfers: List[ThirdCountryTransferElement]) -> None:
        self.access_and_data_portability = access_and_data_portability
        self.automated_decision_making = automated_decision_making
        self.changes_of_purpose = changes_of_purpose
        self.controller = controller
        self.data_disclosed = data_disclosed
        self.data_protection_officer = data_protection_officer
        self.meta = meta
        self.right_to_complain = right_to_complain
        self.right_to_data_portability = right_to_data_portability
        self.right_to_information = right_to_information
        self.right_to_rectification_or_deletion = right_to_rectification_or_deletion
        self.right_to_withdraw_consent = right_to_withdraw_consent
        self.sources = sources
        self.third_country_transfers = third_country_transfers

    @staticmethod
    def from_dict(obj: Any) -> 'Tilt':
        assert isinstance(obj, dict)
        access_and_data_portability = AccessAndDataPortability.from_dict(obj.get("accessAndDataPortability"))
        automated_decision_making = AutomatedDecisionMaking.from_dict(obj.get("automatedDecisionMaking"))
        changes_of_purpose = from_list(ChangesOfPurposeElement.from_dict, obj.get("changesOfPurpose"))
        controller = Controller.from_dict(obj.get("controller"))
        data_disclosed = from_list(DataDisclosedElement.from_dict, obj.get("dataDisclosed"))
        data_protection_officer = DataProtectionOfficer.from_dict(obj.get("dataProtectionOfficer"))
        meta = Meta.from_dict(obj.get("meta"))
        right_to_complain = RightToComplain.from_dict(obj.get("rightToComplain"))
        right_to_data_portability = RightToDataPortability.from_dict(obj.get("rightToDataPortability"))
        right_to_information = RightToInformation.from_dict(obj.get("rightToInformation"))
        right_to_rectification_or_deletion = RightToRectificationOrDeletion.from_dict(obj.get("rightToRectificationOrDeletion"))
        right_to_withdraw_consent = RightToWithdrawConsent.from_dict(obj.get("rightToWithdrawConsent"))
        sources = from_list(Source.from_dict, obj.get("sources"))
        third_country_transfers = from_list(ThirdCountryTransferElement.from_dict, obj.get("thirdCountryTransfers"))
        return Tilt(access_and_data_portability, automated_decision_making, changes_of_purpose, controller, data_disclosed, data_protection_officer, meta, right_to_complain, right_to_data_portability, right_to_information, right_to_rectification_or_deletion, right_to_withdraw_consent, sources, third_country_transfers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accessAndDataPortability"] = to_class(AccessAndDataPortability, self.access_and_data_portability)
        result["automatedDecisionMaking"] = to_class(AutomatedDecisionMaking, self.automated_decision_making)
        result["changesOfPurpose"] = from_list(lambda x: to_class(ChangesOfPurposeElement, x), self.changes_of_purpose)
        result["controller"] = to_class(Controller, self.controller)
        result["dataDisclosed"] = from_list(lambda x: to_class(DataDisclosedElement, x), self.data_disclosed)
        result["dataProtectionOfficer"] = to_class(DataProtectionOfficer, self.data_protection_officer)
        result["meta"] = to_class(Meta, self.meta)
        result["rightToComplain"] = to_class(RightToComplain, self.right_to_complain)
        result["rightToDataPortability"] = to_class(RightToDataPortability, self.right_to_data_portability)
        result["rightToInformation"] = to_class(RightToInformation, self.right_to_information)
        result["rightToRectificationOrDeletion"] = to_class(RightToRectificationOrDeletion, self.right_to_rectification_or_deletion)
        result["rightToWithdrawConsent"] = to_class(RightToWithdrawConsent, self.right_to_withdraw_consent)
        result["sources"] = from_list(lambda x: to_class(Source, x), self.sources)
        result["thirdCountryTransfers"] = from_list(lambda x: to_class(ThirdCountryTransferElement, x), self.third_country_transfers)
        return result


def tilt_from_dict(s: Any) -> Tilt:
    return Tilt.from_dict(s)


def tilt_to_dict(x: Tilt) -> Any:
    return to_class(Tilt, x)
