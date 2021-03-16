# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.28.0-55613c9e-20210220-164656
 
"""
The IBM DataStage service provides APIs to manage, edit, and run data flows in supported
runtimes such as PX-Engine.
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DatastageV3(BaseService):
    """The datastage V3 service."""

    DEFAULT_SERVICE_URL = 'https://datastage.cloud.ibm.com/data_intg'
    DEFAULT_SERVICE_NAME = 'datastage'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DatastageV3':
        """
        Return a new client for the datastage service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the datastage service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # DataStage flows
    #########################


    def datastage_flows_delete(self,
        id: List[str],
        *,
        catalog_id: str = None,
        project_id: str = None,
        force: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete DataStage flows.

        Deletes the specified data flows in a project or catalog (either project_id or
        catalog_id must be set).
        If the deletion of the data flows and their runs will take some time to finish,
        then a 202 response will be returned and the deletion will continue
        asynchronously.
                 All the data flow runs associated with the data flows will also be
        deleted. If a data flow is still running, it will not be deleted unless the force
        parameter is set to true. If a data flow is still running and the force parameter
        is set to true, the call returns immediately with a 202 response. The related data
        flows are deleted after the data flow runs are stopped.

        :param List[str] id: The list of DataStage flow IDs to delete.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param bool force: (optional) Whether to stop all running data flows.
               Running DataStage flows must be stopped before the DataStage flows can be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_delete')
        headers.update(sdk_headers)

        params = {
            'id': convert_list(id),
            'catalog_id': catalog_id,
            'project_id': project_id,
            'force': force
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v3/data_intg_flows'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def datastage_flows_list(self,
        *,
        catalog_id: str = None,
        project_id: str = None,
        sort: str = None,
        start: str = None,
        limit: int = None,
        entity_name: str = None,
        entity_description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get metadata and lock information for DataStage flows.

        Lists the metadata, entity and lock information for DataStage flows that are
        contained in the specified project.
        Use the following parameters to filter the results:
        | Field                    | Match type   | Example
         |
        | ------------------------ | ------------ |
        --------------------------------------- |
        | entity.name              | Equals           | entity.name=MyDataStageFlow  |
        | entity.name              | Starts with      | entity.name=starts:MyData  |
        | entity.description       | Equals           | entity.description=movement  |
        | entity.description       | Starts with      | entity.description=starts:data  |
        To sort the results, use one or more of the parameters  described in the following
        section. If no sort key is specified, the results are sorted in descending order
        on metadata.create_time (i.e. returning the most  recently created data flows
        first).
        | Field                          | Example |
        | ------------------------- | ----------------------------------- |
        | sort     | sort=+entity.name (sort by ascending name)  |
        | sort     | sort=-metadata.create_time (sort by descending creation time) |
        Multiple sort keys can be specified by delimiting them with a comma. For example,
        to sort in descending order on create_time and then in ascending order on name
        use: sort=-metadata.create_time,+entity.name.

        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param str sort: (optional) The field to sort the results on, including
               whether to sort ascending (+) or descending (-), for example,
               sort=-metadata.create_time.
        :param str start: (optional) The page token indicating where to start
               paging from.
        :param int limit: (optional) The limit of the number of items to return,
               for example limit=50. If not specified a default of 100 will be  used.
        :param str entity_name: (optional) Filter results based on the specified
               name.
        :param str entity_description: (optional) Filter results based on the
               specified description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataFlowPagedCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_list')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id,
            'sort': sort,
            'start': start,
            'limit': limit,
            'entity.name': entity_name,
            'entity.description': entity_description
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        url = '/v3/data_intg_flows'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def datastage_flows_create(self,
        data_intg_flow_name: str,
        *,
        pipeline_flows: 'PipelineJson' = None,
        catalog_id: str = None,
        project_id: str = None,
        asset_category: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create DataStage flow.

        Creates a DataStage flow in the specified project or catalog (either project_id or
        catalog_id must be set). All subsequent calls to use the data flow must specify
        the project or catalog ID the data flow was created in.

        :param str data_intg_flow_name: The data flow name.
        :param PipelineJson pipeline_flows: (optional) Pipeline flow to be stored.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param str asset_category: (optional) The category of the asset. Must be
               either SYSTEM or USER. Only a registered service can use this parameter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataIntgFlow` object
        """

        if data_intg_flow_name is None:
            raise ValueError('data_intg_flow_name must be provided')
        if pipeline_flows is not None:
            pipeline_flows = convert_model(pipeline_flows)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_create')
        headers.update(sdk_headers)

        params = {
            'data_intg_flow_name': data_intg_flow_name,
            'catalog_id': catalog_id,
            'project_id': project_id,
            'asset_category': asset_category
        }

        data = {
            'pipeline_flows': pipeline_flows
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json;charset=utf-8'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        url = '/v3/data_intg_flows'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def datastage_flows_get(self,
        data_intg_flow_id: str,
        *,
        catalog_id: str = None,
        project_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get DataStage flow.

        Lists the DataStage flow that is contained in the specified project. Attachments,
        metadata and a limited number of attributes from the entity of each DataStage flow
        is returned.

        :param str data_intg_flow_id: The DataStage flow ID to use.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataIntgFlowJson` object
        """

        if data_intg_flow_id is None:
            raise ValueError('data_intg_flow_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_get')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        path_param_keys = ['data_intg_flow_id']
        path_param_values = self.encode_path_vars(data_intg_flow_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/data_intg_flows/{data_intg_flow_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def datastage_flows_update(self,
        data_intg_flow_id: str,
        data_intg_flow_name: str,
        *,
        pipeline_flows: 'PipelineJson' = None,
        catalog_id: str = None,
        project_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update DataStage flow.

        Modifies a data flow in the specified project or catalog (either project_id or
        catalog_id must be set). All subsequent calls to use the data flow must specify
        the project or catalog ID the data flow was created in.

        :param str data_intg_flow_id: The DataStage flow ID to use.
        :param str data_intg_flow_name: The data flow name.
        :param PipelineJson pipeline_flows: (optional) Pipeline flow to be stored.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataIntgFlow` object
        """

        if data_intg_flow_id is None:
            raise ValueError('data_intg_flow_id must be provided')
        if data_intg_flow_name is None:
            raise ValueError('data_intg_flow_name must be provided')
        if pipeline_flows is not None:
            pipeline_flows = convert_model(pipeline_flows)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_update')
        headers.update(sdk_headers)

        params = {
            'data_intg_flow_name': data_intg_flow_name,
            'catalog_id': catalog_id,
            'project_id': project_id
        }

        data = {
            'pipeline_flows': pipeline_flows
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json;charset=utf-8'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        path_param_keys = ['data_intg_flow_id']
        path_param_values = self.encode_path_vars(data_intg_flow_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/data_intg_flows/{data_intg_flow_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def datastage_flows_clone(self,
        data_intg_flow_id: str,
        *,
        catalog_id: str = None,
        project_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Clone DataStage flow.

        Create a DataStage flow in the specified project or catalog based on an existing
        DataStage flow in the same project or catalog.

        :param str data_intg_flow_id: The DataStage flow ID to use.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DataIntgFlow` object
        """

        if data_intg_flow_id is None:
            raise ValueError('data_intg_flow_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_clone')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        path_param_keys = ['data_intg_flow_id']
        path_param_values = self.encode_path_vars(data_intg_flow_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/data_intg_flows/{data_intg_flow_id}/clone'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def datastage_flows_compile(self,
        data_intg_flow_id: str,
        *,
        catalog_id: str = None,
        project_id: str = None,
        runtime_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Compile DataStage flow to generate runtime assets.

        Generate the runtime assets for a DataStage flow in the specified project or
        catalog (either project_id or catalog_id must be set) for specified runtime type.

        :param str data_intg_flow_id: The DataStage flow ID to use.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param str runtime_type: (optional) The type of the runtime to use. e.g.
               dspxosh or Spark etc. If not provided queried from within pipeline flow if
               available otherwise default of dspxosh is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FlowCompileResponse` object
        """

        if data_intg_flow_id is None:
            raise ValueError('data_intg_flow_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='datastage_flows_compile')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id,
            'runtime_type': runtime_type
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        path_param_keys = ['data_intg_flow_id']
        path_param_values = self.encode_path_vars(data_intg_flow_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/ds_codegen/compile/{data_intg_flow_id}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Migration
    #########################


    def migration_create(self,
        body: BinaryIO,
        *,
        catalog_id: str = None,
        project_id: str = None,
        on_failure: str = None,
        conflict_resolution: str = None,
        attachment_type: str = None,
        file_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create V3 data flows from the attached job export file.

        Creates data flows from the attached job export file. This is an asynchronous
        call. The API call returns almost immediately which does not necessarily imply the
        completion of the import request. It only means that the import request has been
        accepted. The status field of the import request is included in the import
        response object. The status "completed" ("in_progress", "failed", resp.) indicates
        the import request is completed (in progress, and failed, resp.) The job export
        file for an import request may contain one mor more data flows. Unless the
        on_failure option is set to "stop", a completed import request may contain not
        only successfully imported data flows but also data flows that cannot be imported.

        :param BinaryIO body:
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param str on_failure: (optional) Action when the first import failure
               occurs. The default action is "continue" which will continue importing the
               remaining data flows. The "stop" action will stop the import operation upon
               the first error.
        :param str conflict_resolution: (optional) Resolution when data flow to be
               imported has a name conflict with an existing data flow in the project or
               catalog. The default conflict resolution is "skip" will skip  the data flow
               so that it will not be imported. The "rename" resolution will append
               "_Import_NNNN" suffix to the original name and use the new name for the
               imported data flow, while the "replace" resolution will first remove the
               existing data flow with the same name and  import the new data flow. For
               the "rename_replace" option, when the flow name is already used, a new flow
               name with the suffix
               "_DATASTAGE_ISX_IMPORT" will be used. If the name is not currently used,
               the imported flow will be created with this name. In case the new name is
               already used, the existing flow will be removed  first before the imported
               flow is created. With the rename_replace option, job creation will be
               determined  as follows. If the job name is already used, a new job name
               with the suffix ".DataStage job" will be used. If the new job name is not
               currently used, the job will be created with this name. In case the new job
               name is already used, the job creation will not happen and an error will be
               raised.
        :param str attachment_type: (optional) Type of attachment. The default
               attachment type is "isx".
        :param str file_name: (optional) Name of the input file (if exists).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImportResponse` object
        """

        if body is None:
            raise ValueError('body must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='migration_create')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id,
            'on_failure': on_failure,
            'conflict_resolution': conflict_resolution,
            'attachment_type': attachment_type,
            'file_name': file_name
        }

        data = body
        headers['content-type'] = 'application/octet-stream'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        url = '/v3/migration/isx_imports'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


    def migration_delete(self,
        import_id: str,
        *,
        catalog_id: str = None,
        project_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Cancel a previous import request.

        Cancel a previous import request. Use GET /v3/migration/imports/{import_id} to
        obtain the current status of the import, including whether it has been cancelled.

        :param str import_id: Unique ID of the import request.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if import_id is None:
            raise ValueError('import_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='migration_delete')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['import_id']
        path_param_values = self.encode_path_vars(import_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/migration/isx_imports/{import_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def migration_get(self,
        import_id: str,
        *,
        catalog_id: str = None,
        project_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the status of a previous import request.

        Gets the status of an import request. The status field in the response object
        indicates if the given import is completed, in progress, or failed. Detailed
        status information about each imported data flow is also contained in the response
        object.

        :param str import_id: Unique ID of the import request.
        :param str catalog_id: (optional) The ID of the catalog to use. catalog_id
               or project_id is required.
        :param str project_id: (optional) The ID of the project to use. catalog_id
               or project_id is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImportResponse` object
        """

        if import_id is None:
            raise ValueError('import_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='migration_get')
        headers.update(sdk_headers)

        params = {
            'catalog_id': catalog_id,
            'project_id': project_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json;charset=utf-8'

        path_param_keys = ['import_id']
        path_param_values = self.encode_path_vars(import_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/migration/isx_imports/{import_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class DatastageFlowsCreateEnums:
    """
    Enums for datastage_flows_create parameters.
    """

    class AssetCategory(str, Enum):
        """
        The category of the asset. Must be either SYSTEM or USER. Only a registered
        service can use this parameter.
        """
        SYSTEM = 'system'
        USER = 'user'


class MigrationCreateEnums:
    """
    Enums for migration_create parameters.
    """

    class OnFailure(str, Enum):
        """
        Action when the first import failure occurs. The default action is "continue"
        which will continue importing the remaining data flows. The "stop" action will
        stop the import operation upon the first error.
        """
        CONTINUE = 'continue'
        STOP = 'stop'
    class ConflictResolution(str, Enum):
        """
        Resolution when data flow to be imported has a name conflict with an existing data
        flow in the project or catalog. The default conflict resolution is "skip" will
        skip  the data flow so that it will not be imported. The "rename" resolution will
        append "_Import_NNNN" suffix to the original name and use the new name for the
        imported data flow, while the "replace" resolution will first remove the existing
        data flow with the same name and  import the new data flow. For the
        "rename_replace" option, when the flow name is already used, a new flow name with
        the suffix
        "_DATASTAGE_ISX_IMPORT" will be used. If the name is not currently used, the
        imported flow will be created with this name. In case the new name is already
        used, the existing flow will be removed  first before the imported flow is
        created. With the rename_replace option, job creation will be determined  as
        follows. If the job name is already used, a new job name with the suffix
        ".DataStage job" will be used. If the new job name is not currently used, the job
        will be created with this name. In case the new job name is already used, the job
        creation will not happen and an error will be raised.
        """
        SKIP = 'skip'
        RENAME = 'rename'
        REPLACE = 'replace'
        RENAME_REPLACE = 'rename_replace'
    class AttachmentType(str, Enum):
        """
        Type of attachment. The default attachment type is "isx".
        """
        ISX = 'isx'


##############################################################################
# Models
##############################################################################


class AssetEntityROV():
    """
    The rules of visibility for an asset.

    :attr List[str] members: (optional) An array of members belonging to
          AssetEntityROV.
    :attr int mode: (optional) The values for mode are 0 (public, searchable and
          viewable by all), 8 (private, searchable by all, but not viewable unless view
          permission given) or 16 (hidden, only searchable by users with view
          permissions).
    """

    def __init__(self,
                 *,
                 members: List[str] = None,
                 mode: int = None) -> None:
        """
        Initialize a AssetEntityROV object.

        :param List[str] members: (optional) An array of members belonging to
               AssetEntityROV.
        :param int mode: (optional) The values for mode are 0 (public, searchable
               and viewable by all), 8 (private, searchable by all, but not viewable
               unless view permission given) or 16 (hidden, only searchable by users with
               view permissions).
        """
        self.members = members
        self.mode = mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetEntityROV':
        """Initialize a AssetEntityROV object from a json dictionary."""
        args = {}
        if 'members' in _dict:
            args['members'] = _dict.get('members')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetEntityROV object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = self.members
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetEntityROV object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetEntityROV') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetEntityROV') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AssetSystemMetadata():
    """
    System metadata about an asset.

    :attr str asset_id: (optional) The ID of the asset.
    :attr str asset_type: (optional) The type of the asset.
    :attr str catalog_id: (optional) The ID of the catalog which contains the asset.
          catalog_id or project_id is required.
    :attr datetime create_time: (optional) The timestamp when the asset was created
          (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the
          date-time format as specified by RFC 3339).
    :attr str creator_id: (optional) The IAM ID of the user that created the asset.
    :attr str description: (optional) The description of the asset.
    :attr str href: (optional) URL that can be used to get the asset.
    :attr str name: (optional) name of the asset.
    :attr str origin_country: (optional) origin of the asset.
    :attr str project_id: (optional) The ID of the project which contains the asset.
          catalog_id or project_id is required.
    :attr str resource_key: (optional) This is a unique string that uniquely
          identifies an asset.
    :attr int size: (optional) size of the asset.
    :attr dict source_system: (optional) Custom data to be associated with a given
          object.
    :attr List[str] tags: (optional) A list of tags that can be used to identify
          different types of data flow.
    :attr AssetSystemMetadataUsage usage: (optional) Metadata usage information
          about an asset.
    """

    def __init__(self,
                 *,
                 asset_id: str = None,
                 asset_type: str = None,
                 catalog_id: str = None,
                 create_time: datetime = None,
                 creator_id: str = None,
                 description: str = None,
                 href: str = None,
                 name: str = None,
                 origin_country: str = None,
                 project_id: str = None,
                 resource_key: str = None,
                 size: int = None,
                 source_system: dict = None,
                 tags: List[str] = None,
                 usage: 'AssetSystemMetadataUsage' = None) -> None:
        """
        Initialize a AssetSystemMetadata object.

        :param str asset_id: (optional) The ID of the asset.
        :param str asset_type: (optional) The type of the asset.
        :param str catalog_id: (optional) The ID of the catalog which contains the
               asset. catalog_id or project_id is required.
        :param datetime create_time: (optional) The timestamp when the asset was
               created (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339).
        :param str creator_id: (optional) The IAM ID of the user that created the
               asset.
        :param str description: (optional) The description of the asset.
        :param str href: (optional) URL that can be used to get the asset.
        :param str name: (optional) name of the asset.
        :param str origin_country: (optional) origin of the asset.
        :param str project_id: (optional) The ID of the project which contains the
               asset. catalog_id or project_id is required.
        :param str resource_key: (optional) This is a unique string that uniquely
               identifies an asset.
        :param int size: (optional) size of the asset.
        :param dict source_system: (optional) Custom data to be associated with a
               given object.
        :param List[str] tags: (optional) A list of tags that can be used to
               identify different types of data flow.
        :param AssetSystemMetadataUsage usage: (optional) Metadata usage
               information about an asset.
        """
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.catalog_id = catalog_id
        self.create_time = create_time
        self.creator_id = creator_id
        self.description = description
        self.href = href
        self.name = name
        self.origin_country = origin_country
        self.project_id = project_id
        self.resource_key = resource_key
        self.size = size
        self.source_system = source_system
        self.tags = tags
        self.usage = usage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetSystemMetadata':
        """Initialize a AssetSystemMetadata object from a json dictionary."""
        args = {}
        if 'asset_id' in _dict:
            args['asset_id'] = _dict.get('asset_id')
        if 'asset_type' in _dict:
            args['asset_type'] = _dict.get('asset_type')
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'create_time' in _dict:
            args['create_time'] = string_to_datetime(_dict.get('create_time'))
        if 'creator_id' in _dict:
            args['creator_id'] = _dict.get('creator_id')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'origin_country' in _dict:
            args['origin_country'] = _dict.get('origin_country')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        if 'resource_key' in _dict:
            args['resource_key'] = _dict.get('resource_key')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'source_system' in _dict:
            args['source_system'] = _dict.get('source_system')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'usage' in _dict:
            args['usage'] = AssetSystemMetadataUsage.from_dict(_dict.get('usage'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetSystemMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'asset_id') and self.asset_id is not None:
            _dict['asset_id'] = self.asset_id
        if hasattr(self, 'asset_type') and self.asset_type is not None:
            _dict['asset_type'] = self.asset_type
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = datetime_to_string(self.create_time)
        if hasattr(self, 'creator_id') and self.creator_id is not None:
            _dict['creator_id'] = self.creator_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'origin_country') and self.origin_country is not None:
            _dict['origin_country'] = self.origin_country
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'resource_key') and self.resource_key is not None:
            _dict['resource_key'] = self.resource_key
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'source_system') and self.source_system is not None:
            _dict['source_system'] = self.source_system
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = self.usage.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetSystemMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetSystemMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetSystemMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AssetSystemMetadataUsage():
    """
    Metadata usage information about an asset.

    :attr int access_count: Number of times this asset has been accessed.
    :attr datetime last_access_time: The timestamp when the asset was last accessed
          (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the
          date-time format as specified by RFC 3339).
    :attr str last_accessor_id: The IAM ID of the user that last accessed the asset.
    :attr datetime last_modification_time: The timestamp when the asset was last
          modified (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching
          the date-time format as specified by RFC 3339).
    :attr str last_modifier_id: The IAM ID of the user that last modified the asset.
    """

    def __init__(self,
                 access_count: int,
                 last_access_time: datetime,
                 last_accessor_id: str,
                 last_modification_time: datetime,
                 last_modifier_id: str) -> None:
        """
        Initialize a AssetSystemMetadataUsage object.

        :param int access_count: Number of times this asset has been accessed.
        :param datetime last_access_time: The timestamp when the asset was last
               accessed (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339).
        :param str last_accessor_id: The IAM ID of the user that last accessed the
               asset.
        :param datetime last_modification_time: The timestamp when the asset was
               last modified (in format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339).
        :param str last_modifier_id: The IAM ID of the user that last modified the
               asset.
        """
        self.access_count = access_count
        self.last_access_time = last_access_time
        self.last_accessor_id = last_accessor_id
        self.last_modification_time = last_modification_time
        self.last_modifier_id = last_modifier_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssetSystemMetadataUsage':
        """Initialize a AssetSystemMetadataUsage object from a json dictionary."""
        args = {}
        if 'access_count' in _dict:
            args['access_count'] = _dict.get('access_count')
        else:
            raise ValueError('Required property \'access_count\' not present in AssetSystemMetadataUsage JSON')
        if 'last_access_time' in _dict:
            args['last_access_time'] = string_to_datetime(_dict.get('last_access_time'))
        else:
            raise ValueError('Required property \'last_access_time\' not present in AssetSystemMetadataUsage JSON')
        if 'last_accessor_id' in _dict:
            args['last_accessor_id'] = _dict.get('last_accessor_id')
        else:
            raise ValueError('Required property \'last_accessor_id\' not present in AssetSystemMetadataUsage JSON')
        if 'last_modification_time' in _dict:
            args['last_modification_time'] = string_to_datetime(_dict.get('last_modification_time'))
        else:
            raise ValueError('Required property \'last_modification_time\' not present in AssetSystemMetadataUsage JSON')
        if 'last_modifier_id' in _dict:
            args['last_modifier_id'] = _dict.get('last_modifier_id')
        else:
            raise ValueError('Required property \'last_modifier_id\' not present in AssetSystemMetadataUsage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssetSystemMetadataUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_count') and self.access_count is not None:
            _dict['access_count'] = self.access_count
        if hasattr(self, 'last_access_time') and self.last_access_time is not None:
            _dict['last_access_time'] = datetime_to_string(self.last_access_time)
        if hasattr(self, 'last_accessor_id') and self.last_accessor_id is not None:
            _dict['last_accessor_id'] = self.last_accessor_id
        if hasattr(self, 'last_modification_time') and self.last_modification_time is not None:
            _dict['last_modification_time'] = datetime_to_string(self.last_modification_time)
        if hasattr(self, 'last_modifier_id') and self.last_modifier_id is not None:
            _dict['last_modifier_id'] = self.last_modifier_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssetSystemMetadataUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssetSystemMetadataUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssetSystemMetadataUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataFlowPagedCollection():
    """
    A page from a collection of DataStage flows.

    :attr List[DataIntgFlow] data_flows: (optional) A page from a collection of
          DataStage flows.
    :attr HrefModel first: (optional) URI of a resource.
    :attr HrefModel last: (optional) URI of a resource.
    :attr int limit: (optional) The number of data flows requested to be returned.
    :attr HrefModel next: (optional) URI of a resource.
    :attr HrefModel prev: (optional) URI of a resource.
    :attr int total_count: (optional) The total number of DataStage flows available.
    """

    def __init__(self,
                 *,
                 data_flows: List['DataIntgFlow'] = None,
                 first: 'HrefModel' = None,
                 last: 'HrefModel' = None,
                 limit: int = None,
                 next: 'HrefModel' = None,
                 prev: 'HrefModel' = None,
                 total_count: int = None) -> None:
        """
        Initialize a DataFlowPagedCollection object.

        :param List[DataIntgFlow] data_flows: (optional) A page from a collection
               of DataStage flows.
        :param HrefModel first: (optional) URI of a resource.
        :param HrefModel last: (optional) URI of a resource.
        :param int limit: (optional) The number of data flows requested to be
               returned.
        :param HrefModel next: (optional) URI of a resource.
        :param HrefModel prev: (optional) URI of a resource.
        :param int total_count: (optional) The total number of DataStage flows
               available.
        """
        self.data_flows = data_flows
        self.first = first
        self.last = last
        self.limit = limit
        self.next = next
        self.prev = prev
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataFlowPagedCollection':
        """Initialize a DataFlowPagedCollection object from a json dictionary."""
        args = {}
        if 'data_flows' in _dict:
            args['data_flows'] = [DataIntgFlow.from_dict(x) for x in _dict.get('data_flows')]
        if 'first' in _dict:
            args['first'] = HrefModel.from_dict(_dict.get('first'))
        if 'last' in _dict:
            args['last'] = HrefModel.from_dict(_dict.get('last'))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'next' in _dict:
            args['next'] = HrefModel.from_dict(_dict.get('next'))
        if 'prev' in _dict:
            args['prev'] = HrefModel.from_dict(_dict.get('prev'))
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataFlowPagedCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_flows') and self.data_flows is not None:
            _dict['data_flows'] = [x.to_dict() for x in self.data_flows]
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'prev') and self.prev is not None:
            _dict['prev'] = self.prev.to_dict()
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataFlowPagedCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataFlowPagedCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataFlowPagedCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataImportError():
    """
    An import error object describe an import problem specific to a particular data flow.

    :attr str description: (optional) additional error text.
    :attr str name: error object name.
    :attr str type: error type.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 description: str = None) -> None:
        """
        Initialize a DataImportError object.

        :param str name: error object name.
        :param str type: error type.
        :param str description: (optional) additional error text.
        """
        self.description = description
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataImportError':
        """Initialize a DataImportError object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in DataImportError JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in DataImportError JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataImportError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataImportError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataImportError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataImportError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        error type.
        """
        UNSUPPORTED_STAGE_TYPE = 'unsupported_stage_type'
        UNSUPPORTED_FEATURE = 'unsupported_feature'
        EMPTY_JSON = 'empty_json'
        ISX_CONVERSION_ERROR = 'isx_conversion_error'
        MODEL_CONVERSION_ERROR = 'model_conversion_error'
        INVALID_INPUT_TYPE = 'invalid_input_type'
        INVALID_JSON_FORMAT = 'invalid_json_format'
        JSON_CONVERSION_ERROR = 'json_conversion_error'
        FLOW_DELETION_ERROR = 'flow_deletion_error'
        FLOW_CREATION_ERROR = 'flow_creation_error'
        FLOW_RESPONSE_PARSING_ERROR = 'flow_response_parsing_error'
        AUTH_TOKEN_ERROR = 'auth_token_error'
        FLOW_COMPILATION_ERROR = 'flow_compilation_error'
        EMPTY_STAGE_LIST = 'empty_stage_list'
        EMPTY_STAGE_NODE = 'empty_stage_node'
        MISSING_STAGE_TYPE_CLASS_NAME = 'missing_stage_type_class_name'
        DUMMY_STAGE = 'dummy_stage'
        MISSING_STAGE_TYPE = 'missing_stage_type'
        MISSING_REPOS_ID = 'missing_repos_id'
        STAGE_CONVERSION_ERROR = 'stage_conversion_error'
        UNIMPLEMENTED_STAGE_TYPE = 'unimplemented_stage_type'
        JOB_CREATION_ERROR = 'job_creation_error'
        JOB_RUN_ERROR = 'job_run_error'
        FLOW_SEARCH_ERROR = 'flow_search_error'
        UNSUPPORTED_JOB_TYPE = 'unsupported_job_type'
        INTERNAL_ERROR = 'internal_error'
        CONNECTION_CREATION_ERROR = 'connection_creation_error'
        FLOW_RENAME_ERROR = 'flow_rename_error'
        DUPLICATE_JOB_ERROR = 'duplicate_job_error'
        PARAMETER_SET_CREATION_ERROR = 'parameter_set_creation_error'
        DISTRIBUTED_LOCK_ERROR = 'distributed_lock_error'
        DUPLICATE_OBJECT_ERROR = 'duplicate_object_error'


class DataIntgFlow():
    """
    A DataStage flow model that defines physical source(s), physical target(s) and an
    optional pipeline containing operations to apply to source(s).

    :attr List[object] attachments: (optional) Metadata information for datastage
          flow.
    :attr DataIntgFlowEntity entity: (optional) The underlying DataStage flow
          definition.
    :attr AssetSystemMetadata metadata: (optional) System metadata about an asset.
    """

    def __init__(self,
                 *,
                 attachments: List[object] = None,
                 entity: 'DataIntgFlowEntity' = None,
                 metadata: 'AssetSystemMetadata' = None) -> None:
        """
        Initialize a DataIntgFlow object.

        :param List[object] attachments: (optional) Metadata information for
               datastage flow.
        :param DataIntgFlowEntity entity: (optional) The underlying DataStage flow
               definition.
        :param AssetSystemMetadata metadata: (optional) System metadata about an
               asset.
        """
        self.attachments = attachments
        self.entity = entity
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlow':
        """Initialize a DataIntgFlow object from a json dictionary."""
        args = {}
        if 'attachments' in _dict:
            args['attachments'] = _dict.get('attachments')
        if 'entity' in _dict:
            args['entity'] = DataIntgFlowEntity.from_dict(_dict.get('entity'))
        if 'metadata' in _dict:
            args['metadata'] = AssetSystemMetadata.from_dict(_dict.get('metadata'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = self.attachments
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataIntgFlowEntity():
    """
    The underlying DataStage flow definition.

    :attr object data_intg_flow: (optional) Asset type object.
    :attr str description: (optional) The description of the DataStage flow.
    :attr DataIntgFlowLock lock: (optional) Lock information for a DataStage flow
          asset.
    :attr str name: (optional) The name of the DataStage flow.
    :attr AssetEntityROV rov: (optional) The rules of visibility for an asset.
    :attr str sub_type: (optional) A read-only field that can be used to distinguish
          between different types of data flow based on the service that created it.
    """

    def __init__(self,
                 *,
                 data_intg_flow: object = None,
                 description: str = None,
                 lock: 'DataIntgFlowLock' = None,
                 name: str = None,
                 rov: 'AssetEntityROV' = None,
                 sub_type: str = None) -> None:
        """
        Initialize a DataIntgFlowEntity object.

        :param object data_intg_flow: (optional) Asset type object.
        :param str description: (optional) The description of the DataStage flow.
        :param DataIntgFlowLock lock: (optional) Lock information for a DataStage
               flow asset.
        :param str name: (optional) The name of the DataStage flow.
        :param AssetEntityROV rov: (optional) The rules of visibility for an asset.
        :param str sub_type: (optional) A read-only field that can be used to
               distinguish between different types of data flow based on the service that
               created it.
        """
        self.data_intg_flow = data_intg_flow
        self.description = description
        self.lock = lock
        self.name = name
        self.rov = rov
        self.sub_type = sub_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlowEntity':
        """Initialize a DataIntgFlowEntity object from a json dictionary."""
        args = {}
        if 'data_intg_flow' in _dict:
            args['data_intg_flow'] = _dict.get('data_intg_flow')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'lock' in _dict:
            args['lock'] = DataIntgFlowLock.from_dict(_dict.get('lock'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'rov' in _dict:
            args['rov'] = AssetEntityROV.from_dict(_dict.get('rov'))
        if 'sub_type' in _dict:
            args['sub_type'] = _dict.get('sub_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlowEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_intg_flow') and self.data_intg_flow is not None:
            _dict['data_intg_flow'] = self.data_intg_flow
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'lock') and self.lock is not None:
            _dict['lock'] = self.lock.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'rov') and self.rov is not None:
            _dict['rov'] = self.rov.to_dict()
        if hasattr(self, 'sub_type') and self.sub_type is not None:
            _dict['sub_type'] = self.sub_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlowEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlowEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlowEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataIntgFlowJson():
    """
    A pipeline JSON containing operations to apply to source(s).

    :attr PipelineJson attachments: (optional) Pipeline flow to be stored.
    :attr DataIntgFlowEntity entity: (optional) The underlying DataStage flow
          definition.
    :attr AssetSystemMetadata metadata: (optional) System metadata about an asset.
    """

    def __init__(self,
                 *,
                 attachments: 'PipelineJson' = None,
                 entity: 'DataIntgFlowEntity' = None,
                 metadata: 'AssetSystemMetadata' = None) -> None:
        """
        Initialize a DataIntgFlowJson object.

        :param PipelineJson attachments: (optional) Pipeline flow to be stored.
        :param DataIntgFlowEntity entity: (optional) The underlying DataStage flow
               definition.
        :param AssetSystemMetadata metadata: (optional) System metadata about an
               asset.
        """
        self.attachments = attachments
        self.entity = entity
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlowJson':
        """Initialize a DataIntgFlowJson object from a json dictionary."""
        args = {}
        if 'attachments' in _dict:
            args['attachments'] = PipelineJson.from_dict(_dict.get('attachments'))
        if 'entity' in _dict:
            args['entity'] = DataIntgFlowEntity.from_dict(_dict.get('entity'))
        if 'metadata' in _dict:
            args['metadata'] = AssetSystemMetadata.from_dict(_dict.get('metadata'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlowJson object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachments') and self.attachments is not None:
            _dict['attachments'] = self.attachments.to_dict()
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlowJson object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlowJson') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlowJson') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataIntgFlowLock():
    """
    Lock information for a DataStage flow asset.

    :attr DataIntgFlowLockEntity entity: (optional) Entity information for a
          DataStage lock object.
    :attr DataIntgFlowLockMetadata metadata: (optional) Metadata information for a
          DataStage lock object.
    """

    def __init__(self,
                 *,
                 entity: 'DataIntgFlowLockEntity' = None,
                 metadata: 'DataIntgFlowLockMetadata' = None) -> None:
        """
        Initialize a DataIntgFlowLock object.

        :param DataIntgFlowLockEntity entity: (optional) Entity information for a
               DataStage lock object.
        :param DataIntgFlowLockMetadata metadata: (optional) Metadata information
               for a DataStage lock object.
        """
        self.entity = entity
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlowLock':
        """Initialize a DataIntgFlowLock object from a json dictionary."""
        args = {}
        if 'entity' in _dict:
            args['entity'] = DataIntgFlowLockEntity.from_dict(_dict.get('entity'))
        if 'metadata' in _dict:
            args['metadata'] = DataIntgFlowLockMetadata.from_dict(_dict.get('metadata'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlowLock object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlowLock object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlowLock') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlowLock') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataIntgFlowLockEntity():
    """
    Entity information for a DataStage lock object.

    :attr str data_intg_flow_id: (optional) DataStage flow ID that is locked.
    :attr str requester: (optional) Requester of the lock.
    """

    def __init__(self,
                 *,
                 data_intg_flow_id: str = None,
                 requester: str = None) -> None:
        """
        Initialize a DataIntgFlowLockEntity object.

        :param str data_intg_flow_id: (optional) DataStage flow ID that is locked.
        :param str requester: (optional) Requester of the lock.
        """
        self.data_intg_flow_id = data_intg_flow_id
        self.requester = requester

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlowLockEntity':
        """Initialize a DataIntgFlowLockEntity object from a json dictionary."""
        args = {}
        if 'data_intg_flow_id' in _dict:
            args['data_intg_flow_id'] = _dict.get('data_intg_flow_id')
        if 'requester' in _dict:
            args['requester'] = _dict.get('requester')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlowLockEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_intg_flow_id') and self.data_intg_flow_id is not None:
            _dict['data_intg_flow_id'] = self.data_intg_flow_id
        if hasattr(self, 'requester') and self.requester is not None:
            _dict['requester'] = self.requester
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlowLockEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlowLockEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlowLockEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataIntgFlowLockMetadata():
    """
    Metadata information for a DataStage lock object.

    :attr bool alive: (optional) Lock status.
    """

    def __init__(self,
                 *,
                 alive: bool = None) -> None:
        """
        Initialize a DataIntgFlowLockMetadata object.

        :param bool alive: (optional) Lock status.
        """
        self.alive = alive

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataIntgFlowLockMetadata':
        """Initialize a DataIntgFlowLockMetadata object from a json dictionary."""
        args = {}
        if 'alive' in _dict:
            args['alive'] = _dict.get('alive')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataIntgFlowLockMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'alive') and self.alive is not None:
            _dict['alive'] = self.alive
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataIntgFlowLockMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataIntgFlowLockMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataIntgFlowLockMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FlowCompileResponse():
    """
    Describes the compile response model.

    :attr object message: (optional) Compile result for DataStage flow.
    :attr str type: (optional) Compile response type. e.g. ok or error.
    """

    def __init__(self,
                 *,
                 message: object = None,
                 type: str = None) -> None:
        """
        Initialize a FlowCompileResponse object.

        :param object message: (optional) Compile result for DataStage flow.
        :param str type: (optional) Compile response type. e.g. ok or error.
        """
        self.message = message
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FlowCompileResponse':
        """Initialize a FlowCompileResponse object from a json dictionary."""
        args = {}
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FlowCompileResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FlowCompileResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FlowCompileResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FlowCompileResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HrefModel():
    """
    URI of a resource.

    :attr str href: URI of a resource.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a HrefModel object.

        :param str href: URI of a resource.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HrefModel':
        """Initialize a HrefModel object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in HrefModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HrefModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HrefModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HrefModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HrefModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImportCount():
    """
    Import statistics. total = imported (including renamed and replaced) + skipped +
    failed + deprecated + unsupported + pending.

    :attr int connections_total: (optional) Total number of data connections.
    :attr int deprecated: Total number of deprecated resources in the import file.
    :attr int failed: Total number of data flows that cannot be imported due to
          import errors.
    :attr int imported: Total number of data flows successfully imported.
    :attr int parameter_sets_total: (optional) Total number of parameter sets.
    :attr int pending: Total number of data flows that have not been processed.
    :attr int px_containers_total: (optional) Total number of parallel job
          containers.
    :attr int renamed: Total number of data flows successfully imported and renamed
          due to a name conflict. The renamed count is included in the imported count.
    :attr int replaced: Total number of existing data flows replaced by imported
          flows. The replaced count is included in the imported count.
    :attr int sequence_jobs_total: (optional) Total number of sequence jobs.
    :attr int skipped: Total number of data flows skipped due to name conflicts. The
          skipped count is not included in the failed count or imported count.
    :attr int table_definitions_total: (optional) Total number of table definitions.
    :attr int total: Total number of data flows to be imported.
    :attr int unsupported: Total number of unsupported resources in the import file.
    """

    def __init__(self,
                 deprecated: int,
                 failed: int,
                 imported: int,
                 pending: int,
                 renamed: int,
                 replaced: int,
                 skipped: int,
                 total: int,
                 unsupported: int,
                 *,
                 connections_total: int = None,
                 parameter_sets_total: int = None,
                 px_containers_total: int = None,
                 sequence_jobs_total: int = None,
                 table_definitions_total: int = None) -> None:
        """
        Initialize a ImportCount object.

        :param int deprecated: Total number of deprecated resources in the import
               file.
        :param int failed: Total number of data flows that cannot be imported due
               to import errors.
        :param int imported: Total number of data flows successfully imported.
        :param int pending: Total number of data flows that have not been
               processed.
        :param int renamed: Total number of data flows successfully imported and
               renamed due to a name conflict. The renamed count is included in the
               imported count.
        :param int replaced: Total number of existing data flows replaced by
               imported flows. The replaced count is included in the imported count.
        :param int skipped: Total number of data flows skipped due to name
               conflicts. The skipped count is not included in the failed count or
               imported count.
        :param int total: Total number of data flows to be imported.
        :param int unsupported: Total number of unsupported resources in the import
               file.
        :param int connections_total: (optional) Total number of data connections.
        :param int parameter_sets_total: (optional) Total number of parameter sets.
        :param int px_containers_total: (optional) Total number of parallel job
               containers.
        :param int sequence_jobs_total: (optional) Total number of sequence jobs.
        :param int table_definitions_total: (optional) Total number of table
               definitions.
        """
        self.connections_total = connections_total
        self.deprecated = deprecated
        self.failed = failed
        self.imported = imported
        self.parameter_sets_total = parameter_sets_total
        self.pending = pending
        self.px_containers_total = px_containers_total
        self.renamed = renamed
        self.replaced = replaced
        self.sequence_jobs_total = sequence_jobs_total
        self.skipped = skipped
        self.table_definitions_total = table_definitions_total
        self.total = total
        self.unsupported = unsupported

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportCount':
        """Initialize a ImportCount object from a json dictionary."""
        args = {}
        if 'connections_total' in _dict:
            args['connections_total'] = _dict.get('connections_total')
        if 'deprecated' in _dict:
            args['deprecated'] = _dict.get('deprecated')
        else:
            raise ValueError('Required property \'deprecated\' not present in ImportCount JSON')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        else:
            raise ValueError('Required property \'failed\' not present in ImportCount JSON')
        if 'imported' in _dict:
            args['imported'] = _dict.get('imported')
        else:
            raise ValueError('Required property \'imported\' not present in ImportCount JSON')
        if 'parameter_sets_total' in _dict:
            args['parameter_sets_total'] = _dict.get('parameter_sets_total')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        else:
            raise ValueError('Required property \'pending\' not present in ImportCount JSON')
        if 'px_containers_total' in _dict:
            args['px_containers_total'] = _dict.get('px_containers_total')
        if 'renamed' in _dict:
            args['renamed'] = _dict.get('renamed')
        else:
            raise ValueError('Required property \'renamed\' not present in ImportCount JSON')
        if 'replaced' in _dict:
            args['replaced'] = _dict.get('replaced')
        else:
            raise ValueError('Required property \'replaced\' not present in ImportCount JSON')
        if 'sequence_jobs_total' in _dict:
            args['sequence_jobs_total'] = _dict.get('sequence_jobs_total')
        if 'skipped' in _dict:
            args['skipped'] = _dict.get('skipped')
        else:
            raise ValueError('Required property \'skipped\' not present in ImportCount JSON')
        if 'table_definitions_total' in _dict:
            args['table_definitions_total'] = _dict.get('table_definitions_total')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        else:
            raise ValueError('Required property \'total\' not present in ImportCount JSON')
        if 'unsupported' in _dict:
            args['unsupported'] = _dict.get('unsupported')
        else:
            raise ValueError('Required property \'unsupported\' not present in ImportCount JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportCount object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'connections_total') and self.connections_total is not None:
            _dict['connections_total'] = self.connections_total
        if hasattr(self, 'deprecated') and self.deprecated is not None:
            _dict['deprecated'] = self.deprecated
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'imported') and self.imported is not None:
            _dict['imported'] = self.imported
        if hasattr(self, 'parameter_sets_total') and self.parameter_sets_total is not None:
            _dict['parameter_sets_total'] = self.parameter_sets_total
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        if hasattr(self, 'px_containers_total') and self.px_containers_total is not None:
            _dict['px_containers_total'] = self.px_containers_total
        if hasattr(self, 'renamed') and self.renamed is not None:
            _dict['renamed'] = self.renamed
        if hasattr(self, 'replaced') and self.replaced is not None:
            _dict['replaced'] = self.replaced
        if hasattr(self, 'sequence_jobs_total') and self.sequence_jobs_total is not None:
            _dict['sequence_jobs_total'] = self.sequence_jobs_total
        if hasattr(self, 'skipped') and self.skipped is not None:
            _dict['skipped'] = self.skipped
        if hasattr(self, 'table_definitions_total') and self.table_definitions_total is not None:
            _dict['table_definitions_total'] = self.table_definitions_total
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'unsupported') and self.unsupported is not None:
            _dict['unsupported'] = self.unsupported
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportCount object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportCount') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportCount') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImportFlow():
    """
    Import flow object.

    :attr str conflict_resolution_status: (optional) conflict resolution status.
    :attr datetime end_time: (optional) The timestamp when the flow import is
          completed. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching
          the date-time format as specified by RFC 3339.
    :attr List[DataImportError] errors: (optional) The errors array report all the
          problems preventing the data flow from being successfully imported.
    :attr str id: (optional) Unique id of the data flow. This field is returned only
          if the underlying data flow has been successfully imported.
    :attr str job_id: (optional) Unique id of the job. This field is returned only
          if the corresponding job object has been successfully created.
    :attr str job_name: (optional) Job name. This field is returned only if the
          corresponding job object has been successfully created.
    :attr str job_type: (optional) (deprecated) original type of the job or data
          flow in the import file.
    :attr str name: Name of the imported data flow.
    :attr str original_name: (optional) Name of the data flow to be imported.
    :attr str ref_asset_id: (optional) The ID of an existing asset this object
          refers to. If ref_asset_id is specified, the id field will be the same as
          ref_asset_id for backward compatibility.
    :attr str status: data import status.
    :attr str type: (optional) type of the job or data connection in the import
          file.
    :attr List[ImportFlowWarning] warnings: (optional) The warnings array report all
          the warnings in the data flow import operation.
    """

    def __init__(self,
                 name: str,
                 status: str,
                 *,
                 conflict_resolution_status: str = None,
                 end_time: datetime = None,
                 errors: List['DataImportError'] = None,
                 id: str = None,
                 job_id: str = None,
                 job_name: str = None,
                 job_type: str = None,
                 original_name: str = None,
                 ref_asset_id: str = None,
                 type: str = None,
                 warnings: List['ImportFlowWarning'] = None) -> None:
        """
        Initialize a ImportFlow object.

        :param str name: Name of the imported data flow.
        :param str status: data import status.
        :param str conflict_resolution_status: (optional) conflict resolution
               status.
        :param datetime end_time: (optional) The timestamp when the flow import is
               completed. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339.
        :param List[DataImportError] errors: (optional) The errors array report all
               the problems preventing the data flow from being successfully imported.
        :param str id: (optional) Unique id of the data flow. This field is
               returned only if the underlying data flow has been successfully imported.
        :param str job_id: (optional) Unique id of the job. This field is returned
               only if the corresponding job object has been successfully created.
        :param str job_name: (optional) Job name. This field is returned only if
               the corresponding job object has been successfully created.
        :param str job_type: (optional) (deprecated) original type of the job or
               data flow in the import file.
        :param str original_name: (optional) Name of the data flow to be imported.
        :param str ref_asset_id: (optional) The ID of an existing asset this object
               refers to. If ref_asset_id is specified, the id field will be the same as
               ref_asset_id for backward compatibility.
        :param str type: (optional) type of the job or data connection in the
               import file.
        :param List[ImportFlowWarning] warnings: (optional) The warnings array
               report all the warnings in the data flow import operation.
        """
        self.conflict_resolution_status = conflict_resolution_status
        self.end_time = end_time
        self.errors = errors
        self.id = id
        self.job_id = job_id
        self.job_name = job_name
        self.job_type = job_type
        self.name = name
        self.original_name = original_name
        self.ref_asset_id = ref_asset_id
        self.status = status
        self.type = type
        self.warnings = warnings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportFlow':
        """Initialize a ImportFlow object from a json dictionary."""
        args = {}
        if 'conflict_resolution_status' in _dict:
            args['conflict_resolution_status'] = _dict.get('conflict_resolution_status')
        if 'end_time' in _dict:
            args['end_time'] = string_to_datetime(_dict.get('end_time'))
        if 'errors' in _dict:
            args['errors'] = [DataImportError.from_dict(x) for x in _dict.get('errors')]
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'job_id' in _dict:
            args['job_id'] = _dict.get('job_id')
        if 'job_name' in _dict:
            args['job_name'] = _dict.get('job_name')
        if 'job_type' in _dict:
            args['job_type'] = _dict.get('job_type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ImportFlow JSON')
        if 'original_name' in _dict:
            args['original_name'] = _dict.get('original_name')
        if 'ref_asset_id' in _dict:
            args['ref_asset_id'] = _dict.get('ref_asset_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in ImportFlow JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'warnings' in _dict:
            args['warnings'] = [ImportFlowWarning.from_dict(x) for x in _dict.get('warnings')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportFlow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'conflict_resolution_status') and self.conflict_resolution_status is not None:
            _dict['conflict_resolution_status'] = self.conflict_resolution_status
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = datetime_to_string(self.end_time)
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'job_id') and self.job_id is not None:
            _dict['job_id'] = self.job_id
        if hasattr(self, 'job_name') and self.job_name is not None:
            _dict['job_name'] = self.job_name
        if hasattr(self, 'job_type') and self.job_type is not None:
            _dict['job_type'] = self.job_type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'original_name') and self.original_name is not None:
            _dict['original_name'] = self.original_name
        if hasattr(self, 'ref_asset_id') and self.ref_asset_id is not None:
            _dict['ref_asset_id'] = self.ref_asset_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x.to_dict() for x in self.warnings]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportFlow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportFlow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportFlow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConflictResolutionStatusEnum(str, Enum):
        """
        conflict resolution status.
        """
        FLOW_REPLACEMENT_SUCCEEDED = 'flow_replacement_succeeded'
        FLOW_REPLACEMENT_FAILED = 'flow_replacement_failed'
        IMPORT_FLOW_RENAMED = 'import_flow_renamed'
        IMPORT_FLOW_SKIPPED = 'import_flow_skipped'
        CONNECTION_REPLACEMENT_SUCCEEDED = 'connection_replacement_succeeded'
        CONNECTION_REPLACEMENT_FAILED = 'connection_replacement_failed'
        CONNECTION_RENAMED = 'connection_renamed'
        CONNECTION_SKIPPED = 'connection_skipped'
        PARAMETER_SET_REPLACEMENT_SUCCEEDED = 'parameter_set_replacement_succeeded'
        PARAMETER_SET_REPLACEMENT_FAILED = 'parameter_set_replacement_failed'
        PARAMETER_SET_RENAMED = 'parameter_set_renamed'
        PARAMETER_SET_SKIPPED = 'parameter_set_skipped'
        TABLE_DEFINITION_REPLACEMENT_SUCCEEDED = 'table_definition_replacement_succeeded'
        TABLE_DEFINITION_REPLACEMENT_FAILED = 'table_definition_replacement_failed'
        TABLE_DEFINITION_RENAMED = 'table_definition_renamed'
        TABLE_DEFINITION_SKIPPED = 'table_definition_skipped'


    class JobTypeEnum(str, Enum):
        """
        (deprecated) original type of the job or data flow in the import file.
        """
        PX_JOB = 'px_job'
        SERVER_JOB = 'server_job'
        CONNECTION = 'connection'
        TABLE_DEF = 'table_def'


    class StatusEnum(str, Enum):
        """
        data import status.
        """
        COMPLETED = 'completed'
        IN_PROGRESS = 'in_progress'
        FAILED = 'failed'
        SKIPPED = 'skipped'
        DEPRECATED = 'deprecated'
        UNSUPPORTED = 'unsupported'
        FLOW_CONVERSION_FAILED = 'flow_conversion_failed'
        FLOW_CREATION_FAILED = 'flow_creation_failed'
        FLOW_COMPILATION_FAILED = 'flow_compilation_failed'
        JOB_CREATION_FAILED = 'job_creation_failed'
        JOB_RUN_FAILED = 'job_run_failed'
        CONNECTION_CONVERSION_FAILED = 'connection_conversion_failed'
        CONNECTION_CREATION_FAILED = 'connection_creation_failed'
        PARAMETER_SET_CONVERSION_FAILED = 'parameter_set_conversion_failed'
        PARAMETER_SET_CREATION_FAILED = 'parameter_set_creation_failed'
        TABLE_DEFINITION_CONVERSION_FAILED = 'table_definition_conversion_failed'
        TABLE_DEFINITION_CREATION_FAILED = 'table_definition_creation_failed'


    class TypeEnum(str, Enum):
        """
        type of the job or data connection in the import file.
        """
        PX_JOB = 'px_job'
        SERVER_JOB = 'server_job'
        CONNECTION = 'connection'
        TABLE_DEF = 'table_def'
        PARAMETER_SET = 'parameter_set'
        PX_CONTAINER = 'px_container'
        SEQUENCE_JOB = 'sequence_job'


class ImportFlowWarning():
    """
    An import warning object describe a warning message specific to a particular data
    flow.

    :attr str description: (optional) additional warning text.
    :attr str name: warning object name.
    :attr str type: warning type.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 description: str = None) -> None:
        """
        Initialize a ImportFlowWarning object.

        :param str name: warning object name.
        :param str type: warning type.
        :param str description: (optional) additional warning text.
        """
        self.description = description
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportFlowWarning':
        """Initialize a ImportFlowWarning object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ImportFlowWarning JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ImportFlowWarning JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportFlowWarning object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportFlowWarning object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportFlowWarning') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportFlowWarning') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        warning type.
        """
        UNRELEASED_STAGE_TYPE = 'unreleased_stage_type'
        UNRELEASED_FEATURE = 'unreleased_feature'
        UNSUPPORTED_CREDENTIALS_FILE = 'unsupported_credentials_file'


class ImportResponse():
    """
    Response object of an import request.

    :attr ImportResponseEntity entity: import response entity.
    :attr ImportResponseMetadata metadata: import response metadata.
    """

    def __init__(self,
                 entity: 'ImportResponseEntity',
                 metadata: 'ImportResponseMetadata') -> None:
        """
        Initialize a ImportResponse object.

        :param ImportResponseEntity entity: import response entity.
        :param ImportResponseMetadata metadata: import response metadata.
        """
        self.entity = entity
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportResponse':
        """Initialize a ImportResponse object from a json dictionary."""
        args = {}
        if 'entity' in _dict:
            args['entity'] = ImportResponseEntity.from_dict(_dict.get('entity'))
        else:
            raise ValueError('Required property \'entity\' not present in ImportResponse JSON')
        if 'metadata' in _dict:
            args['metadata'] = ImportResponseMetadata.from_dict(_dict.get('metadata'))
        else:
            raise ValueError('Required property \'metadata\' not present in ImportResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImportResponseEntity():
    """
    import response entity.

    :attr str cancelled_by: (optional) Account ID of the user who cancelled the
          import request. This field is required only when the status  field is
          "cancelled".
    :attr str conflict_resolution: (optional) The conflict_resolution option used
          for the import.
    :attr datetime end_time: (optional) The timestamp when the import opearton
          completed. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching
          the date-time format as specified by RFC 3339.
    :attr List[ImportFlow] import_data_flows: All data flows imported or to be
          imported. Each ImportFlow object contains status for the individual data flow
          import operation.
    :attr str name: (optional) Name of the import request.
    :attr str on_failure: (optional) The on_failure option used for the import.
    :attr int remaining_time: (optional) Estimate of remaining time in seconds.
    :attr datetime start_time: (optional) The timestamp when the import opearton
          started. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching
          the date-time format as specified by RFC 3339.
    :attr str status: import status.
    :attr ImportCount tally: (optional) Import statistics. total = imported
          (including renamed and replaced) + skipped + failed + deprecated + unsupported +
          pending.
    """

    def __init__(self,
                 import_data_flows: List['ImportFlow'],
                 status: str,
                 *,
                 cancelled_by: str = None,
                 conflict_resolution: str = None,
                 end_time: datetime = None,
                 name: str = None,
                 on_failure: str = None,
                 remaining_time: int = None,
                 start_time: datetime = None,
                 tally: 'ImportCount' = None) -> None:
        """
        Initialize a ImportResponseEntity object.

        :param List[ImportFlow] import_data_flows: All data flows imported or to be
               imported. Each ImportFlow object contains status for the individual data
               flow import operation.
        :param str status: import status.
        :param str cancelled_by: (optional) Account ID of the user who cancelled
               the import request. This field is required only when the status  field is
               "cancelled".
        :param str conflict_resolution: (optional) The conflict_resolution option
               used for the import.
        :param datetime end_time: (optional) The timestamp when the import opearton
               completed. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339.
        :param str name: (optional) Name of the import request.
        :param str on_failure: (optional) The on_failure option used for the
               import.
        :param int remaining_time: (optional) Estimate of remaining time in
               seconds.
        :param datetime start_time: (optional) The timestamp when the import
               opearton started. In format YYYY-MM-DDTHH:mm:ssZ or
               YYYY-MM-DDTHH:mm:ss.sssZ, matching the date-time format as specified by RFC
               3339.
        :param ImportCount tally: (optional) Import statistics. total = imported
               (including renamed and replaced) + skipped + failed + deprecated +
               unsupported + pending.
        """
        self.cancelled_by = cancelled_by
        self.conflict_resolution = conflict_resolution
        self.end_time = end_time
        self.import_data_flows = import_data_flows
        self.name = name
        self.on_failure = on_failure
        self.remaining_time = remaining_time
        self.start_time = start_time
        self.status = status
        self.tally = tally

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportResponseEntity':
        """Initialize a ImportResponseEntity object from a json dictionary."""
        args = {}
        if 'cancelled_by' in _dict:
            args['cancelled_by'] = _dict.get('cancelled_by')
        if 'conflict_resolution' in _dict:
            args['conflict_resolution'] = _dict.get('conflict_resolution')
        if 'end_time' in _dict:
            args['end_time'] = string_to_datetime(_dict.get('end_time'))
        if 'import_data_flows' in _dict:
            args['import_data_flows'] = [ImportFlow.from_dict(x) for x in _dict.get('import_data_flows')]
        else:
            raise ValueError('Required property \'import_data_flows\' not present in ImportResponseEntity JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'on_failure' in _dict:
            args['on_failure'] = _dict.get('on_failure')
        if 'remaining_time' in _dict:
            args['remaining_time'] = _dict.get('remaining_time')
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in ImportResponseEntity JSON')
        if 'tally' in _dict:
            args['tally'] = ImportCount.from_dict(_dict.get('tally'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportResponseEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cancelled_by') and self.cancelled_by is not None:
            _dict['cancelled_by'] = self.cancelled_by
        if hasattr(self, 'conflict_resolution') and self.conflict_resolution is not None:
            _dict['conflict_resolution'] = self.conflict_resolution
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = datetime_to_string(self.end_time)
        if hasattr(self, 'import_data_flows') and self.import_data_flows is not None:
            _dict['import_data_flows'] = [x.to_dict() for x in self.import_data_flows]
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'on_failure') and self.on_failure is not None:
            _dict['on_failure'] = self.on_failure
        if hasattr(self, 'remaining_time') and self.remaining_time is not None:
            _dict['remaining_time'] = self.remaining_time
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'tally') and self.tally is not None:
            _dict['tally'] = self.tally.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportResponseEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportResponseEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportResponseEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        import status.
        """
        IN_PROGRESS = 'in_progress'
        CANCELLED = 'cancelled'
        QUEUED = 'queued'
        STARTED = 'started'
        COMPLETED = 'completed'


class ImportResponseMetadata():
    """
    import response metadata.

    :attr str catalog_id: (optional) Catalog id.
    :attr datetime created_at: (optional) The timestamp when the import API was
          submitted. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching
          the date-time format as specified by RFC 3339.
    :attr str created_by: (optional) Account ID of the user who submitted the import
          request.
    :attr str id: The unique import id.
    :attr datetime modified_at: (optional) The timestamp when the import status was
          last updated. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
          matching the date-time format as specified by RFC 3339.
    :attr str name: (optional) import file name.
    :attr str project_id: (optional) Project id.
    :attr str project_name: (optional) Project name.
    :attr str url: The URL which can be used to get the status of the import request
          right after it is submitted.
    """

    def __init__(self,
                 id: str,
                 url: str,
                 *,
                 catalog_id: str = None,
                 created_at: datetime = None,
                 created_by: str = None,
                 modified_at: datetime = None,
                 name: str = None,
                 project_id: str = None,
                 project_name: str = None) -> None:
        """
        Initialize a ImportResponseMetadata object.

        :param str id: The unique import id.
        :param str url: The URL which can be used to get the status of the import
               request right after it is submitted.
        :param str catalog_id: (optional) Catalog id.
        :param datetime created_at: (optional) The timestamp when the import API
               was submitted. In format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ,
               matching the date-time format as specified by RFC 3339.
        :param str created_by: (optional) Account ID of the user who submitted the
               import request.
        :param datetime modified_at: (optional) The timestamp when the import
               status was last updated. In format YYYY-MM-DDTHH:mm:ssZ or
               YYYY-MM-DDTHH:mm:ss.sssZ, matching the date-time format as specified by RFC
               3339.
        :param str name: (optional) import file name.
        :param str project_id: (optional) Project id.
        :param str project_name: (optional) Project name.
        """
        self.catalog_id = catalog_id
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.modified_at = modified_at
        self.name = name
        self.project_id = project_id
        self.project_name = project_name
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportResponseMetadata':
        """Initialize a ImportResponseMetadata object from a json dictionary."""
        args = {}
        if 'catalog_id' in _dict:
            args['catalog_id'] = _dict.get('catalog_id')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ImportResponseMetadata JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        if 'project_name' in _dict:
            args['project_name'] = _dict.get('project_name')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in ImportResponseMetadata JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportResponseMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'catalog_id') and self.catalog_id is not None:
            _dict['catalog_id'] = self.catalog_id
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'project_name') and self.project_name is not None:
            _dict['project_name'] = self.project_name
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportResponseMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportResponseMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportResponseMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineJson():
    """
    Pipeline flow to be stored.

    :attr object app_data: (optional) Object containing app-specific data.
    :attr str doc_type: (optional) The document type.
    :attr List[object] external_paramsets: (optional) Array of parameter set
          references.
    :attr str id: (optional) Document identifier, GUID recommended.
    :attr str json_schema: (optional) Refers to the JSON schema used to validate
          documents of this type.
    :attr object parameters: (optional) Parameters for the flow document.
    :attr List[Pipelines] pipelines: (optional)
    :attr str primary_pipeline: (optional) Reference to the primary (main) pipeline
          flow within the document.
    :attr List[object] runtimes: (optional) Runtime information for pipeline flow.
    :attr List[object] schemas: (optional) Array of data record schemas used in the
          pipeline.
    :attr str version: (optional) Pipeline flow version.
    """

    def __init__(self,
                 *,
                 app_data: object = None,
                 doc_type: str = None,
                 external_paramsets: List[object] = None,
                 id: str = None,
                 json_schema: str = None,
                 parameters: object = None,
                 pipelines: List['Pipelines'] = None,
                 primary_pipeline: str = None,
                 runtimes: List[object] = None,
                 schemas: List[object] = None,
                 version: str = None) -> None:
        """
        Initialize a PipelineJson object.

        :param object app_data: (optional) Object containing app-specific data.
        :param str doc_type: (optional) The document type.
        :param List[object] external_paramsets: (optional) Array of parameter set
               references.
        :param str id: (optional) Document identifier, GUID recommended.
        :param str json_schema: (optional) Refers to the JSON schema used to
               validate documents of this type.
        :param object parameters: (optional) Parameters for the flow document.
        :param List[Pipelines] pipelines: (optional)
        :param str primary_pipeline: (optional) Reference to the primary (main)
               pipeline flow within the document.
        :param List[object] runtimes: (optional) Runtime information for pipeline
               flow.
        :param List[object] schemas: (optional) Array of data record schemas used
               in the pipeline.
        :param str version: (optional) Pipeline flow version.
        """
        self.app_data = app_data
        self.doc_type = doc_type
        self.external_paramsets = external_paramsets
        self.id = id
        self.json_schema = json_schema
        self.parameters = parameters
        self.pipelines = pipelines
        self.primary_pipeline = primary_pipeline
        self.runtimes = runtimes
        self.schemas = schemas
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineJson':
        """Initialize a PipelineJson object from a json dictionary."""
        args = {}
        if 'app_data' in _dict:
            args['app_data'] = _dict.get('app_data')
        if 'doc_type' in _dict:
            args['doc_type'] = _dict.get('doc_type')
        if 'external_paramsets' in _dict:
            args['external_paramsets'] = _dict.get('external_paramsets')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'json_schema' in _dict:
            args['json_schema'] = _dict.get('json_schema')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        if 'pipelines' in _dict:
            args['pipelines'] = [Pipelines.from_dict(x) for x in _dict.get('pipelines')]
        if 'primary_pipeline' in _dict:
            args['primary_pipeline'] = _dict.get('primary_pipeline')
        if 'runtimes' in _dict:
            args['runtimes'] = _dict.get('runtimes')
        if 'schemas' in _dict:
            args['schemas'] = _dict.get('schemas')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineJson object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'app_data') and self.app_data is not None:
            _dict['app_data'] = self.app_data
        if hasattr(self, 'doc_type') and self.doc_type is not None:
            _dict['doc_type'] = self.doc_type
        if hasattr(self, 'external_paramsets') and self.external_paramsets is not None:
            _dict['external_paramsets'] = self.external_paramsets
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'json_schema') and self.json_schema is not None:
            _dict['json_schema'] = self.json_schema
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'pipelines') and self.pipelines is not None:
            _dict['pipelines'] = [x.to_dict() for x in self.pipelines]
        if hasattr(self, 'primary_pipeline') and self.primary_pipeline is not None:
            _dict['primary_pipeline'] = self.primary_pipeline
        if hasattr(self, 'runtimes') and self.runtimes is not None:
            _dict['runtimes'] = self.runtimes
        if hasattr(self, 'schemas') and self.schemas is not None:
            _dict['schemas'] = self.schemas
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineJson object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineJson') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineJson') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Pipelines():
    """
    Pipelines.

    :attr object app_data: (optional) Object containing app-specific data.
    :attr str description: (optional) A brief description of the DataStage flow.
    :attr str id: (optional) Unique identifier.
    :attr List[object] nodes: (optional) Array of pipeline nodes.
    :attr str runtime_ref: (optional) Reference to the runtime type.
    """

    def __init__(self,
                 *,
                 app_data: object = None,
                 description: str = None,
                 id: str = None,
                 nodes: List[object] = None,
                 runtime_ref: str = None) -> None:
        """
        Initialize a Pipelines object.

        :param object app_data: (optional) Object containing app-specific data.
        :param str description: (optional) A brief description of the DataStage
               flow.
        :param str id: (optional) Unique identifier.
        :param List[object] nodes: (optional) Array of pipeline nodes.
        :param str runtime_ref: (optional) Reference to the runtime type.
        """
        self.app_data = app_data
        self.description = description
        self.id = id
        self.nodes = nodes
        self.runtime_ref = runtime_ref

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pipelines':
        """Initialize a Pipelines object from a json dictionary."""
        args = {}
        if 'app_data' in _dict:
            args['app_data'] = _dict.get('app_data')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'nodes' in _dict:
            args['nodes'] = _dict.get('nodes')
        if 'runtime_ref' in _dict:
            args['runtime_ref'] = _dict.get('runtime_ref')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pipelines object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'app_data') and self.app_data is not None:
            _dict['app_data'] = self.app_data
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'nodes') and self.nodes is not None:
            _dict['nodes'] = self.nodes
        if hasattr(self, 'runtime_ref') and self.runtime_ref is not None:
            _dict['runtime_ref'] = self.runtime_ref
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pipelines object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pipelines') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pipelines') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
