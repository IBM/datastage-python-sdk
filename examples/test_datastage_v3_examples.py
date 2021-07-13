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
Examples for DatastageV3
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from pathlib import Path
import traceback
import datetime
import time
from datastage.datastage_v3 import *

#
# This file provides an example of how to use the datastage service.
#
# The following configuration properties are assumed to be defined:
# DATASTAGE_URL=<service base url>
# DATASTAGE_AUTH_TYPE=iam
# DATASTAGE_APIKEY=<IAM apikey>
# DATASTAGE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'credentials.env'
custome_service_name = 'EXAMPLE_SERVICE_NAME'

datastage_service = None

config = None



##############################################################################
# Pipeline models
##############################################################################

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

# Construct an updated dict representation of a Pipelines model
updated_pipelines_model = {
    'id': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
    'description': 'An updated test DataStage flow',
    'runtime_ref': 'pxOsh',
    'nodes': [{'outputs':[{'id':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d', 'app_data':{'datastage':{'is_source_of_link':'73a5fb2c-f499-4c75-a8a7-71cea90f5105'}, 'ui_data':{'label':'outPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'parameters':{'records':10}}], 'op':'PxRowGenerator', 'id':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type':'binding', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxRowGenerator.svg', 'description':'Produce a set of mock data based on the specified metadata', 'x_pos':108, 'label':'Row_Generator_1', 'y_pos':162}}, 'parameters':{'output_count':1, 'input_count':0}}, {'outputs':[{'id':'', 'app_data':{'ui_data':{'label':'outPort'}}}], 'op':'PxPeek', 'inputs':[{'links':[{'node_id_ref':'9fc2ec49-87ed-49c7-bdfc-abb06a46af37', 'type_attr':'PRIMARY', 'id':'73a5fb2c-f499-4c75-a8a7-71cea90f5105', 'app_data':{'ui_data':{'decorations':[{'path':'', 'outline':True, 'hotspot':False, 'id':'Link_1', 'position':'middle', 'label':'Link_1', 'class_name':''}]}}, 'link_name':'Link_1', 'port_id_ref':'3d01fe66-e675-4e7f-ad7b-3ba9a9cff30d'}], 'id':'c4195b34-8b4a-473f-b987-fa6d028f3968', 'app_data':{'ui_data':{'label':'inPort'}}, 'schema_ref':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d'}], 'id':'4195b012-d3e7-4f74-8099-e7b23ec6ebb9', 'type':'execution_node', 'app_data':{'ui_data':{'image':'/data-intg/flows/graphics/palette/PxPeek.svg', 'description':'Print row column values to either the job log or to a separate output link', 'x_pos':342, 'label':'Peek_1', 'y_pos':162}}, 'parameters':{'all':' ', 'columns':' ', 'nrecs':10, 'selection':' ', 'output_count':0, 'input_count':1, 'name':'name', 'dataset':' '}}],
    'app_data': { 'foo': 'bar' }
}

# Construct an updated dict representation of a PipelineJson model
updated_pipeline_json_model = {
    'doc_type': 'pipeline',
    'version': '3.0',
    'json_schema': 'http://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
    'id': '84c2b6fb-1dd5-4114-b4ba-9bb2cb364fff',
    'primary_pipeline': 'fa1b859a-d592-474d-b56c-2137e4efa4bc',
    'pipelines': [updated_pipelines_model],
    'schemas': [{'id':'0e04b1b8-60c2-4b36-bae6-d0c7ae03dd8d', 'fields':[{'metadata':{'item_index':0, 'is_key':False, 'min_length':0, 'decimal_scale':0, 'decimal_precision':6, 'max_length':6, 'is_signed':False}, 'nullable':False, 'name':'ID', 'app_data':{'odbc_type':'INTEGER', 'is_unicode_string':False, 'type_code':'INT32'}, 'type':'integer'}]}],
    'runtimes': [{'name':'pxOsh', 'id':'pxOsh'}],
    'app_data': { 'foo': 'bar' },
    'parameters': { 'foo': 'bar' },
    'external_paramsets': [{'name':'Test Param Set', 'ref':'eeabf991-b69e-4f8c-b9f1-e6f2129b9a57', 'project_id':'bd0dbbfd-810d-4f0e-b0a9-228c328a8e23'}]
}

# Construct a dict representation of a Pipelines model for subflow
subflow_pipelines_model = {
    'id': 'b2456f91-568b-4bbb-bfa2-6d9dbd7838b8',
    'runtime_ref': 'pxOsh',
    'nodes': [{"outputs":[{"id":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd","app_data":{"datastage":{"is_source_of_link":"db6e0275-4c3f-41dd-804f-77c273b53c2b"},"ui_data":{"label":"outPort"}},"schema_ref":"606d83c4-c340-46db-802c-13eb4cdc5404"}],"id":"9bb04a97-0892-4116-b1bb-98cb5da36033","type":"binding","app_data":{"datastage":{"outputs_order":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd"},"ui_data":{"image":"","x_pos":48,"label":"Entrynode1","y_pos":48}}},{"outputs":[{"id":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2","app_data":{"datastage":{"is_source_of_link":"95daf7c5-41c0-45d6-a105-833709fbcbd6"},"ui_data":{"label":"outPort"}},"schema_ref":"33148a26-7d86-41bf-9d95-b865d184e926"}],"op":"PxSort","inputs":[{"links":[{"node_id_ref":"9bb04a97-0892-4116-b1bb-98cb5da36033","type_attr":"PRIMARY","id":"db6e0275-4c3f-41dd-804f-77c273b53c2b","link_name":"DSLink1B","app_data":{"datastage":{},"ui_data":{"decorations":[{"path":"","outline":True,"hotspot":False,"id":"DSLink1B","label":"DSLink1B","position":"middle","class_name":""}]}},"port_id_ref":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd"}],"id":"80a55420-a8c4-4d3d-8911-b26fa49065bb","app_data":{"datastage":{},"ui_data":{"label":"inPort"}},"parameters":{"runtime_column_propagation":0},"schema_ref":"606d83c4-c340-46db-802c-13eb4cdc5404"}],"id":"9ff15aa6-d018-4a83-b592-c9f5fdac575b","type":"execution_node","app_data":{"datastage":{"inputs_order":"80a55420-a8c4-4d3d-8911-b26fa49065bb","outputs_order":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2"},"ui_data":{"image":"../graphics/palette/PxSort.svg","x_pos":216,"label":"Sort_2","y_pos":48}},"parameters":{"keyProperties":[{"sorted-clustered":"","asc-desc":"asc","key":"col1"}],"output_count":1,"stats":"","input_count":1,"stable":"stable","unique":"","flagCluster":"","allow_column_mapping":False,"operator":"tsort","flagKey":""}},{"inputs":[{"links":[{"node_id_ref":"9ff15aa6-d018-4a83-b592-c9f5fdac575b","type_attr":"PRIMARY","id":"95daf7c5-41c0-45d6-a105-833709fbcbd6","link_name":"DSLink2B","app_data":{"datastage":{},"ui_data":{"decorations":[{"path":"","outline":True,"hotspot":False,"id":"DSLink2B","label":"DSLink2B","position":"middle","class_name":""}]}},"port_id_ref":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2"}],"id":"20415ae4-4b75-400a-b183-0f52241e32e3","app_data":{"datastage":{},"ui_data":{"label":"inPort"}},"schema_ref":"33148a26-7d86-41bf-9d95-b865d184e926"}],"id":"535afa26-96a0-401a-93f2-6e79e8dc4ded","type":"binding","app_data":{"datastage":{"inputs_order":"20415ae4-4b75-400a-b183-0f52241e32e3"},"ui_data":{"image":"","x_pos":384,"label":"Exitnode1","y_pos":48}}}],
    'app_data': {"datastage":{"runtimecolumnpropagation":"true"},"ui_data":{"comments":[]}}
}

