#!/usr/bin/env python
"""
WordAPI.py
Copyright 2012 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class ConcessionsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def createConcessionOrder(self, location_id, api_key, body, **kwargs):
        """Create a concession style order

        Args:
            location_id, int: SubtleData Location ID (required)
            api_key, str: Subtledata API Key (required)
            body, ConcessionTicketDetails: Concession Ticket Details (required)
            
        Returns: ConcessionOrderResults
        """

        allParams = ['location_id', 'api_key', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createConcessionOrder" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/concessions/{location_id}/order'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('api_key' in params):
            queryParams['api_key'] = self.apiClient.toPathValue(params['api_key'])
        if ('location_id' in params):
            replacement = str(self.apiClient.toPathValue(params['location_id']))
            resourcePath = resourcePath.replace('{' + 'location_id' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ConcessionOrderResults')
        return responseObject
        
        
    


