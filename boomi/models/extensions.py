from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# Common field model (used in Connections, Operations, SharedCommunications, TradingPartners)
class ExtensionField(BaseModel):
    id: str
    value: Optional[str] = None
    encryptedValueSet: Optional[bool] = Field(default=None, alias="encryptedValueSet")
    usesEncryption: Optional[bool] = Field(default=None, alias="usesEncryption")
    componentOverride: Optional[bool] = Field(default=None, alias="componentOverride")
    useDefault: Optional[bool] = Field(default=None, alias="useDefault")
    
    class Config:
        allow_population_by_field_name = True

# For Connection.customProperties.properties
class CustomPropertyPair(BaseModel):
    key: str
    value: Optional[str] = None
    encrypted: Optional[bool] = None

class CustomProperties(BaseModel):
    properties: Optional[List[CustomPropertyPair]] = Field(default=None, alias="Property") # XML list <properties><Property>...</Property></properties>

    class Config:
        allow_population_by_field_name = True

# Model for Connection field, which can have customProperties
class ConnectionExtensionField(ExtensionField): # Inherits from ExtensionField
    customProperties: Optional[CustomProperties] = None # JSON/XML key is "customProperties"

    class Config:
        allow_population_by_field_name = True
        
# Model for a Connection
class ConnectionExtension(BaseModel):
    id: str
    name: Optional[str] = None 
    field: Optional[List[ConnectionExtensionField]] = Field(default=None, alias="Field") # XML list <field>...</field>

    class Config:
        allow_population_by_field_name = True

class ConnectionsList(BaseModel): # Container for <connections>
    connection: Optional[List[ConnectionExtension]] = Field(default=None, alias="Connection") # XML list <connection>...</connection>

    class Config:
        allow_population_by_field_name = True

# Model for Process Property Value (part of ProcessProperty)
class ProcessPropertyValueExtension(BaseModel):
    label: Optional[str] = None
    key: str
    value: Optional[str] = None
    encryptedValueSet: Optional[bool] = Field(default=None, alias="encryptedValueSet")
    useDefault: Optional[bool] = Field(default=None, alias="useDefault")

    class Config:
        allow_population_by_field_name = True

# Model for a Process Property
class ProcessPropertyExtension(BaseModel):
    id: str
    name: Optional[str] = None 
    ProcessPropertyValue: Optional[List[ProcessPropertyValueExtension]] = None # JSON/XML key is "ProcessPropertyValue"

    class Config:
        allow_population_by_field_name = True

class ProcessPropertiesList(BaseModel): # Container for <processProperties>
    ProcessProperty: Optional[List[ProcessPropertyExtension]] = Field(default=None, alias="ProcessProperty") # XML list <ProcessProperty>...</ProcessProperty>

    class Config:
        allow_population_by_field_name = True

# Model for a Dynamic Process Property (referred to as 'properties' in the main model)
class DynamicProcessPropertyExtension(BaseModel):
    name: str 
    value: str

class DynamicProcessPropertiesList(BaseModel): # Container for <properties>
    property: Optional[List[DynamicProcessPropertyExtension]] = Field(default=None, alias="Property") # XML list <property>...</property>

    class Config:
        allow_population_by_field_name = True
        
# Model for Trading Partner Category Field
class TradingPartnerCategoryField(ExtensionField):
    pass

# Model for Trading Partner Category
class TradingPartnerCategory(BaseModel):
    id: str
    name: Optional[str] = None
    field: Optional[List[TradingPartnerCategoryField]] = Field(default=None, alias="Field") # XML list <field>...</field>

    class Config:
        allow_population_by_field_name = True

# Model for a Trading Partner
class TradingPartnerExtension(BaseModel):
    id: str
    name: Optional[str] = None
    category: Optional[List[TradingPartnerCategory]] = Field(default=None, alias="Category") # XML list <category>...</category>

    class Config:
        allow_population_by_field_name = True

class TradingPartnersList(BaseModel): # Container for <tradingPartners>
    tradingPartner: Optional[List[TradingPartnerExtension]] = Field(default=None, alias="TradingPartner") # XML list <tradingPartner>...</tradingPartner>

    class Config:
        allow_population_by_field_name = True