# Construct a dict representation of a PipelineJson model for subflow
subflow_pipeline_json_model = {
    'doc_type': 'subpipeline',
    'version': '3.0',
    'json_schema': 'https://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
    'id': '0059f0ed-7069-4571-b367-50884268c14b',
    'primary_pipeline': 'b2456f91-568b-4bbb-bfa2-6d9dbd7838b8',
    'pipelines': [subflow_pipelines_model],
    'schemas': [{"id":"606d83c4-c340-46db-802c-13eb4cdc5404","fields":[{"metadata":{"item_index":0,"is_key":True,"min_length":0,"decimal_scale":0,"decimal_precision":0,"max_length":0,"is_signed":True},"nullable":False,"name":"col1","type":"integer","app_data":{"column_reference":"col1","odbc_type":"INTEGER","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"INT32"}},{"metadata":{"item_index":0,"is_key":False,"min_length":5,"decimal_scale":0,"decimal_precision":0,"max_length":5,"is_signed":False},"nullable":False,"name":"col2","type":"string","app_data":{"column_reference":"col2","odbc_type":"CHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}},{"metadata":{"item_index":0,"is_key":False,"min_length":0,"decimal_scale":0,"decimal_precision":0,"max_length":10,"is_signed":False},"nullable":False,"name":"col3","type":"string","app_data":{"column_reference":"col3","odbc_type":"VARCHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}}]},{"id":"33148a26-7d86-41bf-9d95-b865d184e926","fields":[{"metadata":{"item_index":0,"is_key":True,"min_length":0,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col1","max_length":0,"is_signed":True},"nullable":False,"name":"col1","type":"integer","app_data":{"column_reference":"col1","odbc_type":"INTEGER","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"INT32"}},{"metadata":{"item_index":0,"is_key":False,"min_length":5,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col2","max_length":5,"is_signed":False},"nullable":False,"name":"col2","type":"string","app_data":{"column_reference":"col2","odbc_type":"CHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}},{"metadata":{"item_index":0,"is_key":False,"min_length":0,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col3","max_length":10,"is_signed":False},"nullable":False,"name":"col3","type":"string","app_data":{"column_reference":"col3","odbc_type":"VARCHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}}]}],
    'runtimes': [{"name":"pxOsh","id":"pxOsh"}],
    'app_data': {"datastage":{"version":"3.0.2"}}
}

# Construct a dict representation of a Pipelines model
updated_subflow_pipelines_model = {
    'id': 'b2456f91-568b-4bbb-bfa2-6d9dbd7838b8',
    'runtime_ref': 'pxOsh',
    'nodes': [{"outputs":[{"id":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd","app_data":{"datastage":{"is_source_of_link":"db6e0275-4c3f-41dd-804f-77c273b53c2b"},"ui_data":{"label":"outPort"}},"schema_ref":"606d83c4-c340-46db-802c-13eb4cdc5404"}],"id":"9bb04a97-0892-4116-b1bb-98cb5da36033","type":"binding","app_data":{"datastage":{"outputs_order":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd"},"ui_data":{"image":"","x_pos":48,"label":"Entrynode1","y_pos":48}}},{"outputs":[{"id":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2","app_data":{"datastage":{"is_source_of_link":"95daf7c5-41c0-45d6-a105-833709fbcbd6"},"ui_data":{"label":"outPort"}},"schema_ref":"33148a26-7d86-41bf-9d95-b865d184e926"}],"op":"PxSort","inputs":[{"links":[{"node_id_ref":"9bb04a97-0892-4116-b1bb-98cb5da36033","type_attr":"PRIMARY","id":"db6e0275-4c3f-41dd-804f-77c273b53c2b","link_name":"DSLink1B","app_data":{"datastage":{},"ui_data":{"decorations":[{"path":"","outline":True,"hotspot":False,"id":"DSLink1B","label":"DSLink1B","position":"middle","class_name":""}]}},"port_id_ref":"23933e70-1408-4f0f-bf7a-e00cb09fa5bd"}],"id":"80a55420-a8c4-4d3d-8911-b26fa49065bb","app_data":{"datastage":{},"ui_data":{"label":"inPort"}},"parameters":{"runtime_column_propagation":0},"schema_ref":"606d83c4-c340-46db-802c-13eb4cdc5404"}],"id":"9ff15aa6-d018-4a83-b592-c9f5fdac575b","type":"execution_node","app_data":{"datastage":{"inputs_order":"80a55420-a8c4-4d3d-8911-b26fa49065bb","outputs_order":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2"},"ui_data":{"image":"../graphics/palette/PxSort.svg","x_pos":216,"label":"Sort_2","y_pos":48}},"parameters":{"keyProperties":[{"sorted-clustered":"","asc-desc":"desc","key":"col1"}],"output_count":1,"stats":"","input_count":1,"stable":"stable","unique":"","flagCluster":"","allow_column_mapping":False,"operator":"tsort","flagKey":""}},{"inputs":[{"links":[{"node_id_ref":"9ff15aa6-d018-4a83-b592-c9f5fdac575b","type_attr":"PRIMARY","id":"95daf7c5-41c0-45d6-a105-833709fbcbd6","link_name":"DSLink2B","app_data":{"datastage":{},"ui_data":{"decorations":[{"path":"","outline":True,"hotspot":False,"id":"DSLink2B","label":"DSLink2B","position":"middle","class_name":""}]}},"port_id_ref":"3c6edc1d-da25-44cb-b80c-f6f216a8a6f2"}],"id":"20415ae4-4b75-400a-b183-0f52241e32e3","app_data":{"datastage":{},"ui_data":{"label":"inPort"}},"schema_ref":"33148a26-7d86-41bf-9d95-b865d184e926"}],"id":"535afa26-96a0-401a-93f2-6e79e8dc4ded","type":"binding","app_data":{"datastage":{"inputs_order":"20415ae4-4b75-400a-b183-0f52241e32e3"},"ui_data":{"image":"","x_pos":384,"label":"Exitnode1","y_pos":48}}}],
    'app_data': {"datastage":{"runtimecolumnpropagation":"true"},"ui_data":{"comments":[]}}
}

# Construct a dict representation of a PipelineJson model
updated_subflow_pipeline_json_model = {
    'doc_type': 'subpipeline',
    'version': '3.0',
    'json_schema': 'https://api.dataplatform.ibm.com/schemas/common-pipeline/pipeline-flow/pipeline-flow-v3-schema.json',
    'id': '0059f0ed-7069-4571-b367-50884268c14b',
    'primary_pipeline': 'b2456f91-568b-4bbb-bfa2-6d9dbd7838b8',
    'pipelines': [updated_subflow_pipelines_model],
    'schemas': [{"id":"606d83c4-c340-46db-802c-13eb4cdc5404","fields":[{"metadata":{"item_index":0,"is_key":True,"min_length":0,"decimal_scale":0,"decimal_precision":0,"max_length":0,"is_signed":True},"nullable":False,"name":"col1","type":"integer","app_data":{"column_reference":"col1","odbc_type":"INTEGER","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"INT32"}},{"metadata":{"item_index":0,"is_key":False,"min_length":5,"decimal_scale":0,"decimal_precision":0,"max_length":5,"is_signed":False},"nullable":False,"name":"col2","type":"string","app_data":{"column_reference":"col2","odbc_type":"CHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}},{"metadata":{"item_index":0,"is_key":False,"min_length":0,"decimal_scale":0,"decimal_precision":0,"max_length":10,"is_signed":False},"nullable":False,"name":"col3","type":"string","app_data":{"column_reference":"col3","odbc_type":"VARCHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}}]},{"id":"33148a26-7d86-41bf-9d95-b865d184e926","fields":[{"metadata":{"item_index":0,"is_key":True,"min_length":0,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col1","max_length":0,"is_signed":True},"nullable":False,"name":"col1","type":"integer","app_data":{"column_reference":"col1","odbc_type":"INTEGER","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"INT32"}},{"metadata":{"item_index":0,"is_key":False,"min_length":5,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col2","max_length":5,"is_signed":False},"nullable":False,"name":"col2","type":"string","app_data":{"column_reference":"col2","odbc_type":"CHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}},{"metadata":{"item_index":0,"is_key":False,"min_length":0,"decimal_scale":0,"decimal_precision":0,"source_field_id":"DSLink1B.col3","max_length":10,"is_signed":False},"nullable":False,"name":"col3","type":"string","app_data":{"column_reference":"col3","odbc_type":"VARCHAR","table_def":"Basic3\\\\Basic3\\\\Basic3","is_unicode_string":False,"type_code":"STRING"}}]}],
    'runtimes': [{"name":"pxOsh","id":"pxOsh"}],
    'app_data': {"datastage":{"version":"3.0.2"}}
}


##############################################################################
# Start of Examples for Service: DatastageV3
##############################################################################
# region
class TestDatastageV3Examples():
    """
    Example Test Class for DatastageV3
    """

    @classmethod
    def setup_class(cls):
        global datastage_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            datastage_service = DatastageV3.new_instance(custome_service_name)

            # end-common
            assert datastage_service is not None

            # Load the configuration
            global config
            config = read_external_sources(custome_service_name)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_datastage_flows_example(self):
        """
        list_datastage_flows request example
        """
        try:
            print('\nlist_datastage_flows() result:')
            # begin-list_datastage_flows

            data_flow_paged_collection = datastage_service.list_datastage_flows(
                project_id=config['PROJECT_ID'],
                limit=100
            ).get_result()

            print(json.dumps(data_flow_paged_collection, indent=2))

            # end-list_datastage_flows

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_datastage_flows_example(self):
        """
        create_datastage_flows request example
        """
        createdFlowId = None
        
        try:
            print('\ncreate_datastage_flows() result:')
            # begin-create_datastage_flows

            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-create_datastage_flows
            
            createdFlowId = data_intg_flow['metadata']['asset_id']

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=createdFlowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_get_datastage_flows_example(self):
        """
        get_datastage_flows request example
        """
        createdFlowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            print('\nget_datastage_flows() result:')
            # begin-get_datastage_flows

            data_intg_flow_json = datastage_service.get_datastage_flows(
                data_intg_flow_id=createdFlowId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow_json, indent=2))

            # end-get_datastage_flows

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=createdFlowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_update_datastage_flows_example(self):
        """
        update_datastage_flows request example
        """
        createdFlowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            print('\nupdate_datastage_flows() result:')
            # begin-update_datastage_flows

            data_intg_flow = datastage_service.update_datastage_flows(
                data_intg_flow_id=createdFlowId,
                data_intg_flow_name='testFlowJob1Updated',
                pipeline_flows=updated_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-update_datastage_flows

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=createdFlowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_clone_datastage_flows_example(self):
        """
        clone_datastage_flows request example
        """
        createdFlowId = None
        clonedFlowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            print('\nclone_datastage_flows() result:')
            # begin-clone_datastage_flows

            data_intg_flow = datastage_service.clone_datastage_flows(
                data_intg_flow_id=createdFlowId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-clone_datastage_flows
            
            clonedFlowId = data_intg_flow['metadata']['asset_id']

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=createdFlowId,
                    project_id=config['PROJECT_ID']
                )
            if (clonedFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=clonedFlowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_compile_datastage_flows_example(self):
        """
        compile_datastage_flows request example
        """
        createdFlowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            print('\ncompile_datastage_flows() result:')
            # begin-compile_datastage_flows

            flow_compile_response = datastage_service.compile_datastage_flows(
                data_intg_flow_id=createdFlowId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(flow_compile_response, indent=2))

            # end-compile_datastage_flows

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdFlowId is not None):
                datastage_service.delete_datastage_flows(
                    id=createdFlowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_list_datastage_subflows_example(self):
        """
        list_datastage_subflows request example
        """
        try:
            print('\nlist_datastage_subflows() result:')
            # begin-list_datastage_subflows

            data_flow_paged_collection = datastage_service.list_datastage_subflows(
                project_id=config['PROJECT_ID'],
                limit=100
            ).get_result()

            print(json.dumps(data_flow_paged_collection, indent=2))

            # end-list_datastage_subflows

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_datastage_subflows_example(self):
        """
        create_datastage_subflows request example
        """
        createdSubflowId = None
        
        try:
            print('\ncreate_datastage_subflows() result:')
            # begin-create_datastage_subflows

            data_intg_flow = datastage_service.create_datastage_subflows(
                data_intg_subflow_name='testSubflow1',
                pipeline_flows=subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-create_datastage_subflows
            
            createdSubflowId = data_intg_flow['metadata']['asset_id']

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdSubflowId is not None):
                datastage_service.delete_datastage_subflows(
                    id=createdSubflowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_get_datastage_subflows_example(self):
        """
        get_datastage_subflows request example
        """
        createdSubflowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_subflows(
                data_intg_subflow_name='testSubflow1',
                pipeline_flows=subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdSubflowId = data_intg_flow['metadata']['asset_id']
            
            print('\nget_datastage_subflows() result:')
            # begin-get_datastage_subflows

            data_intg_flow_json = datastage_service.get_datastage_subflows(
                data_intg_subflow_id=createdSubflowId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow_json, indent=2))

            # end-get_datastage_subflows

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdSubflowId is not None):
                datastage_service.delete_datastage_subflows(
                    id=createdSubflowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_update_datastage_subflows_example(self):
        """
        update_datastage_subflows request example
        """
        createdSubflowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_subflows(
                data_intg_subflow_name='testSubflow1',
                pipeline_flows=subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            createdSubflowId = data_intg_flow['metadata']['asset_id']
            
            print('\nupdate_datastage_subflows() result:')
            # begin-update_datastage_subflows

            data_intg_flow = datastage_service.update_datastage_subflows(
                data_intg_subflow_id=createdSubflowId,
                data_intg_subflow_name='testSubflow1Updated',
                pipeline_flows=updated_subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-update_datastage_subflows

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdSubflowId is not None):
                datastage_service.delete_datastage_subflows(
                    id=createdSubflowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_clone_datastage_subflows_example(self):
        """
        clone_datastage_subflows request example
        """
        createdSubflowId = None
        clonedSubflowId = None
        
        try:
            data_intg_flow = datastage_service.create_datastage_subflows(
                data_intg_subflow_name='testSubflow1',
                pipeline_flows=subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            createdSubflowId = data_intg_flow['metadata']['asset_id']
            
            print('\nclone_datastage_subflows() result:')
            # begin-clone_datastage_subflows

            data_intg_flow = datastage_service.clone_datastage_subflows(
                data_intg_subflow_id=createdSubflowId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(data_intg_flow, indent=2))

            # end-clone_datastage_subflows
            
            clonedSubflowId = data_intg_flow['metadata']['asset_id']

        except ApiException as e:
            pytest.fail(str(e))
            
        finally:
            if (createdSubflowId is not None):
                datastage_service.delete_datastage_subflows(
                    id=createdSubflowId,
                    project_id=config['PROJECT_ID']
                )
            if (clonedSubflowId is not None):
                datastage_service.delete_datastage_subflows(
                    id=clonedSubflowId,
                    project_id=config['PROJECT_ID']
                )

    @needscredentials
    def test_create_migration_example(self):
        """
        create_migration request example
        """
        try:
            print('\ncreate_migration() result:')
            # begin-create_migration

            import_response = datastage_service.create_migration(
                body=open(Path(__file__).parent / 'inputFiles/rowgen_peek.isx', "rb").read(),
                project_id=config['PROJECT_ID'],
                on_failure='continue',
                conflict_resolution='rename',
                attachment_type='isx',
                file_name='rowgen_peek.isx'
            ).get_result()

            print(json.dumps(import_response, indent=2))

            # end-create_migration
            
            importId = import_response['metadata']['id']
            
            startTime = datetime.now()
            while (datetime.now() - startTime).seconds < 60:
                data_intg_migration = datastage_service.get_migration(
                    import_id=importId,
                    project_id=config['PROJECT_ID']
                ).get_result()
                
                status = data_intg_migration['entity']['import_data_flows'][0]['status']
                if status != 'in_progress':
                    migration_success = True
                    migrated_job_id = data_intg_migration['entity']['import_data_flows'][0]['id']
                    break
                else:
                    time.sleep(0.25)
                    
            if (not migration_success):
                raise Exception('Job migration unsuccessful.')
            elif migrated_job_id is not None:
                datastage_service.delete_datastage_flows(
                    id=migrated_job_id,
                    project_id=config['PROJECT_ID']
                )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_migration_example(self):
        """
        get_migration request example
        """
        try:
            migration_create_response = datastage_service.create_migration(
                body=open(Path(__file__).parent / 'inputFiles/rowgen_peek.isx', "rb").read(),
                project_id=config['PROJECT_ID'],
                on_failure='continue',
                conflict_resolution='rename',
                attachment_type='isx',
                file_name='rowgen_peek.isx'
            ).get_result()
            
            importId = migration_create_response['metadata']['id']
            
            print('\nget_migration() result:')
            # begin-get_migration

            import_response = datastage_service.get_migration(
                import_id=importId,
                project_id=config['PROJECT_ID']
            ).get_result()

            print(json.dumps(import_response, indent=2))

            # end-get_migration
            
            startTime = datetime.now()
            while (datetime.now() - startTime).seconds < 60:
                data_intg_migration = datastage_service.get_migration(
                    import_id=importId,
                    project_id=config['PROJECT_ID']
                ).get_result()
                
                status = data_intg_migration['entity']['import_data_flows'][0]['status']
                if status != 'in_progress':
                    migration_success = True
                    migrated_job_id = data_intg_migration['entity']['import_data_flows'][0]['id']
                    break
                else:
                    time.sleep(0.25)
                    
            if (not migration_success):
                raise Exception('Job migration unsuccessful.')
            elif migrated_job_id is not None:
                datastage_service.delete_datastage_flows(
                    id=migrated_job_id,
                    project_id=config['PROJECT_ID']
                )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_migration_example(self):
        """
        delete_migration request example
        """
        try:
            migration_create_response = datastage_service.create_migration(
                body=open(Path(__file__).parent / 'inputFiles/rowgen_peek.isx', "rb").read(),
                project_id=config['PROJECT_ID'],
                on_failure='continue',
                conflict_resolution='rename',
                attachment_type='isx',
                file_name='rowgen_peek.isx'
            ).get_result()
            
            importId = migration_create_response['metadata']['id']
            
            # begin-delete_migration

            response = datastage_service.delete_migration(
                import_id=importId,
                project_id=config['PROJECT_ID']
            )

            # end-delete_migration
            print('\ndelete_migration() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_datastage_subflows_example(self):
        """
        delete_datastage_subflows request example
        """
        try:
            data_intg_flow = datastage_service.create_datastage_subflows(
                data_intg_subflow_name='testSubflow1',
                pipeline_flows=subflow_pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()

            createdSubflowId = data_intg_flow['metadata']['asset_id']
            
            # begin-delete_datastage_subflows

            response = datastage_service.delete_datastage_subflows(
                id=createdSubflowId,
                project_id=config['PROJECT_ID']
            )

            # end-delete_datastage_subflows
            print('\ndelete_datastage_subflows() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_datastage_flows_example(self):
        """
        delete_datastage_flows request example
        """
        try:
            data_intg_flow = datastage_service.create_datastage_flows(
                data_intg_flow_name='testFlowJob1',
                pipeline_flows=pipeline_json_model,
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            # begin-delete_datastage_flows

            response = datastage_service.delete_datastage_flows(
                id=createdFlowId,
                project_id=config['PROJECT_ID']
            )

            # end-delete_datastage_flows
            print('\ndelete_datastage_flows() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: DatastageV3
##############################################################################
