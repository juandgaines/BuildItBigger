# -*- coding: utf-8 -*- #
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Get IAM workflow template policy command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataproc import dataproc as dp
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc import flags


@base.ReleaseTracks(base.ReleaseTrack.GA)
class GetIamPolicy(base.ListCommand):
  """Get IAM policy for a workflow template.

  Gets the IAM policy for a workflow template, given a template ID.

  ## EXAMPLES

  The following command prints the IAM policy for a workflow template with the
  ID `example-workflow`:

    $ {command} example-workflow
  """

  @staticmethod
  def Args(parser):
    flags.AddTemplateResourceArg(
        parser, 'retrieve the policy for', api_version='v1')
    base.URI_FLAG.RemoveFromParser(parser)

  def Run(self, args):
    dataproc = dp.Dataproc(self.ReleaseTrack())
    msgs = dataproc.messages

    template_ref = args.CONCEPTS.template.Parse()
    request = msgs.DataprocProjectsRegionsWorkflowTemplatesGetIamPolicyRequest(
        resource=template_ref.RelativeName())

    return dataproc.client.projects_regions_workflowTemplates.GetIamPolicy(
        request)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class GetIamPolicyBeta(GetIamPolicy):
  """Get IAM policy for a workflow template.

  Gets the IAM policy for a workflow template, given a template ID.

  ## EXAMPLES

  The following command prints the IAM policy for a workflow template with the
  ID `example-workflow`:

    $ {command} example-workflow
  """

  @staticmethod
  def Args(parser):
    flags.AddTemplateResourceArg(
        parser, 'retrieve the policy for', api_version='v1beta2')
    base.URI_FLAG.RemoveFromParser(parser)
