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
import json
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
                project_id=config['PROJECT_ID']
            ).get_result()
            
            createdFlowId = data_intg_flow['metadata']['asset_id']
            
            print('\nupdate_datastage_flows() result:')
            # begin-update_datastage_flows

            data_intg_flow = datastage_service.update_datastage_flows(
                data_intg_flow_id=createdFlowId,
                data_intg_flow_name='testFlowJob1Updated',
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlowUpdated.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflow.json'),
                project_id=config['PROJECT_ID']
            ).get_result()

            createdSubflowId = data_intg_flow['metadata']['asset_id']
            
            print('\nupdate_datastage_subflows() result:')
            # begin-update_datastage_subflows

            data_intg_flow = datastage_service.update_datastage_subflows(
                data_intg_subflow_id=createdSubflowId,
                data_intg_subflow_name='testSubflow1Updated',
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflowUpdated.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleSubflow.json'),
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
                pipeline_flows=UtilHelper.readJsonFileToDict('inputFiles/exampleFlow.json'),
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

class UtilHelper:
    @staticmethod
    def readJsonFileToDict(pathToJsonFile):
        f = open(pathToJsonFile,'r')
        data = json.load(f)
        f.close()
        return data
    
    
    
    
    
    
     
