"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from gs_quant.base import *
from gs_quant.common import *
import datetime
from typing import Dict, Optional, Tuple, Union
from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from enum import Enum


class RiskModelCoverage(EnumBase, Enum):    
    
    """Allowed risk model coverages"""

    Global = 'Global'
    Region = 'Region'
    Region_Excluding_Countries = 'Region Excluding Countries'
    Country = 'Country'    


class RiskModelDataMeasure(EnumBase, Enum):    
    
    """A list of the different risk model data measures to choose from."""

    Asset_Universe = 'Asset Universe'
    Historical_Beta = 'Historical Beta'
    Total_Risk = 'Total Risk'
    Specific_Risk = 'Specific Risk'
    Specific_Return = 'Specific Return'
    Residual_Variance = 'Residual Variance'
    Universe_Factor_Exposure = 'Universe Factor Exposure'
    R_Squared = 'R Squared'
    Fair_Value_Gap_Percent = 'Fair Value Gap Percent'
    Fair_Value_Gap_Standard_Deviation = 'Fair Value Gap Standard Deviation'
    Factor_Id = 'Factor Id'
    Factor_Name = 'Factor Name'
    Factor_Category_Id = 'Factor Category Id'
    Factor_Category = 'Factor Category'
    Factor_Return = 'Factor Return'
    Factor_Standard_Deviation = 'Factor Standard Deviation'
    Factor_Z_Score = 'Factor Z Score'
    Covariance_Matrix = 'Covariance Matrix'
    Issuer_Specific_Covariance = 'Issuer Specific Covariance'
    Factor_Portfolios = 'Factor Portfolios'    


class RiskModelEventType(EnumBase, Enum):    
    
    """Event type for risk model class."""

    Risk_Model = 'Risk Model'
    Risk_Model_PFP_Data = 'Risk Model PFP Data'
    Risk_Model_ISC_Data = 'Risk Model ISC Data'    


class RiskModelLogicalDb(EnumBase, Enum):    
    
    QSAR_AX_NYC = 'QSAR_AX_NYC'
    STUDIO_DAILY = 'STUDIO_DAILY'    


class RiskModelTerm(EnumBase, Enum):    
    
    """Allowed risk model terms"""

    Trading = 'Trading'
    Day = 'Day'
    Short = 'Short'
    Medium = 'Medium'
    Long = 'Long'    


class RiskModelUniverseIdentifier(EnumBase, Enum):    
    
    """The identifier which the risk model is uploaded by."""

    sedol = 'sedol'
    bcid = 'bcid'
    cusip = 'cusip'
    gsid = 'gsid'    


class RiskModelUniverseIdentifierRequest(EnumBase, Enum):    
    
    """The identifier which the risk model is queried by."""

    gsid = 'gsid'
    bbid = 'bbid'
    cusip = 'cusip'
    sedol = 'sedol'
    ric = 'ric'
    ticker = 'ticker'
    primeId = 'primeId'    


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class Factor(Base):
    identifier: str = field(default=None, metadata=field_metadata)
    type_: str = field(default=None, metadata=config(field_name='type', exclude=exclude_none))
    description: Optional[str] = field(default=None, metadata=field_metadata)
    glossary_description: Optional[str] = field(default=None, metadata=field_metadata)
    tooltip: Optional[str] = field(default=None, metadata=field_metadata)
    created_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    created_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    last_updated_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    last_updated_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelCalendar(Base):
    business_dates: Tuple[datetime.date, ...] = field(default=None, metadata=field_metadata)
    created_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    created_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    last_updated_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    last_updated_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelFactorData(Base):
    factor_id: str = field(default=None, metadata=field_metadata)
    factor_name: str = field(default=None, metadata=field_metadata)
    factor_category_id: str = field(default=None, metadata=field_metadata)
    factor_category: str = field(default=None, metadata=field_metadata)
    factor_return: float = field(default=None, metadata=field_metadata)
    factor_standard_deviation: Optional[float] = field(default=None, metadata=field_metadata)
    factor_z_score: Optional[float] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


