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
Integration Tests for DatastageV3
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from datastage.datastage_v3 import *
from pathlib import Path

# Config file name
config_file = 'datastage_v3.env'

class TestDatastageV3():
    """
    Integration Test Class for DatastageV3
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.datastage_service = DatastageV3.new_instance(
                )
            assert cls.datastage_service is not None

            cls.config = read_external_sources(
                DatastageV3.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_datastage_flows_list(self):

        datastage_flows_list_response = self.datastage_service.datastage_flows_list(
            project_id=self.config['PROJECT_ID'],
            limit=100
        )

        assert datastage_flows_list_response.get_status_code() == 200
        data_flow_paged_collection = datastage_flows_list_response.get_result()
        assert data_flow_paged_collection is not None

    @needscredentials
    def test_datastage_flows_create(self):

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createdDataFlowId = data_intg_flow['metadata']['asset_id']
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

    @needscredentials
    def test_datastage_flows_get(self):

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createdDataFlowId = data_intg_flow['metadata']['asset_id']

        datastage_flows_get_response = self.datastage_service.datastage_flows_get(
            data_intg_flow_id=createdDataFlowId,
            project_id=self.config['PROJECT_ID']
        )

        assert datastage_flows_get_response.get_status_code() == 200
        data_intg_flow = datastage_flows_get_response.get_result()
        assert data_intg_flow is not None
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

    @needscredentials
    def test_datastage_flows_update(self):

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createdDataFlowId = data_intg_flow['metadata']['asset_id']
        
        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_update_response = self.datastage_service.datastage_flows_update(
            data_intg_flow_id=createdDataFlowId,
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID']
        )

        assert datastage_flows_update_response.get_status_code() == 201
        data_intg_flow = datastage_flows_update_response.get_result()
        assert data_intg_flow is not None
        
        updatedDataFlowId = data_intg_flow['metadata']['asset_id']
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

    @needscredentials
    def test_datastage_flows_clone(self):

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createdDataFlowId = data_intg_flow['metadata']['asset_id']
        
        datastage_flows_clone_response = self.datastage_service.datastage_flows_clone(
            data_intg_flow_id=createdDataFlowId,
            project_id=self.config['PROJECT_ID']
        )

        assert datastage_flows_clone_response.get_status_code() == 200
        data_intg_flow = datastage_flows_clone_response.get_result()
        assert data_intg_flow is not None
        
        cloneDataFlowId = data_intg_flow['metadata']['asset_id']
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=cloneDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

    @needscredentials
    def test_datastage_flows_compile(self):

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createdDataFlowId = data_intg_flow['metadata']['asset_id']

        datastage_flows_compile_response = self.datastage_service.datastage_flows_compile(
            data_intg_flow_id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            runtime_type='dspxOsh'
        )

        assert datastage_flows_compile_response.get_status_code() == 200
        flow_compile_response = datastage_flows_compile_response.get_result()
        assert flow_compile_response is not None
        
        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createdDataFlowId,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

    @needscredentials
    def test_migration_create(self):

        migration_create_response = self.datastage_service.migration_create(
            body=open(Path(__file__).parent / '../../testInput/rowgen_peek.isx', "rb").read(),
            project_id=self.config['PROJECT_ID'],
            on_failure='continue',
            conflict_resolution='rename',
            attachment_type='isx',
            file_name='rowgen_peek.isx'
        )

        assert migration_create_response.get_status_code() == 202
        import_response = migration_create_response.get_result()
        assert import_response is not None
        
        importId = import_response['metadata']['id']
        
        migration_delete_response = self.datastage_service.migration_delete(
            import_id=importId,
            project_id=self.config['PROJECT_ID']
        )

        assert migration_delete_response.get_status_code() == 202

    @needscredentials
    def test_migration_get(self):
    
        migration_create_response = self.datastage_service.migration_create(
            body=open(Path(__file__).parent / '../../testInput/rowgen_peek.isx', "rb").read(),
            project_id=self.config['PROJECT_ID'],
            on_failure='continue',
            conflict_resolution='rename',
            attachment_type='isx',
            file_name='rowgen_peek.isx'
        )

        assert migration_create_response.get_status_code() == 202
        import_response = migration_create_response.get_result()
        assert import_response is not None
        
        importId = import_response['metadata']['id']

        migration_get_response = self.datastage_service.migration_get(
            import_id=importId,
            project_id=self.config['PROJECT_ID']
        )

        assert migration_get_response.get_status_code() == 200
        import_response = migration_get_response.get_result()
        assert import_response is not None
        
        migration_delete_response = self.datastage_service.migration_delete(
            import_id=importId,
            project_id=self.config['PROJECT_ID']
        )

        assert migration_delete_response.get_status_code() == 202

    @needscredentials
    def test_migration_delete(self):
    
        migration_create_response = self.datastage_service.migration_create(
            body=open(Path(__file__).parent / '../../testInput/rowgen_peek.isx', "rb").read(),
            project_id=self.config['PROJECT_ID'],
            on_failure='continue',
            conflict_resolution='rename',
            attachment_type='isx',
            file_name='rowgen_peek.isx'
        )

        assert migration_create_response.get_status_code() == 202
        import_response = migration_create_response.get_result()
        assert import_response is not None
        
        importId = import_response['metadata']['id']

        migration_delete_response = self.datastage_service.migration_delete(
            import_id=importId,
            project_id=self.config['PROJECT_ID']
        )

        assert migration_delete_response.get_status_code() == 202

    @needscredentials
    def test_datastage_flows_delete(self):
    
        createDataFlowIds = []

        # Construct a dict representation of a Pipelines model
        pipelines_model = {
            'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'description': 'A test DataStage flow',
            'runtime_ref': 'pxOsh',
            'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
            'app_data': { 'foo': 'bar' }
        }

        # Construct a dict representation of a PipelineJson model
        pipeline_json_model = {
            'doc_type': 'pipeline',
            'version': '3.0',
            'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
            'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
            'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
            'pipelines': [pipelines_model],
            'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
            'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
            'app_data': { 'foo': 'bar' },
            'parameters': { 'foo': 'bar' },
            'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
        }

        datastage_flows_create_response = self.datastage_service.datastage_flows_create(
            data_intg_flow_name='testCreatFlowSDKJob',
            pipeline_flows=pipeline_json_model,
            project_id=self.config['PROJECT_ID'],
            asset_category='system'
        )

        assert datastage_flows_create_response.get_status_code() == 201
        data_intg_flow = datastage_flows_create_response.get_result()
        assert data_intg_flow is not None
        
        createDataFlowIds.append(data_intg_flow['metadata']['asset_id'])
        
        datastage_flows_clone_response = self.datastage_service.datastage_flows_clone(
            data_intg_flow_id=createDataFlowIds[0],
            project_id=self.config['PROJECT_ID']
        )

        assert datastage_flows_clone_response.get_status_code() == 200
        data_intg_flow = datastage_flows_clone_response.get_result()
        assert data_intg_flow is not None
        
        createDataFlowIds.append(data_intg_flow['metadata']['asset_id'])

        datastage_flows_delete_response = self.datastage_service.datastage_flows_delete(
            id=createDataFlowIds,
            project_id=self.config['PROJECT_ID'],
            force=True
        )

        assert datastage_flows_delete_response.get_status_code() == 204

