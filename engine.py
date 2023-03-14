#!/usr/bin/python3

"""
This module provides the class `DBClient`
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.polling_unit import PollingUnit
from models.announced_pu_results import AnnouncedPUResults
from models.lga import LGA
from models.party import Party
from models.ward import Ward
from typing import (Dict, List)
from datetime import datetime


class DBClient:
    """
    DBClient class for communicating with Database
    """

    def __init__(self):
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                               'root',
                               'opeyemi2106',
                               'localhost:3306',
                               'bincomphptest'))
        Session = sessionmaker(bind=engine)
        self.__session = Session()

    def getAllPollingUnitVotes(self) -> Dict:
        """ This returns a record of all the scores for each polling unit """
        results = {}
        polling_units = self.__session.query(PollingUnit)
        for unit in polling_units:
            unit_result = self.__session.query(AnnouncedPUResults)\
                .filter(AnnouncedPUResults.polling_unit_uniqueid ==
                        unit.uniqueid)
            if len(list(unit_result)) > 0:
                results[str(unit.polling_unit_name)] = list(unit_result)
        return results

    def getLgaVotes(self, lga_id: int) -> Dict:
        """ This returns the results for each lga """
        parties_results = {party.partyname: 0 for party in list(
            self.__session.query(Party))}
        parties_results['LABO'] = 0
        del parties_results['LABOUR']
        lga = list(self.__session.query(LGA).filter(LGA.lga_id == lga_id))
        if len(lga) == 0:
            return parties_results
        pollingUnits = self.__session.query(PollingUnit).filter(
            PollingUnit.lga_id == lga[0].lga_id)
        for pu in list(pollingUnits):
            pu_id = pu.uniqueid
            pu_results = list(self.__session.query(AnnouncedPUResults).filter(
                AnnouncedPUResults.polling_unit_uniqueid == pu_id))
            for party_result in pu_results:
                parties_results[party_result.party_abbreviation] +=\
                    party_result.party_score
        return {'lga': lga[0].lga_name, 'results': parties_results}

    def getAllLGAs(self) -> List:
        """ This returns all existing LGAs """
        return list(self.__session.query(LGA))

    def getAllWards(self) -> List:
        """ This returns all existing Wards """
        return list(self.__session.query(Ward))

    def getAllParties(self) -> List:
        """ This returns all existing Parties """
        return list(self.__session.query(Party))

    def addPollingUnit(self, args):
        """ This adds a new Polling unit and its result """
        ward_id = args.get('ward')
        ward = self.__session.query(Ward).filter(
            Ward.uniqueid == ward_id).first()
        polling_unit_name = args.get('polling_unit_name')
        polling_unit_number = args.get('polling_unit_number')
        polling_unit_id = args.get('polling_unit_id')
        entered_by_user = args.get('username')
        lat = args.get('lat')
        long = args.get('long')
        parties = self.getAllParties()
        partydict = {}
        pu_uniqueid = self.__session.query(PollingUnit)\
            .order_by(PollingUnit.uniqueid.desc()).first().uniqueid + 1
        user_ip_address = '127.0.0.1'
        for party in parties:
            partydict[party.partyname] = args.get(party.partyname)
        partydict['LABO'] = partydict['LABOUR']
        del partydict['LABOUR']
        pollingUnit = PollingUnit(uniqueid=pu_uniqueid,
                                  polling_unit_id=polling_unit_id,
                                  ward_id=ward.ward_id, lga_id=ward.lga_id,
                                  uniquewardid=ward.uniqueid,
                                  polling_unit_number=polling_unit_number,
                                  polling_unit_name=polling_unit_name,
                                  polling_unit_description=polling_unit_name,
                                  lat=lat, long=long,
                                  entered_by_user=entered_by_user,
                                  date_entered=datetime.now(),
                                  user_ip_address=user_ip_address)
        self.__session.add(pollingUnit)
        pollingUnit = self.__session.query(PollingUnit)\
            .filter(PollingUnit.uniqueid == pu_uniqueid).first()
        if pollingUnit is None:
            return "Failed to add result for new result"
        result_id = self.__session.query(AnnouncedPUResults)\
            .order_by(AnnouncedPUResults.result_id.desc()).first().result_id + 1
        for party, score in partydict.items():
            pu_result = AnnouncedPUResults(result_id=result_id,
                                           polling_unit_uniqueid=pollingUnit.uniqueid,
                                           party_abbreviation=party,
                                           party_score=score,
                                           entered_by_user=entered_by_user,
                                           date_entered=datetime.now(),
                                           user_ip_address=user_ip_address)
            self.__session.add(pu_result)
            result_id += 1
        self.__session.commit()
        return "Successfully added result for new polling unit"


db = DBClient()
