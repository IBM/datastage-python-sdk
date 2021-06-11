# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for DatastageV3
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from datastage.datastage_v3 import *


_service = DatastageV3(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://datastage.cloud.ibm.com/data_intg'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: DataStageFlows
##############################################################################
# region

class TestDeleteDatastageFlows():
    """
    Test Class for delete_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_datastage_flows_all_params(self):
        """
        delete_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        force = True

        # Invoke method
        response = _service.delete_datastage_flows(
            id,
            catalog_id=catalog_id,
            project_id=project_id,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(','.join(id)) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'force={}'.format('true' if force else 'false') in query_string


    @responses.activate
    def test_delete_datastage_flows_required_params(self):
        """
        test_delete_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']

        # Invoke method
        response = _service.delete_datastage_flows(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(','.join(id)) in query_string


    @responses.activate
    def test_delete_datastage_flows_value_error(self):
        """
        test_delete_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_datastage_flows(**req_copy)



class TestListDatastageFlows():
    """
    Test Class for list_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_datastage_flows_all_params(self):
        """
        list_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        mock_response = '{"data_flows": [{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}], "first": {"href": "href"}, "last": {"href": "href"}, "limit": 5, "next": {"href": "href"}, "prev": {"href": "href"}, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        sort = 'testString'
        start = 'testString'
        limit = 100
        entity_name = 'testString'
        entity_description = 'testString'

        # Invoke method
        response = _service.list_datastage_flows(
            catalog_id=catalog_id,
            project_id=project_id,
            sort=sort,
            start=start,
            limit=limit,
            entity_name=entity_name,
            entity_description=entity_description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'entity.name={}'.format(entity_name) in query_string
        assert 'entity.description={}'.format(entity_description) in query_string


    @responses.activate
    def test_list_datastage_flows_required_params(self):
        """
        test_list_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        mock_response = '{"data_flows": [{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}], "first": {"href": "href"}, "last": {"href": "href"}, "limit": 5, "next": {"href": "href"}, "prev": {"href": "href"}, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Invoke method
        response = _service.list_datastage_flows()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateDatastageFlows():
    """
    Test Class for create_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_datastage_flows_all_params(self):
        """
        create_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        asset_category = 'system'

        # Invoke method
        response = _service.create_datastage_flows(
            data_intg_flow_name,
            pipeline_flows=pipeline_flows,
            catalog_id=catalog_id,
            project_id=project_id,
            asset_category=asset_category,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_flow_name={}'.format(data_intg_flow_name) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'asset_category={}'.format(asset_category) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_create_datastage_flows_required_params(self):
        """
        test_create_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Invoke method
        response = _service.create_datastage_flows(
            data_intg_flow_name,
            pipeline_flows=pipeline_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_flow_name={}'.format(data_intg_flow_name) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_create_datastage_flows_value_error(self):
        """
        test_create_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_flow_name": data_intg_flow_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_datastage_flows(**req_copy)



class TestGetDatastageFlows():
    """
    Test Class for get_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_datastage_flows_all_params(self):
        """
        get_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.get_datastage_flows(
            data_intg_flow_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_get_datastage_flows_required_params(self):
        """
        test_get_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Invoke method
        response = _service.get_datastage_flows(
            data_intg_flow_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_datastage_flows_value_error(self):
        """
        test_get_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_flow_id": data_intg_flow_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_datastage_flows(**req_copy)



class TestUpdateDatastageFlows():
    """
    Test Class for update_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_datastage_flows_all_params(self):
        """
        update_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_id = 'testString'
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.update_datastage_flows(
            data_intg_flow_id,
            data_intg_flow_name,
            pipeline_flows=pipeline_flows,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_flow_name={}'.format(data_intg_flow_name) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_update_datastage_flows_required_params(self):
        """
        test_update_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_id = 'testString'
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Invoke method
        response = _service.update_datastage_flows(
            data_intg_flow_id,
            data_intg_flow_name,
            pipeline_flows=pipeline_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_flow_name={}'.format(data_intg_flow_name) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_update_datastage_flows_value_error(self):
        """
        test_update_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_flow_id = 'testString'
        data_intg_flow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_flow_id": data_intg_flow_id,
            "data_intg_flow_name": data_intg_flow_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_datastage_flows(**req_copy)



class TestCloneDatastageFlows():
    """
    Test Class for clone_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_clone_datastage_flows_all_params(self):
        """
        clone_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_flow_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.clone_datastage_flows(
            data_intg_flow_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_clone_datastage_flows_required_params(self):
        """
        test_clone_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Invoke method
        response = _service.clone_datastage_flows(
            data_intg_flow_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_clone_datastage_flows_value_error(self):
        """
        test_clone_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_flow_id": data_intg_flow_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.clone_datastage_flows(**req_copy)



class TestCompileDatastageFlows():
    """
    Test Class for compile_datastage_flows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_compile_datastage_flows_all_params(self):
        """
        compile_datastage_flows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/ds_codegen/compile/testString')
        mock_response = '{"message": {"anyKey": "anyValue"}, "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        runtime_type = 'testString'

        # Invoke method
        response = _service.compile_datastage_flows(
            data_intg_flow_id,
            catalog_id=catalog_id,
            project_id=project_id,
            runtime_type=runtime_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'runtime_type={}'.format(runtime_type) in query_string


    @responses.activate
    def test_compile_datastage_flows_required_params(self):
        """
        test_compile_datastage_flows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/ds_codegen/compile/testString')
        mock_response = '{"message": {"anyKey": "anyValue"}, "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Invoke method
        response = _service.compile_datastage_flows(
            data_intg_flow_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_compile_datastage_flows_value_error(self):
        """
        test_compile_datastage_flows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/ds_codegen/compile/testString')
        mock_response = '{"message": {"anyKey": "anyValue"}, "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_flow_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_flow_id": data_intg_flow_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.compile_datastage_flows(**req_copy)



# endregion
##############################################################################
# End of Service: DataStageFlows
##############################################################################

##############################################################################
# Start of Service: DataStageSubflows
##############################################################################
# region

class TestDeleteDatastageSubflows():
    """
    Test Class for delete_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_datastage_subflows_all_params(self):
        """
        delete_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.delete_datastage_subflows(
            id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(','.join(id)) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_delete_datastage_subflows_required_params(self):
        """
        test_delete_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']

        # Invoke method
        response = _service.delete_datastage_subflows(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(','.join(id)) in query_string


    @responses.activate
    def test_delete_datastage_subflows_value_error(self):
        """
        test_delete_datastage_subflows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        id = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_datastage_subflows(**req_copy)



class TestListDatastageSubflows():
    """
    Test Class for list_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_datastage_subflows_all_params(self):
        """
        list_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        mock_response = '{"data_flows": [{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}], "first": {"href": "href"}, "last": {"href": "href"}, "limit": 5, "next": {"href": "href"}, "prev": {"href": "href"}, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        sort = 'testString'
        start = 'testString'
        limit = 100
        entity_name = 'testString'
        entity_description = 'testString'

        # Invoke method
        response = _service.list_datastage_subflows(
            catalog_id=catalog_id,
            project_id=project_id,
            sort=sort,
            start=start,
            limit=limit,
            entity_name=entity_name,
            entity_description=entity_description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'entity.name={}'.format(entity_name) in query_string
        assert 'entity.description={}'.format(entity_description) in query_string


    @responses.activate
    def test_list_datastage_subflows_required_params(self):
        """
        test_list_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        mock_response = '{"data_flows": [{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}], "first": {"href": "href"}, "last": {"href": "href"}, "limit": 5, "next": {"href": "href"}, "prev": {"href": "href"}, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Invoke method
        response = _service.list_datastage_subflows()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateDatastageSubflows():
    """
    Test Class for create_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_datastage_subflows_all_params(self):
        """
        create_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        asset_category = 'system'

        # Invoke method
        response = _service.create_datastage_subflows(
            data_intg_subflow_name,
            pipeline_flows=pipeline_flows,
            catalog_id=catalog_id,
            project_id=project_id,
            asset_category=asset_category,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_subflow_name={}'.format(data_intg_subflow_name) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'asset_category={}'.format(asset_category) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_create_datastage_subflows_required_params(self):
        """
        test_create_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Invoke method
        response = _service.create_datastage_subflows(
            data_intg_subflow_name,
            pipeline_flows=pipeline_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_subflow_name={}'.format(data_intg_subflow_name) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_create_datastage_subflows_value_error(self):
        """
        test_create_datastage_subflows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_subflow_name": data_intg_subflow_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_datastage_subflows(**req_copy)



class TestGetDatastageSubflows():
    """
    Test Class for get_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_datastage_subflows_all_params(self):
        """
        get_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_subflow_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.get_datastage_subflows(
            data_intg_subflow_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_get_datastage_subflows_required_params(self):
        """
        test_get_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_subflow_id = 'testString'

        # Invoke method
        response = _service.get_datastage_subflows(
            data_intg_subflow_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_datastage_subflows_value_error(self):
        """
        test_get_datastage_subflows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": {"app_data": {"anyKey": "anyValue"}, "doc_type": "pipeline", "external_paramsets": [{"anyKey": "anyValue"}], "id": "84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff", "json_schema": "http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json", "parameters": {"anyKey": "anyValue"}, "pipelines": [{"app_data": {"anyKey": "anyValue"}, "description": "A test DataStage flow.", "id": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "name": "ContainerC1", "nodes": [{"anyKey": "anyValue"}], "runtime_ref": "pxOsh"}], "primary_pipeline": "fa1b859a-d592-474d-b56c-2137e4efa4bc", "runtimes": [{"anyKey": "anyValue"}], "schemas": [{"anyKey": "anyValue"}], "version": "3.0"}, "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        data_intg_subflow_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_subflow_id": data_intg_subflow_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_datastage_subflows(**req_copy)



class TestUpdateDatastageSubflows():
    """
    Test Class for update_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_datastage_subflows_all_params(self):
        """
        update_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_id = 'testString'
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.update_datastage_subflows(
            data_intg_subflow_id,
            data_intg_subflow_name,
            pipeline_flows=pipeline_flows,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_subflow_name={}'.format(data_intg_subflow_name) in query_string
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_update_datastage_subflows_required_params(self):
        """
        test_update_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_id = 'testString'
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Invoke method
        response = _service.update_datastage_subflows(
            data_intg_subflow_id,
            data_intg_subflow_name,
            pipeline_flows=pipeline_flows,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'data_intg_subflow_name={}'.format(data_intg_subflow_name) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['pipeline_flows'] == pipeline_json_model


    @responses.activate
    def test_update_datastage_subflows_value_error(self):
        """
        test_update_datastage_subflows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Construct a dict representation of a Pipelines model
        pipelines_model = {}
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {}
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        # Set up parameter values
        data_intg_subflow_id = 'testString'
        data_intg_subflow_name = 'testString'
        pipeline_flows = pipeline_json_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_subflow_id": data_intg_subflow_id,
            "data_intg_subflow_name": data_intg_subflow_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_datastage_subflows(**req_copy)



class TestCloneDatastageSubflows():
    """
    Test Class for clone_datastage_subflows
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_clone_datastage_subflows_all_params(self):
        """
        clone_datastage_subflows()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_subflow_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.clone_datastage_subflows(
            data_intg_subflow_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_clone_datastage_subflows_required_params(self):
        """
        test_clone_datastage_subflows_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_subflow_id = 'testString'

        # Invoke method
        response = _service.clone_datastage_subflows(
            data_intg_subflow_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_clone_datastage_subflows_value_error(self):
        """
        test_clone_datastage_subflows_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/data_intg_flows/subflows/testString/clone')
        mock_response = '{"attachments": [{"anyKey": "anyValue"}], "entity": {"data_intg_flow": {"anyKey": "anyValue"}, "data_intg_subflow": {"anyKey": "anyValue"}, "description": "description", "lock": {"entity": {"data_intg_flow_id": "data_intg_flow_id", "requester": "requester"}, "metadata": {"alive": false}}, "name": "name", "rov": {"members": ["members"], "mode": 4}, "sub_type": "sub_type"}, "metadata": {"asset_id": "asset_id", "asset_type": "asset_type", "catalog_id": "catalog_id", "create_time": "2019-01-01T12:00:00.000Z", "creator_id": "creator_id", "description": "description", "href": "href", "name": "name", "origin_country": "origin_country", "project_id": "project_id", "resource_key": "resource_key", "size": 4, "source_system": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "usage": {"access_count": 12, "last_access_time": "2019-01-01T12:00:00.000Z", "last_accessor_id": "last_accessor_id", "last_modification_time": "2019-01-01T12:00:00.000Z", "last_modifier_id": "last_modifier_id"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=201)

        # Set up parameter values
        data_intg_subflow_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "data_intg_subflow_id": data_intg_subflow_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.clone_datastage_subflows(**req_copy)



# endregion
##############################################################################
# End of Service: DataStageSubflows
##############################################################################

##############################################################################
# Start of Service: Migration
##############################################################################
# region

class TestCreateMigration():
    """
    Test Class for create_migration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_migration_all_params(self):
        """
        create_migration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=202)

        # Set up parameter values
        body = io.BytesIO(b'This is a mock file.').getvalue()
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'
        on_failure = 'continue'
        conflict_resolution = 'rename'
        attachment_type = 'isx'
        file_name = 'myFlows.isx'

        # Invoke method
        response = _service.create_migration(
            body,
            catalog_id=catalog_id,
            project_id=project_id,
            on_failure=on_failure,
            conflict_resolution=conflict_resolution,
            attachment_type=attachment_type,
            file_name=file_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string
        assert 'on_failure={}'.format(on_failure) in query_string
        assert 'conflict_resolution={}'.format(conflict_resolution) in query_string
        assert 'attachment_type={}'.format(attachment_type) in query_string
        assert 'file_name={}'.format(file_name) in query_string
        # Validate body params
        assert responses.calls[0].request.body == body


    @responses.activate
    def test_create_migration_required_params(self):
        """
        test_create_migration_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=202)

        # Set up parameter values
        body = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_migration(
            body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        assert responses.calls[0].request.body == body


    @responses.activate
    def test_create_migration_value_error(self):
        """
        test_create_migration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=202)

        # Set up parameter values
        body = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_migration(**req_copy)



class TestDeleteMigration():
    """
    Test Class for delete_migration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_migration_all_params(self):
        """
        delete_migration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/cc6dbbfd-810d-4f0e-b0a9-228c328aff29')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        import_id = 'cc6dbbfd-810d-4f0e-b0a9-228c328aff29'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.delete_migration(
            import_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_delete_migration_required_params(self):
        """
        test_delete_migration_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/cc6dbbfd-810d-4f0e-b0a9-228c328aff29')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        import_id = 'cc6dbbfd-810d-4f0e-b0a9-228c328aff29'

        # Invoke method
        response = _service.delete_migration(
            import_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_migration_value_error(self):
        """
        test_delete_migration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/cc6dbbfd-810d-4f0e-b0a9-228c328aff29')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        import_id = 'cc6dbbfd-810d-4f0e-b0a9-228c328aff29'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "import_id": import_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_migration(**req_copy)



class TestGetMigration():
    """
    Test Class for get_migration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_migration_all_params(self):
        """
        get_migration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/testString')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        import_id = 'testString'
        catalog_id = 'testString'
        project_id = 'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'

        # Invoke method
        response = _service.get_migration(
            import_id,
            catalog_id=catalog_id,
            project_id=project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_id={}'.format(catalog_id) in query_string
        assert 'project_id={}'.format(project_id) in query_string


    @responses.activate
    def test_get_migration_required_params(self):
        """
        test_get_migration_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/testString')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        import_id = 'testString'

        # Invoke method
        response = _service.get_migration(
            import_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_migration_value_error(self):
        """
        test_get_migration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/migration/isx_imports/testString')
        mock_response = '{"entity": {"cancelled_by": "user1@company1.com", "conflict_resolution": "conflict_resolution", "end_time": "2019-01-01T12:00:00.000Z", "import_data_flows": [{"conflict_resolution_status": "import_flow_renamed", "end_time": "2019-01-01T12:00:00.000Z", "errors": [{"description": "description", "name": "name", "stage_type": "stage_type", "type": "unsupported_stage_type"}], "id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "job_id": "ccfaaafd-810d-4f0e-b0a9-228c328a0136", "job_name": "Aggregator12_DataStage_1", "job_type": "px_job", "name": "cancel-reservation-job", "original_name": "cancel-reservation-job", "ref_asset_id": "ccfdbbfd-810d-4f0e-b0a9-228c328a0136", "status": "completed", "type": "px_job", "warnings": [{"description": "description", "name": "name", "type": "unreleased_stage_type"}]}], "name": "seat-reservation-jobs", "notifications": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "id", "status": "status"}], "on_failure": "on_failure", "remaining_time": 14, "start_time": "2019-01-01T12:00:00.000Z", "status": "in_progress", "tally": {"connections_total": 17, "deprecated": 10, "failed": 6, "imported": 8, "parameter_sets_total": 20, "pending": 7, "renamed": 7, "replaced": 8, "sequence_jobs_total": 19, "skipped": 7, "subflows_total": 14, "table_definitions_total": 23, "total": 5, "unsupported": 11}}, "metadata": {"catalog_id": "catalog_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "user1@company1.com", "id": "id", "modified_at": "2019-01-01T12:00:00.000Z", "name": "name", "project_id": "project_id", "project_name": "project_name", "url": "url"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json;charset=utf-8',
                      status=200)

        # Set up parameter values
        import_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "import_id": import_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_migration(**req_copy)



# endregion
##############################################################################
# End of Service: Migration
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class AssetEntityROVUnitTests():
    """
    Test Class for AssetEntityROV
    """

    def test_asset_entity_rov_serialization(self):
        """
        Test serialization/deserialization for AssetEntityROV
        """

        # Construct a json representation of a AssetEntityROV model
        asset_entity_rov_model_json = {}
        asset_entity_rov_model_json['members'] = ['testString']
        asset_entity_rov_model_json['mode'] = 38

        # Construct a model instance of AssetEntityROV by calling from_dict on the json representation
        asset_entity_rov_model = AssetEntityROV.from_dict(asset_entity_rov_model_json)
        assert asset_entity_rov_model != False

        # Construct a model instance of AssetEntityROV by calling from_dict on the json representation
        asset_entity_rov_model_dict = AssetEntityROV.from_dict(asset_entity_rov_model_json).__dict__
        asset_entity_rov_model2 = AssetEntityROV(**asset_entity_rov_model_dict)

        # Verify the model instances are equivalent
        assert asset_entity_rov_model == asset_entity_rov_model2

        # Convert model instance back to dict and verify no loss of data
        asset_entity_rov_model_json2 = asset_entity_rov_model.to_dict()
        assert asset_entity_rov_model_json2 == asset_entity_rov_model_json

class AssetSystemMetadataUnitTests():
    """
    Test Class for AssetSystemMetadata
    """

    def test_asset_system_metadata_serialization(self):
        """
        Test serialization/deserialization for AssetSystemMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        asset_system_metadata_usage_model = {} # AssetSystemMetadataUsage
        asset_system_metadata_usage_model['access_count'] = 38
        asset_system_metadata_usage_model['last_access_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_accessor_id'] = 'testString'
        asset_system_metadata_usage_model['last_modification_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_modifier_id'] = 'testString'

        # Construct a json representation of a AssetSystemMetadata model
        asset_system_metadata_model_json = {}
        asset_system_metadata_model_json['asset_id'] = 'testString'
        asset_system_metadata_model_json['asset_type'] = 'testString'
        asset_system_metadata_model_json['catalog_id'] = 'testString'
        asset_system_metadata_model_json['create_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_model_json['creator_id'] = 'testString'
        asset_system_metadata_model_json['description'] = 'testString'
        asset_system_metadata_model_json['href'] = 'testString'
        asset_system_metadata_model_json['name'] = 'testString'
        asset_system_metadata_model_json['origin_country'] = 'testString'
        asset_system_metadata_model_json['project_id'] = 'testString'
        asset_system_metadata_model_json['resource_key'] = 'testString'
        asset_system_metadata_model_json['size'] = 38
        asset_system_metadata_model_json['source_system'] = {}
        asset_system_metadata_model_json['tags'] = ['testString']
        asset_system_metadata_model_json['usage'] = asset_system_metadata_usage_model

        # Construct a model instance of AssetSystemMetadata by calling from_dict on the json representation
        asset_system_metadata_model = AssetSystemMetadata.from_dict(asset_system_metadata_model_json)
        assert asset_system_metadata_model != False

        # Construct a model instance of AssetSystemMetadata by calling from_dict on the json representation
        asset_system_metadata_model_dict = AssetSystemMetadata.from_dict(asset_system_metadata_model_json).__dict__
        asset_system_metadata_model2 = AssetSystemMetadata(**asset_system_metadata_model_dict)

        # Verify the model instances are equivalent
        assert asset_system_metadata_model == asset_system_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        asset_system_metadata_model_json2 = asset_system_metadata_model.to_dict()
        assert asset_system_metadata_model_json2 == asset_system_metadata_model_json

class AssetSystemMetadataUsageUnitTests():
    """
    Test Class for AssetSystemMetadataUsage
    """

    def test_asset_system_metadata_usage_serialization(self):
        """
        Test serialization/deserialization for AssetSystemMetadataUsage
        """

        # Construct a json representation of a AssetSystemMetadataUsage model
        asset_system_metadata_usage_model_json = {}
        asset_system_metadata_usage_model_json['access_count'] = 38
        asset_system_metadata_usage_model_json['last_access_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model_json['last_accessor_id'] = 'testString'
        asset_system_metadata_usage_model_json['last_modification_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model_json['last_modifier_id'] = 'testString'

        # Construct a model instance of AssetSystemMetadataUsage by calling from_dict on the json representation
        asset_system_metadata_usage_model = AssetSystemMetadataUsage.from_dict(asset_system_metadata_usage_model_json)
        assert asset_system_metadata_usage_model != False

        # Construct a model instance of AssetSystemMetadataUsage by calling from_dict on the json representation
        asset_system_metadata_usage_model_dict = AssetSystemMetadataUsage.from_dict(asset_system_metadata_usage_model_json).__dict__
        asset_system_metadata_usage_model2 = AssetSystemMetadataUsage(**asset_system_metadata_usage_model_dict)

        # Verify the model instances are equivalent
        assert asset_system_metadata_usage_model == asset_system_metadata_usage_model2

        # Convert model instance back to dict and verify no loss of data
        asset_system_metadata_usage_model_json2 = asset_system_metadata_usage_model.to_dict()
        assert asset_system_metadata_usage_model_json2 == asset_system_metadata_usage_model_json

class DataFlowPagedCollectionUnitTests():
    """
    Test Class for DataFlowPagedCollection
    """

    def test_data_flow_paged_collection_serialization(self):
        """
        Test serialization/deserialization for DataFlowPagedCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_intg_flow_lock_entity_model = {} # DataIntgFlowLockEntity
        data_intg_flow_lock_entity_model['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model['requester'] = 'testString'

        data_intg_flow_lock_metadata_model = {} # DataIntgFlowLockMetadata
        data_intg_flow_lock_metadata_model['alive'] = True

        data_intg_flow_lock_model = {} # DataIntgFlowLock
        data_intg_flow_lock_model['entity'] = data_intg_flow_lock_entity_model
        data_intg_flow_lock_model['metadata'] = data_intg_flow_lock_metadata_model

        asset_entity_rov_model = {} # AssetEntityROV
        asset_entity_rov_model['members'] = ['testString']
        asset_entity_rov_model['mode'] = 38

        data_intg_flow_entity_model = {} # DataIntgFlowEntity
        data_intg_flow_entity_model['data_intg_flow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['data_intg_subflow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['description'] = 'testString'
        data_intg_flow_entity_model['lock'] = data_intg_flow_lock_model
        data_intg_flow_entity_model['name'] = 'testString'
        data_intg_flow_entity_model['rov'] = asset_entity_rov_model
        data_intg_flow_entity_model['sub_type'] = 'testString'

        asset_system_metadata_usage_model = {} # AssetSystemMetadataUsage
        asset_system_metadata_usage_model['access_count'] = 38
        asset_system_metadata_usage_model['last_access_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_accessor_id'] = 'testString'
        asset_system_metadata_usage_model['last_modification_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_modifier_id'] = 'testString'

        asset_system_metadata_model = {} # AssetSystemMetadata
        asset_system_metadata_model['asset_id'] = 'testString'
        asset_system_metadata_model['asset_type'] = 'testString'
        asset_system_metadata_model['catalog_id'] = 'testString'
        asset_system_metadata_model['create_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_model['creator_id'] = 'testString'
        asset_system_metadata_model['description'] = 'testString'
        asset_system_metadata_model['href'] = 'testString'
        asset_system_metadata_model['name'] = 'testString'
        asset_system_metadata_model['origin_country'] = 'testString'
        asset_system_metadata_model['project_id'] = 'testString'
        asset_system_metadata_model['resource_key'] = 'testString'
        asset_system_metadata_model['size'] = 38
        asset_system_metadata_model['source_system'] = {}
        asset_system_metadata_model['tags'] = ['testString']
        asset_system_metadata_model['usage'] = asset_system_metadata_usage_model

        data_intg_flow_model = {} # DataIntgFlow
        data_intg_flow_model['attachments'] = [{ 'foo': 'bar' }]
        data_intg_flow_model['entity'] = data_intg_flow_entity_model
        data_intg_flow_model['metadata'] = asset_system_metadata_model

        href_model_model = {} # HrefModel
        href_model_model['href'] = 'testString'

        # Construct a json representation of a DataFlowPagedCollection model
        data_flow_paged_collection_model_json = {}
        data_flow_paged_collection_model_json['data_flows'] = [data_intg_flow_model]
        data_flow_paged_collection_model_json['first'] = href_model_model
        data_flow_paged_collection_model_json['last'] = href_model_model
        data_flow_paged_collection_model_json['limit'] = 38
        data_flow_paged_collection_model_json['next'] = href_model_model
        data_flow_paged_collection_model_json['prev'] = href_model_model
        data_flow_paged_collection_model_json['total_count'] = 38

        # Construct a model instance of DataFlowPagedCollection by calling from_dict on the json representation
        data_flow_paged_collection_model = DataFlowPagedCollection.from_dict(data_flow_paged_collection_model_json)
        assert data_flow_paged_collection_model != False

        # Construct a model instance of DataFlowPagedCollection by calling from_dict on the json representation
        data_flow_paged_collection_model_dict = DataFlowPagedCollection.from_dict(data_flow_paged_collection_model_json).__dict__
        data_flow_paged_collection_model2 = DataFlowPagedCollection(**data_flow_paged_collection_model_dict)

        # Verify the model instances are equivalent
        assert data_flow_paged_collection_model == data_flow_paged_collection_model2

        # Convert model instance back to dict and verify no loss of data
        data_flow_paged_collection_model_json2 = data_flow_paged_collection_model.to_dict()
        assert data_flow_paged_collection_model_json2 == data_flow_paged_collection_model_json

class DataImportErrorUnitTests():
    """
    Test Class for DataImportError
    """

    def test_data_import_error_serialization(self):
        """
        Test serialization/deserialization for DataImportError
        """

        # Construct a json representation of a DataImportError model
        data_import_error_model_json = {}
        data_import_error_model_json['description'] = 'testString'
        data_import_error_model_json['name'] = 'testString'
        data_import_error_model_json['stage_type'] = 'testString'
        data_import_error_model_json['type'] = 'unsupported_stage_type'

        # Construct a model instance of DataImportError by calling from_dict on the json representation
        data_import_error_model = DataImportError.from_dict(data_import_error_model_json)
        assert data_import_error_model != False

        # Construct a model instance of DataImportError by calling from_dict on the json representation
        data_import_error_model_dict = DataImportError.from_dict(data_import_error_model_json).__dict__
        data_import_error_model2 = DataImportError(**data_import_error_model_dict)

        # Verify the model instances are equivalent
        assert data_import_error_model == data_import_error_model2

        # Convert model instance back to dict and verify no loss of data
        data_import_error_model_json2 = data_import_error_model.to_dict()
        assert data_import_error_model_json2 == data_import_error_model_json

class DataIntgFlowUnitTests():
    """
    Test Class for DataIntgFlow
    """

    def test_data_intg_flow_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_intg_flow_lock_entity_model = {} # DataIntgFlowLockEntity
        data_intg_flow_lock_entity_model['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model['requester'] = 'testString'

        data_intg_flow_lock_metadata_model = {} # DataIntgFlowLockMetadata
        data_intg_flow_lock_metadata_model['alive'] = True

        data_intg_flow_lock_model = {} # DataIntgFlowLock
        data_intg_flow_lock_model['entity'] = data_intg_flow_lock_entity_model
        data_intg_flow_lock_model['metadata'] = data_intg_flow_lock_metadata_model

        asset_entity_rov_model = {} # AssetEntityROV
        asset_entity_rov_model['members'] = ['testString']
        asset_entity_rov_model['mode'] = 38

        data_intg_flow_entity_model = {} # DataIntgFlowEntity
        data_intg_flow_entity_model['data_intg_flow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['data_intg_subflow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['description'] = 'testString'
        data_intg_flow_entity_model['lock'] = data_intg_flow_lock_model
        data_intg_flow_entity_model['name'] = 'testString'
        data_intg_flow_entity_model['rov'] = asset_entity_rov_model
        data_intg_flow_entity_model['sub_type'] = 'testString'

        asset_system_metadata_usage_model = {} # AssetSystemMetadataUsage
        asset_system_metadata_usage_model['access_count'] = 38
        asset_system_metadata_usage_model['last_access_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_accessor_id'] = 'testString'
        asset_system_metadata_usage_model['last_modification_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_modifier_id'] = 'testString'

        asset_system_metadata_model = {} # AssetSystemMetadata
        asset_system_metadata_model['asset_id'] = 'testString'
        asset_system_metadata_model['asset_type'] = 'testString'
        asset_system_metadata_model['catalog_id'] = 'testString'
        asset_system_metadata_model['create_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_model['creator_id'] = 'testString'
        asset_system_metadata_model['description'] = 'testString'
        asset_system_metadata_model['href'] = 'testString'
        asset_system_metadata_model['name'] = 'testString'
        asset_system_metadata_model['origin_country'] = 'testString'
        asset_system_metadata_model['project_id'] = 'testString'
        asset_system_metadata_model['resource_key'] = 'testString'
        asset_system_metadata_model['size'] = 38
        asset_system_metadata_model['source_system'] = {}
        asset_system_metadata_model['tags'] = ['testString']
        asset_system_metadata_model['usage'] = asset_system_metadata_usage_model

        # Construct a json representation of a DataIntgFlow model
        data_intg_flow_model_json = {}
        data_intg_flow_model_json['attachments'] = [{ 'foo': 'bar' }]
        data_intg_flow_model_json['entity'] = data_intg_flow_entity_model
        data_intg_flow_model_json['metadata'] = asset_system_metadata_model

        # Construct a model instance of DataIntgFlow by calling from_dict on the json representation
        data_intg_flow_model = DataIntgFlow.from_dict(data_intg_flow_model_json)
        assert data_intg_flow_model != False

        # Construct a model instance of DataIntgFlow by calling from_dict on the json representation
        data_intg_flow_model_dict = DataIntgFlow.from_dict(data_intg_flow_model_json).__dict__
        data_intg_flow_model2 = DataIntgFlow(**data_intg_flow_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_model == data_intg_flow_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_model_json2 = data_intg_flow_model.to_dict()
        assert data_intg_flow_model_json2 == data_intg_flow_model_json

class DataIntgFlowEntityUnitTests():
    """
    Test Class for DataIntgFlowEntity
    """

    def test_data_intg_flow_entity_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlowEntity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_intg_flow_lock_entity_model = {} # DataIntgFlowLockEntity
        data_intg_flow_lock_entity_model['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model['requester'] = 'testString'

        data_intg_flow_lock_metadata_model = {} # DataIntgFlowLockMetadata
        data_intg_flow_lock_metadata_model['alive'] = True

        data_intg_flow_lock_model = {} # DataIntgFlowLock
        data_intg_flow_lock_model['entity'] = data_intg_flow_lock_entity_model
        data_intg_flow_lock_model['metadata'] = data_intg_flow_lock_metadata_model

        asset_entity_rov_model = {} # AssetEntityROV
        asset_entity_rov_model['members'] = ['testString']
        asset_entity_rov_model['mode'] = 38

        # Construct a json representation of a DataIntgFlowEntity model
        data_intg_flow_entity_model_json = {}
        data_intg_flow_entity_model_json['data_intg_flow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model_json['data_intg_subflow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model_json['description'] = 'testString'
        data_intg_flow_entity_model_json['lock'] = data_intg_flow_lock_model
        data_intg_flow_entity_model_json['name'] = 'testString'
        data_intg_flow_entity_model_json['rov'] = asset_entity_rov_model
        data_intg_flow_entity_model_json['sub_type'] = 'testString'

        # Construct a model instance of DataIntgFlowEntity by calling from_dict on the json representation
        data_intg_flow_entity_model = DataIntgFlowEntity.from_dict(data_intg_flow_entity_model_json)
        assert data_intg_flow_entity_model != False

        # Construct a model instance of DataIntgFlowEntity by calling from_dict on the json representation
        data_intg_flow_entity_model_dict = DataIntgFlowEntity.from_dict(data_intg_flow_entity_model_json).__dict__
        data_intg_flow_entity_model2 = DataIntgFlowEntity(**data_intg_flow_entity_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_entity_model == data_intg_flow_entity_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_entity_model_json2 = data_intg_flow_entity_model.to_dict()
        assert data_intg_flow_entity_model_json2 == data_intg_flow_entity_model_json

class DataIntgFlowJsonUnitTests():
    """
    Test Class for DataIntgFlowJson
    """

    def test_data_intg_flow_json_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlowJson
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pipelines_model = {} # Pipelines
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        pipeline_json_model = {} # PipelineJson
        pipeline_json_model['app_data'] = { 'foo': 'bar' }
        pipeline_json_model['doc_type'] = 'pipeline'
        pipeline_json_model['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model['parameters'] = { 'foo': 'bar' }
        pipeline_json_model['pipelines'] = [pipelines_model]
        pipeline_json_model['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model['version'] = '3.0'

        data_intg_flow_lock_entity_model = {} # DataIntgFlowLockEntity
        data_intg_flow_lock_entity_model['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model['requester'] = 'testString'

        data_intg_flow_lock_metadata_model = {} # DataIntgFlowLockMetadata
        data_intg_flow_lock_metadata_model['alive'] = True

        data_intg_flow_lock_model = {} # DataIntgFlowLock
        data_intg_flow_lock_model['entity'] = data_intg_flow_lock_entity_model
        data_intg_flow_lock_model['metadata'] = data_intg_flow_lock_metadata_model

        asset_entity_rov_model = {} # AssetEntityROV
        asset_entity_rov_model['members'] = ['testString']
        asset_entity_rov_model['mode'] = 38

        data_intg_flow_entity_model = {} # DataIntgFlowEntity
        data_intg_flow_entity_model['data_intg_flow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['data_intg_subflow'] = { 'foo': 'bar' }
        data_intg_flow_entity_model['description'] = 'testString'
        data_intg_flow_entity_model['lock'] = data_intg_flow_lock_model
        data_intg_flow_entity_model['name'] = 'testString'
        data_intg_flow_entity_model['rov'] = asset_entity_rov_model
        data_intg_flow_entity_model['sub_type'] = 'testString'

        asset_system_metadata_usage_model = {} # AssetSystemMetadataUsage
        asset_system_metadata_usage_model['access_count'] = 38
        asset_system_metadata_usage_model['last_access_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_accessor_id'] = 'testString'
        asset_system_metadata_usage_model['last_modification_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_usage_model['last_modifier_id'] = 'testString'

        asset_system_metadata_model = {} # AssetSystemMetadata
        asset_system_metadata_model['asset_id'] = 'testString'
        asset_system_metadata_model['asset_type'] = 'testString'
        asset_system_metadata_model['catalog_id'] = 'testString'
        asset_system_metadata_model['create_time'] = "2019-01-01T12:00:00Z"
        asset_system_metadata_model['creator_id'] = 'testString'
        asset_system_metadata_model['description'] = 'testString'
        asset_system_metadata_model['href'] = 'testString'
        asset_system_metadata_model['name'] = 'testString'
        asset_system_metadata_model['origin_country'] = 'testString'
        asset_system_metadata_model['project_id'] = 'testString'
        asset_system_metadata_model['resource_key'] = 'testString'
        asset_system_metadata_model['size'] = 38
        asset_system_metadata_model['source_system'] = {}
        asset_system_metadata_model['tags'] = ['testString']
        asset_system_metadata_model['usage'] = asset_system_metadata_usage_model

        # Construct a json representation of a DataIntgFlowJson model
        data_intg_flow_json_model_json = {}
        data_intg_flow_json_model_json['attachments'] = pipeline_json_model
        data_intg_flow_json_model_json['entity'] = data_intg_flow_entity_model
        data_intg_flow_json_model_json['metadata'] = asset_system_metadata_model

        # Construct a model instance of DataIntgFlowJson by calling from_dict on the json representation
        data_intg_flow_json_model = DataIntgFlowJson.from_dict(data_intg_flow_json_model_json)
        assert data_intg_flow_json_model != False

        # Construct a model instance of DataIntgFlowJson by calling from_dict on the json representation
        data_intg_flow_json_model_dict = DataIntgFlowJson.from_dict(data_intg_flow_json_model_json).__dict__
        data_intg_flow_json_model2 = DataIntgFlowJson(**data_intg_flow_json_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_json_model == data_intg_flow_json_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_json_model_json2 = data_intg_flow_json_model.to_dict()
        assert data_intg_flow_json_model_json2 == data_intg_flow_json_model_json

class DataIntgFlowLockUnitTests():
    """
    Test Class for DataIntgFlowLock
    """

    def test_data_intg_flow_lock_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlowLock
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_intg_flow_lock_entity_model = {} # DataIntgFlowLockEntity
        data_intg_flow_lock_entity_model['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model['requester'] = 'testString'

        data_intg_flow_lock_metadata_model = {} # DataIntgFlowLockMetadata
        data_intg_flow_lock_metadata_model['alive'] = True

        # Construct a json representation of a DataIntgFlowLock model
        data_intg_flow_lock_model_json = {}
        data_intg_flow_lock_model_json['entity'] = data_intg_flow_lock_entity_model
        data_intg_flow_lock_model_json['metadata'] = data_intg_flow_lock_metadata_model

        # Construct a model instance of DataIntgFlowLock by calling from_dict on the json representation
        data_intg_flow_lock_model = DataIntgFlowLock.from_dict(data_intg_flow_lock_model_json)
        assert data_intg_flow_lock_model != False

        # Construct a model instance of DataIntgFlowLock by calling from_dict on the json representation
        data_intg_flow_lock_model_dict = DataIntgFlowLock.from_dict(data_intg_flow_lock_model_json).__dict__
        data_intg_flow_lock_model2 = DataIntgFlowLock(**data_intg_flow_lock_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_lock_model == data_intg_flow_lock_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_lock_model_json2 = data_intg_flow_lock_model.to_dict()
        assert data_intg_flow_lock_model_json2 == data_intg_flow_lock_model_json

class DataIntgFlowLockEntityUnitTests():
    """
    Test Class for DataIntgFlowLockEntity
    """

    def test_data_intg_flow_lock_entity_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlowLockEntity
        """

        # Construct a json representation of a DataIntgFlowLockEntity model
        data_intg_flow_lock_entity_model_json = {}
        data_intg_flow_lock_entity_model_json['data_intg_flow_id'] = 'testString'
        data_intg_flow_lock_entity_model_json['requester'] = 'testString'

        # Construct a model instance of DataIntgFlowLockEntity by calling from_dict on the json representation
        data_intg_flow_lock_entity_model = DataIntgFlowLockEntity.from_dict(data_intg_flow_lock_entity_model_json)
        assert data_intg_flow_lock_entity_model != False

        # Construct a model instance of DataIntgFlowLockEntity by calling from_dict on the json representation
        data_intg_flow_lock_entity_model_dict = DataIntgFlowLockEntity.from_dict(data_intg_flow_lock_entity_model_json).__dict__
        data_intg_flow_lock_entity_model2 = DataIntgFlowLockEntity(**data_intg_flow_lock_entity_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_lock_entity_model == data_intg_flow_lock_entity_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_lock_entity_model_json2 = data_intg_flow_lock_entity_model.to_dict()
        assert data_intg_flow_lock_entity_model_json2 == data_intg_flow_lock_entity_model_json

class DataIntgFlowLockMetadataUnitTests():
    """
    Test Class for DataIntgFlowLockMetadata
    """

    def test_data_intg_flow_lock_metadata_serialization(self):
        """
        Test serialization/deserialization for DataIntgFlowLockMetadata
        """

        # Construct a json representation of a DataIntgFlowLockMetadata model
        data_intg_flow_lock_metadata_model_json = {}
        data_intg_flow_lock_metadata_model_json['alive'] = True

        # Construct a model instance of DataIntgFlowLockMetadata by calling from_dict on the json representation
        data_intg_flow_lock_metadata_model = DataIntgFlowLockMetadata.from_dict(data_intg_flow_lock_metadata_model_json)
        assert data_intg_flow_lock_metadata_model != False

        # Construct a model instance of DataIntgFlowLockMetadata by calling from_dict on the json representation
        data_intg_flow_lock_metadata_model_dict = DataIntgFlowLockMetadata.from_dict(data_intg_flow_lock_metadata_model_json).__dict__
        data_intg_flow_lock_metadata_model2 = DataIntgFlowLockMetadata(**data_intg_flow_lock_metadata_model_dict)

        # Verify the model instances are equivalent
        assert data_intg_flow_lock_metadata_model == data_intg_flow_lock_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        data_intg_flow_lock_metadata_model_json2 = data_intg_flow_lock_metadata_model.to_dict()
        assert data_intg_flow_lock_metadata_model_json2 == data_intg_flow_lock_metadata_model_json

class FlowCompileResponseUnitTests():
    """
    Test Class for FlowCompileResponse
    """

    def test_flow_compile_response_serialization(self):
        """
        Test serialization/deserialization for FlowCompileResponse
        """

        # Construct a json representation of a FlowCompileResponse model
        flow_compile_response_model_json = {}
        flow_compile_response_model_json['message'] = { 'foo': 'bar' }
        flow_compile_response_model_json['type'] = 'testString'

        # Construct a model instance of FlowCompileResponse by calling from_dict on the json representation
        flow_compile_response_model = FlowCompileResponse.from_dict(flow_compile_response_model_json)
        assert flow_compile_response_model != False

        # Construct a model instance of FlowCompileResponse by calling from_dict on the json representation
        flow_compile_response_model_dict = FlowCompileResponse.from_dict(flow_compile_response_model_json).__dict__
        flow_compile_response_model2 = FlowCompileResponse(**flow_compile_response_model_dict)

        # Verify the model instances are equivalent
        assert flow_compile_response_model == flow_compile_response_model2

        # Convert model instance back to dict and verify no loss of data
        flow_compile_response_model_json2 = flow_compile_response_model.to_dict()
        assert flow_compile_response_model_json2 == flow_compile_response_model_json

class HrefModelUnitTests():
    """
    Test Class for HrefModel
    """

    def test_href_model_serialization(self):
        """
        Test serialization/deserialization for HrefModel
        """

        # Construct a json representation of a HrefModel model
        href_model_model_json = {}
        href_model_model_json['href'] = 'testString'

        # Construct a model instance of HrefModel by calling from_dict on the json representation
        href_model_model = HrefModel.from_dict(href_model_model_json)
        assert href_model_model != False

        # Construct a model instance of HrefModel by calling from_dict on the json representation
        href_model_model_dict = HrefModel.from_dict(href_model_model_json).__dict__
        href_model_model2 = HrefModel(**href_model_model_dict)

        # Verify the model instances are equivalent
        assert href_model_model == href_model_model2

        # Convert model instance back to dict and verify no loss of data
        href_model_model_json2 = href_model_model.to_dict()
        assert href_model_model_json2 == href_model_model_json

class ImportCountUnitTests():
    """
    Test Class for ImportCount
    """

    def test_import_count_serialization(self):
        """
        Test serialization/deserialization for ImportCount
        """

        # Construct a json representation of a ImportCount model
        import_count_model_json = {}
        import_count_model_json['connections_total'] = 38
        import_count_model_json['deprecated'] = 38
        import_count_model_json['failed'] = 38
        import_count_model_json['imported'] = 38
        import_count_model_json['parameter_sets_total'] = 38
        import_count_model_json['pending'] = 38
        import_count_model_json['renamed'] = 38
        import_count_model_json['replaced'] = 38
        import_count_model_json['sequence_jobs_total'] = 38
        import_count_model_json['skipped'] = 38
        import_count_model_json['subflows_total'] = 38
        import_count_model_json['table_definitions_total'] = 38
        import_count_model_json['total'] = 38
        import_count_model_json['unsupported'] = 38

        # Construct a model instance of ImportCount by calling from_dict on the json representation
        import_count_model = ImportCount.from_dict(import_count_model_json)
        assert import_count_model != False

        # Construct a model instance of ImportCount by calling from_dict on the json representation
        import_count_model_dict = ImportCount.from_dict(import_count_model_json).__dict__
        import_count_model2 = ImportCount(**import_count_model_dict)

        # Verify the model instances are equivalent
        assert import_count_model == import_count_model2

        # Convert model instance back to dict and verify no loss of data
        import_count_model_json2 = import_count_model.to_dict()
        assert import_count_model_json2 == import_count_model_json

class ImportFlowUnitTests():
    """
    Test Class for ImportFlow
    """

    def test_import_flow_serialization(self):
        """
        Test serialization/deserialization for ImportFlow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_import_error_model = {} # DataImportError
        data_import_error_model['description'] = 'testString'
        data_import_error_model['name'] = 'testString'
        data_import_error_model['stage_type'] = 'testString'
        data_import_error_model['type'] = 'unsupported_stage_type'

        import_flow_warning_model = {} # ImportFlowWarning
        import_flow_warning_model['description'] = 'testString'
        import_flow_warning_model['name'] = 'testString'
        import_flow_warning_model['type'] = 'unreleased_stage_type'

        # Construct a json representation of a ImportFlow model
        import_flow_model_json = {}
        import_flow_model_json['conflict_resolution_status'] = 'import_flow_renamed'
        import_flow_model_json['end_time'] = "2019-01-01T12:00:00Z"
        import_flow_model_json['errors'] = [data_import_error_model]
        import_flow_model_json['id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model_json['job_id'] = 'ccfaaafd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model_json['job_name'] = 'Aggregator12_DataStage_1'
        import_flow_model_json['job_type'] = 'px_job'
        import_flow_model_json['name'] = 'cancel-reservation-job'
        import_flow_model_json['original_name'] = 'cancel-reservation-job'
        import_flow_model_json['ref_asset_id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model_json['status'] = 'completed'
        import_flow_model_json['type'] = 'px_job'
        import_flow_model_json['warnings'] = [import_flow_warning_model]

        # Construct a model instance of ImportFlow by calling from_dict on the json representation
        import_flow_model = ImportFlow.from_dict(import_flow_model_json)
        assert import_flow_model != False

        # Construct a model instance of ImportFlow by calling from_dict on the json representation
        import_flow_model_dict = ImportFlow.from_dict(import_flow_model_json).__dict__
        import_flow_model2 = ImportFlow(**import_flow_model_dict)

        # Verify the model instances are equivalent
        assert import_flow_model == import_flow_model2

        # Convert model instance back to dict and verify no loss of data
        import_flow_model_json2 = import_flow_model.to_dict()
        assert import_flow_model_json2 == import_flow_model_json

class ImportFlowWarningUnitTests():
    """
    Test Class for ImportFlowWarning
    """

    def test_import_flow_warning_serialization(self):
        """
        Test serialization/deserialization for ImportFlowWarning
        """

        # Construct a json representation of a ImportFlowWarning model
        import_flow_warning_model_json = {}
        import_flow_warning_model_json['description'] = 'testString'
        import_flow_warning_model_json['name'] = 'testString'
        import_flow_warning_model_json['type'] = 'unreleased_stage_type'

        # Construct a model instance of ImportFlowWarning by calling from_dict on the json representation
        import_flow_warning_model = ImportFlowWarning.from_dict(import_flow_warning_model_json)
        assert import_flow_warning_model != False

        # Construct a model instance of ImportFlowWarning by calling from_dict on the json representation
        import_flow_warning_model_dict = ImportFlowWarning.from_dict(import_flow_warning_model_json).__dict__
        import_flow_warning_model2 = ImportFlowWarning(**import_flow_warning_model_dict)

        # Verify the model instances are equivalent
        assert import_flow_warning_model == import_flow_warning_model2

        # Convert model instance back to dict and verify no loss of data
        import_flow_warning_model_json2 = import_flow_warning_model.to_dict()
        assert import_flow_warning_model_json2 == import_flow_warning_model_json

class ImportNotificationUnitTests():
    """
    Test Class for ImportNotification
    """

    def test_import_notification_serialization(self):
        """
        Test serialization/deserialization for ImportNotification
        """

        # Construct a json representation of a ImportNotification model
        import_notification_model_json = {}
        import_notification_model_json['created_at'] = "2019-01-01T12:00:00Z"
        import_notification_model_json['id'] = 'testString'
        import_notification_model_json['status'] = 'testString'

        # Construct a model instance of ImportNotification by calling from_dict on the json representation
        import_notification_model = ImportNotification.from_dict(import_notification_model_json)
        assert import_notification_model != False

        # Construct a model instance of ImportNotification by calling from_dict on the json representation
        import_notification_model_dict = ImportNotification.from_dict(import_notification_model_json).__dict__
        import_notification_model2 = ImportNotification(**import_notification_model_dict)

        # Verify the model instances are equivalent
        assert import_notification_model == import_notification_model2

        # Convert model instance back to dict and verify no loss of data
        import_notification_model_json2 = import_notification_model.to_dict()
        assert import_notification_model_json2 == import_notification_model_json

class ImportResponseUnitTests():
    """
    Test Class for ImportResponse
    """

    def test_import_response_serialization(self):
        """
        Test serialization/deserialization for ImportResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_import_error_model = {} # DataImportError
        data_import_error_model['description'] = 'testString'
        data_import_error_model['name'] = 'testString'
        data_import_error_model['stage_type'] = 'testString'
        data_import_error_model['type'] = 'unsupported_stage_type'

        import_flow_warning_model = {} # ImportFlowWarning
        import_flow_warning_model['description'] = 'testString'
        import_flow_warning_model['name'] = 'testString'
        import_flow_warning_model['type'] = 'unreleased_stage_type'

        import_flow_model = {} # ImportFlow
        import_flow_model['conflict_resolution_status'] = 'import_flow_renamed'
        import_flow_model['end_time'] = "2019-01-01T12:00:00Z"
        import_flow_model['errors'] = [data_import_error_model]
        import_flow_model['id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['job_id'] = 'ccfaaafd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['job_name'] = 'Aggregator12_DataStage_1'
        import_flow_model['job_type'] = 'px_job'
        import_flow_model['name'] = 'cancel-reservation-job'
        import_flow_model['original_name'] = 'cancel-reservation-job'
        import_flow_model['ref_asset_id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['status'] = 'completed'
        import_flow_model['type'] = 'px_job'
        import_flow_model['warnings'] = [import_flow_warning_model]

        import_notification_model = {} # ImportNotification
        import_notification_model['created_at'] = "2019-01-01T12:00:00Z"
        import_notification_model['id'] = 'testString'
        import_notification_model['status'] = 'testString'

        import_count_model = {} # ImportCount
        import_count_model['connections_total'] = 38
        import_count_model['deprecated'] = 38
        import_count_model['failed'] = 38
        import_count_model['imported'] = 38
        import_count_model['parameter_sets_total'] = 38
        import_count_model['pending'] = 38
        import_count_model['renamed'] = 38
        import_count_model['replaced'] = 38
        import_count_model['sequence_jobs_total'] = 38
        import_count_model['skipped'] = 38
        import_count_model['subflows_total'] = 38
        import_count_model['table_definitions_total'] = 38
        import_count_model['total'] = 38
        import_count_model['unsupported'] = 38

        import_response_entity_model = {} # ImportResponseEntity
        import_response_entity_model['cancelled_by'] = 'user1@company1.com'
        import_response_entity_model['conflict_resolution'] = 'testString'
        import_response_entity_model['end_time'] = "2019-01-01T12:00:00Z"
        import_response_entity_model['import_data_flows'] = [import_flow_model]
        import_response_entity_model['name'] = 'seat-reservation-jobs'
        import_response_entity_model['notifications'] = [import_notification_model]
        import_response_entity_model['on_failure'] = 'testString'
        import_response_entity_model['remaining_time'] = 38
        import_response_entity_model['start_time'] = "2019-01-01T12:00:00Z"
        import_response_entity_model['status'] = 'in_progress'
        import_response_entity_model['tally'] = import_count_model

        import_response_metadata_model = {} # ImportResponseMetadata
        import_response_metadata_model['catalog_id'] = 'testString'
        import_response_metadata_model['created_at'] = "2019-01-01T12:00:00Z"
        import_response_metadata_model['created_by'] = 'user1@company1.com'
        import_response_metadata_model['id'] = 'testString'
        import_response_metadata_model['modified_at'] = "2019-01-01T12:00:00Z"
        import_response_metadata_model['name'] = 'testString'
        import_response_metadata_model['project_id'] = 'testString'
        import_response_metadata_model['project_name'] = 'testString'
        import_response_metadata_model['url'] = 'testString'

        # Construct a json representation of a ImportResponse model
        import_response_model_json = {}
        import_response_model_json['entity'] = import_response_entity_model
        import_response_model_json['metadata'] = import_response_metadata_model

        # Construct a model instance of ImportResponse by calling from_dict on the json representation
        import_response_model = ImportResponse.from_dict(import_response_model_json)
        assert import_response_model != False

        # Construct a model instance of ImportResponse by calling from_dict on the json representation
        import_response_model_dict = ImportResponse.from_dict(import_response_model_json).__dict__
        import_response_model2 = ImportResponse(**import_response_model_dict)

        # Verify the model instances are equivalent
        assert import_response_model == import_response_model2

        # Convert model instance back to dict and verify no loss of data
        import_response_model_json2 = import_response_model.to_dict()
        assert import_response_model_json2 == import_response_model_json

class ImportResponseEntityUnitTests():
    """
    Test Class for ImportResponseEntity
    """

    def test_import_response_entity_serialization(self):
        """
        Test serialization/deserialization for ImportResponseEntity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        data_import_error_model = {} # DataImportError
        data_import_error_model['description'] = 'testString'
        data_import_error_model['name'] = 'testString'
        data_import_error_model['stage_type'] = 'testString'
        data_import_error_model['type'] = 'unsupported_stage_type'

        import_flow_warning_model = {} # ImportFlowWarning
        import_flow_warning_model['description'] = 'testString'
        import_flow_warning_model['name'] = 'testString'
        import_flow_warning_model['type'] = 'unreleased_stage_type'

        import_flow_model = {} # ImportFlow
        import_flow_model['conflict_resolution_status'] = 'import_flow_renamed'
        import_flow_model['end_time'] = "2019-01-01T12:00:00Z"
        import_flow_model['errors'] = [data_import_error_model]
        import_flow_model['id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['job_id'] = 'ccfaaafd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['job_name'] = 'Aggregator12_DataStage_1'
        import_flow_model['job_type'] = 'px_job'
        import_flow_model['name'] = 'cancel-reservation-job'
        import_flow_model['original_name'] = 'cancel-reservation-job'
        import_flow_model['ref_asset_id'] = 'ccfdbbfd-810d-4f0e-b0a9-228c328a0136'
        import_flow_model['status'] = 'completed'
        import_flow_model['type'] = 'px_job'
        import_flow_model['warnings'] = [import_flow_warning_model]

        import_notification_model = {} # ImportNotification
        import_notification_model['created_at'] = "2019-01-01T12:00:00Z"
        import_notification_model['id'] = 'testString'
        import_notification_model['status'] = 'testString'

        import_count_model = {} # ImportCount
        import_count_model['connections_total'] = 38
        import_count_model['deprecated'] = 38
        import_count_model['failed'] = 38
        import_count_model['imported'] = 38
        import_count_model['parameter_sets_total'] = 38
        import_count_model['pending'] = 38
        import_count_model['renamed'] = 38
        import_count_model['replaced'] = 38
        import_count_model['sequence_jobs_total'] = 38
        import_count_model['skipped'] = 38
        import_count_model['subflows_total'] = 38
        import_count_model['table_definitions_total'] = 38
        import_count_model['total'] = 38
        import_count_model['unsupported'] = 38

        # Construct a json representation of a ImportResponseEntity model
        import_response_entity_model_json = {}
        import_response_entity_model_json['cancelled_by'] = 'user1@company1.com'
        import_response_entity_model_json['conflict_resolution'] = 'testString'
        import_response_entity_model_json['end_time'] = "2019-01-01T12:00:00Z"
        import_response_entity_model_json['import_data_flows'] = [import_flow_model]
        import_response_entity_model_json['name'] = 'seat-reservation-jobs'
        import_response_entity_model_json['notifications'] = [import_notification_model]
        import_response_entity_model_json['on_failure'] = 'testString'
        import_response_entity_model_json['remaining_time'] = 38
        import_response_entity_model_json['start_time'] = "2019-01-01T12:00:00Z"
        import_response_entity_model_json['status'] = 'in_progress'
        import_response_entity_model_json['tally'] = import_count_model

        # Construct a model instance of ImportResponseEntity by calling from_dict on the json representation
        import_response_entity_model = ImportResponseEntity.from_dict(import_response_entity_model_json)
        assert import_response_entity_model != False

        # Construct a model instance of ImportResponseEntity by calling from_dict on the json representation
        import_response_entity_model_dict = ImportResponseEntity.from_dict(import_response_entity_model_json).__dict__
        import_response_entity_model2 = ImportResponseEntity(**import_response_entity_model_dict)

        # Verify the model instances are equivalent
        assert import_response_entity_model == import_response_entity_model2

        # Convert model instance back to dict and verify no loss of data
        import_response_entity_model_json2 = import_response_entity_model.to_dict()
        assert import_response_entity_model_json2 == import_response_entity_model_json

class ImportResponseMetadataUnitTests():
    """
    Test Class for ImportResponseMetadata
    """

    def test_import_response_metadata_serialization(self):
        """
        Test serialization/deserialization for ImportResponseMetadata
        """

        # Construct a json representation of a ImportResponseMetadata model
        import_response_metadata_model_json = {}
        import_response_metadata_model_json['catalog_id'] = 'testString'
        import_response_metadata_model_json['created_at'] = "2019-01-01T12:00:00Z"
        import_response_metadata_model_json['created_by'] = 'user1@company1.com'
        import_response_metadata_model_json['id'] = 'testString'
        import_response_metadata_model_json['modified_at'] = "2019-01-01T12:00:00Z"
        import_response_metadata_model_json['name'] = 'testString'
        import_response_metadata_model_json['project_id'] = 'testString'
        import_response_metadata_model_json['project_name'] = 'testString'
        import_response_metadata_model_json['url'] = 'testString'

        # Construct a model instance of ImportResponseMetadata by calling from_dict on the json representation
        import_response_metadata_model = ImportResponseMetadata.from_dict(import_response_metadata_model_json)
        assert import_response_metadata_model != False

        # Construct a model instance of ImportResponseMetadata by calling from_dict on the json representation
        import_response_metadata_model_dict = ImportResponseMetadata.from_dict(import_response_metadata_model_json).__dict__
        import_response_metadata_model2 = ImportResponseMetadata(**import_response_metadata_model_dict)

        # Verify the model instances are equivalent
        assert import_response_metadata_model == import_response_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        import_response_metadata_model_json2 = import_response_metadata_model.to_dict()
        assert import_response_metadata_model_json2 == import_response_metadata_model_json

class PipelineJsonUnitTests():
    """
    Test Class for PipelineJson
    """

    def test_pipeline_json_serialization(self):
        """
        Test serialization/deserialization for PipelineJson
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pipelines_model = {} # Pipelines
        pipelines_model['app_data'] = { 'foo': 'bar' }
        pipelines_model['description'] = 'A test DataStage flow.'
        pipelines_model['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model['name'] = 'ContainerC1'
        pipelines_model['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model['runtime_ref'] = 'pxOsh'

        # Construct a json representation of a PipelineJson model
        pipeline_json_model_json = {}
        pipeline_json_model_json['app_data'] = { 'foo': 'bar' }
        pipeline_json_model_json['doc_type'] = 'pipeline'
        pipeline_json_model_json['external_paramsets'] = [{'name':'Test Param Set', 'project_ref':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57'}]
        pipeline_json_model_json['id'] = '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff'
        pipeline_json_model_json['json_schema'] = 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json'
        pipeline_json_model_json['parameters'] = { 'foo': 'bar' }
        pipeline_json_model_json['pipelines'] = [pipelines_model]
        pipeline_json_model_json['primary_pipeline'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipeline_json_model_json['runtimes'] = [{'id':'pxOsh', 'name':'pxOsh'}]
        pipeline_json_model_json['schemas'] = [{'fields':[{'app_data':{'is_unicode_string':False, 'odbc_type':'INTEGER', 'type_code':'INT32'}, 'metadata':{'decimal_precision':6, 'decimal_scale':0, 'is_key':False, 'is_signed':False, 'item_index':0, 'max_length':6, 'min_length':0}, 'name':'ID', 'nullable':False, 'type':'integer'}], 'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}]
        pipeline_json_model_json['version'] = '3.0'

        # Construct a model instance of PipelineJson by calling from_dict on the json representation
        pipeline_json_model = PipelineJson.from_dict(pipeline_json_model_json)
        assert pipeline_json_model != False

        # Construct a model instance of PipelineJson by calling from_dict on the json representation
        pipeline_json_model_dict = PipelineJson.from_dict(pipeline_json_model_json).__dict__
        pipeline_json_model2 = PipelineJson(**pipeline_json_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_json_model == pipeline_json_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_json_model_json2 = pipeline_json_model.to_dict()
        assert pipeline_json_model_json2 == pipeline_json_model_json

class PipelinesUnitTests():
    """
    Test Class for Pipelines
    """

    def test_pipelines_serialization(self):
        """
        Test serialization/deserialization for Pipelines
        """

        # Construct a json representation of a Pipelines model
        pipelines_model_json = {}
        pipelines_model_json['app_data'] = { 'foo': 'bar' }
        pipelines_model_json['description'] = 'A test DataStage flow.'
        pipelines_model_json['id'] = 'fa1b859a-d592-474d-b56c-2137e4efa4bc'
        pipelines_model_json['name'] = 'ContainerC1'
        pipelines_model_json['nodes'] = [{'app_data':{'ui_data':{'description':'Produce a set of mock data based on the specified metadata', 'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'label':'Row_Generator_1', 'x_pos':108, 'y_pos':162}}, 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'op':'PxRowGenerator', 'outputs':[{'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'parameters':{'records':10}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'parameters':{'input_count':0, 'output_count':1}, 'type':'binding'}, {'app_data':{'ui_data':{'description':'Print row column values to either the job log or to a separate output link', 'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'label':'Peek_1', 'x_pos':342, 'y_pos':162}}, 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'inputs':[{'app_data':{'ui_data':{'label':'inPort'}}, 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'links':[{'app_data':{'ui_data':{'decorations':[{'class_name':'', 'hotspot':False, 'id':'Link_1', 'label':'Link_1', 'outline':True, 'path':'', 'position':'middle'}]}}, 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'link_name':'Link_1', 'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'type_attr':'PRIMARY'}], 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'op':'PxPeek', 'outputs':[{'app_data':{'ui_data':{'label':'outPort'}}, 'id':''}], 'parameters':{'all':' ', 'columns':' ', 'dataset':' ', 'input_count':1, 'name':'name', 'nrecs':10, 'output_count':0, 'selection':' '}, 'type':'execution_node'}]
        pipelines_model_json['runtime_ref'] = 'pxOsh'

        # Construct a model instance of Pipelines by calling from_dict on the json representation
        pipelines_model = Pipelines.from_dict(pipelines_model_json)
        assert pipelines_model != False

        # Construct a model instance of Pipelines by calling from_dict on the json representation
        pipelines_model_dict = Pipelines.from_dict(pipelines_model_json).__dict__
        pipelines_model2 = Pipelines(**pipelines_model_dict)

        # Verify the model instances are equivalent
        assert pipelines_model == pipelines_model2

        # Convert model instance back to dict and verify no loss of data
        pipelines_model_json2 = pipelines_model.to_dict()
        assert pipelines_model_json2 == pipelines_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