# Model for PGPCertificate
class PGPCertificateExtension(BaseModel):
    id: str 
    value: Optional[str] = None 
    useDefault: Optional[bool] = Field(default=None, alias="useDefault")

    class Config:
        allow_population_by_field_name = True
        
class PGPCertificatesList(BaseModel): # Container for <PGPCertificates>
    PGPCertificate: Optional[List[PGPCertificateExtension]] = Field(default=None, alias="PGPCertificate") # XML list <PGPCertificate>...</PGPCertificate>

    class Config:
        allow_population_by_field_name = True

# Model for Cross Reference Row
class CrossReferenceRow(BaseModel):
    ref1: Optional[str] = None
    ref2: Optional[str] = None
    ref3: Optional[str] = None
    ref4: Optional[str] = None
    ref5: Optional[str] = None
    ref6: Optional[str] = None
    ref7: Optional[str] = None
    ref8: Optional[str] = None
    ref9: Optional[str] = None
    ref10: Optional[str] = None
    ref11: Optional[str] = None
    ref12: Optional[str] = None
    ref13: Optional[str] = None
    ref14: Optional[str] = None
    ref15: Optional[str] = None
    ref16: Optional[str] = None
    ref17: Optional[str] = None
    ref18: Optional[str] = None
    ref19: Optional[str] = None
    ref20: Optional[str] = None

class CrossReferenceRows(BaseModel): # Container for <CrossReferenceRows>
    row: Optional[List[CrossReferenceRow]] = Field(default=None, alias="Row") # XML list <row>...</row>

    class Config:
        allow_population_by_field_name = True

# Model for a Cross Reference Table
class CrossReferenceExtension(BaseModel):
    id: str
    name: Optional[str] = None
    overrideValues: Optional[bool] = Field(default=None, alias="overrideValues")
    CrossReferenceRows: Optional[CrossReferenceRows] = None # JSON/XML key is "CrossReferenceRows"

    class Config:
        allow_population_by_field_name = True

class CrossReferencesList(BaseModel): # Container for <crossReferences>
    crossReference: Optional[List[CrossReferenceExtension]] = Field(default=None, alias="CrossReference") # XML list <crossReference>...</crossReference>

    class Config:
        allow_population_by_field_name = True

# Model for an Operation (Web Services Server operation)
class OperationExtension(BaseModel):
    id: str
    name: Optional[str] = None
    field: Optional[List[ExtensionField]] = Field(default=None, alias="Field") # XML list <field>...</field>

    class Config:
        allow_population_by_field_name = True

class OperationsList(BaseModel): # Container for <operations>
    operation: Optional[List[OperationExtension]] = Field(default=None, alias="Operation") # XML list <operation>...</operation>

    class Config:
        allow_population_by_field_name = True

# Model for Shared Communication Channel
class SharedCommunicationExtension(BaseModel):
    id: str
    name: Optional[str] = None
    type: Optional[str] = None 
    field: Optional[List[ExtensionField]] = Field(default=None, alias="Field") # XML list <field>...</field>

    class Config:
        allow_population_by_field_name = True

class SharedCommunicationsList(BaseModel): # Container for <sharedCommunications>
    sharedCommunication: Optional[List[SharedCommunicationExtension]] = Field(default=None, alias="SharedCommunication") # XML list <sharedCommunication>...</sharedCommunication>

    class Config:
        allow_population_by_field_name = True

# Main EnvironmentExtensionsData model for request body
class EnvironmentExtensionsData(BaseModel):
    partial: Optional[bool] = None 
    
    connections: Optional[ConnectionsList] = None
    processProperties: Optional[ProcessPropertiesList] = None 
    properties: Optional[DynamicProcessPropertiesList] = None 
    tradingPartners: Optional[TradingPartnersList] = None
    PGPCertificates: Optional[PGPCertificatesList] = None
    crossReferences: Optional[CrossReferencesList] = None
    operations: Optional[OperationsList] = None
    sharedCommunications: Optional[SharedCommunicationsList] = None
    
    class Config:
        allow_population_by_field_name = True

# Model for the GET response which includes additional attributes at the root
class EnvironmentExtensionsResponse(EnvironmentExtensionsData):
    environmentId: Optional[str] = None 
    extensionGroupId: Optional[str] = None 
    id: Optional[str] = None 

    class Config:
        allow_population_by_field_name = True