RiskModelFactorExposure = Dict[str, float]


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelFactorPortfolio(Base):
    factor_id: str = field(default=None, metadata=field_metadata)
    weights: Tuple[float, ...] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelIssuerSpecificCovarianceData(Base):
    universe_id1: Tuple[str, ...] = field(default=None, metadata=field_metadata)
    universe_id2: Tuple[str, ...] = field(default=None, metadata=field_metadata)
    covariance: Tuple[float, ...] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelAssetData(Base):
    universe: Tuple[str, ...] = field(default=None, metadata=field_metadata)
    specific_risk: Tuple[float, ...] = field(default=None, metadata=field_metadata)
    factor_exposure: Tuple[RiskModelFactorExposure, ...] = field(default=None, metadata=field_metadata)
    specific_return: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    residual_variance: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    historical_beta: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    total_risk: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    r_squared: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    fair_value_gap_percent: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    fair_value_gap_standard_deviation: Optional[Tuple[float, ...]] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelCoverageRequest(Base):
    asset_ids: Optional[Tuple[str, ...]] = field(default=None, metadata=field_metadata)
    as_of_date: Optional[datetime.date] = field(default=None, metadata=field_metadata)
    sort_by_term: Optional[RiskModelTerm] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelDataAssetsRequest(Base):
    identifier: RiskModelUniverseIdentifierRequest = field(default=None, metadata=field_metadata)
    universe: Tuple[str, ...] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelFactorPortfoliosData(Base):
    universe: Tuple[str, ...] = field(default=None, metadata=field_metadata)
    portfolio: Tuple[RiskModelFactorPortfolio, ...] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModel(Base):
    coverage: RiskModelCoverage = field(default=None, metadata=field_metadata)
    id_: str = field(default=None, metadata=config(field_name='id', exclude=exclude_none))
    name: str = field(default=None, metadata=field_metadata)
    term: RiskModelTerm = field(default=None, metadata=field_metadata)
    universe_identifier: RiskModelUniverseIdentifier = field(default=None, metadata=field_metadata)
    vendor: str = field(default=None, metadata=field_metadata)
    version: float = field(default=None, metadata=field_metadata)
    created_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    created_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    description: Optional[str] = field(default=None, metadata=field_metadata)
    entitlements: Optional[Entitlements] = field(default=None, metadata=field_metadata)
    last_updated_by_id: Optional[str] = field(default=None, metadata=field_metadata)
    last_updated_time: Optional[datetime.datetime] = field(default=None, metadata=field_metadata)
    expected_update_time: Optional[str] = field(default=None, metadata=field_metadata)
    owner_id: Optional[str] = field(default=None, metadata=field_metadata)
    universe_size: Optional[int] = field(default=None, metadata=field_metadata)
    type_: Optional[RiskModelType] = field(default=None, metadata=config(field_name='type', exclude=exclude_none))


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelData(Base):
    date: datetime.date = field(default=None, metadata=field_metadata)
    asset_data: Optional[RiskModelAssetData] = field(default=None, metadata=field_metadata)
    factor_data: Optional[Tuple[RiskModelFactorData, ...]] = field(default=None, metadata=field_metadata)
    covariance_matrix: Optional[Tuple[Tuple[float, ...], ...]] = field(default=None, metadata=field_metadata)
    issuer_specific_covariance: Optional[RiskModelIssuerSpecificCovarianceData] = field(default=None, metadata=field_metadata)
    factor_portfolios: Optional[RiskModelFactorPortfoliosData] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelDataRequest(Base):
    start_date: datetime.date = field(default=None, metadata=field_metadata)
    end_date: datetime.date = field(default=None, metadata=field_metadata)
    assets: Optional[RiskModelDataAssetsRequest] = field(default=None, metadata=field_metadata)
    measures: Optional[Tuple[RiskModelDataMeasure, ...]] = field(default=None, metadata=field_metadata)
    limit_factors: Optional[bool] = field(default=True, metadata=field_metadata)
    format_: Optional[str] = field(default='Json', metadata=config(field_name='format', exclude=exclude_none))
    name: Optional[str] = field(default=None, metadata=name_metadata)


@handle_camel_case_args
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(unsafe_hash=True, repr=False)
class RiskModelDataResponse(Base):
    results: Tuple[RiskModelData, ...] = field(default=None, metadata=field_metadata)
    total_results: int = field(default=None, metadata=field_metadata)
    missing_dates: Optional[Tuple[datetime.date, ...]] = field(default=None, metadata=field_metadata)
    name: Optional[str] = field(default=None, metadata=name_metadata)
