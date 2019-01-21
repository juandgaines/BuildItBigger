# -*- coding: utf-8 -*- #
# Copyright 2018 Google Inc. All Rights Reserved.
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
"""Command to export files into a Cloud Composer environment's bucket."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import posixpath

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.composer import flags
from googlecloudsdk.command_lib.composer import resource_args
from googlecloudsdk.command_lib.composer import storage_util


class Export(base.Command):
  """Export data from an environment into local storage or Cloud Storage.

  If the SOURCE is a directory, it and its contents are are exported
  recursively. If no SOURCE is provided, the entire contents of the
  environment's data directory will be exported. Colliding files in the
  DESTINATION will be overwritten. If a file exists in the DESTINATION but
  there is no corresponding file to overwrite it, it is untouched.

  ## EXAMPLES
  Suppose the environment `myenv`'s Cloud Storage bucket has the following
  structure:

    gs://the-bucket
    |
    +-- data
    |   |
    |   +-- file1.txt
    |   +-- file2.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- file4.txt

  And the local directory '/foo' has the following
  structure:

    /foo
    |
    +-- file1.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- fileY.txt

  The following command:

    {command} myenv --destination /foo

  would result in the following structure in the local '/foo' directory:

    /foo
    |
    +-- file1.txt
    +-- file2.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- file4.txt
    |   |   +-- fileY.txt

  The local files '/foo/file1.txt' and '/foo/subdir1/file3.txt' will be
  overwritten with the contents of the corresponding files in the Cloud Storage
  bucket.

  If instead we had run

    {command} myenv --source subdir1/file3.txt --destination /foo

  the resulting local directory structure would be the following:

    /foo
    |
    +-- file1.txt
    +-- file3.txt
    +-- fileX.txt
    |   |
    |   +-- subdir1
    |   |   |
    |   |   +-- file3.txt
    |   |   +-- fileY.txt

  No local files would be overwritten since
  'gs://the-bucket/dags/subdir1/file3.txt' was written to '/foo/file3.txt'
  instead of 'foo/subdir1/file3.txt'.
  """

  SUBDIR_BASE = 'data'

  @staticmethod
  def Args(parser):
    resource_args.AddEnvironmentResourceArg(
        parser, 'from whose Cloud Storage bucket to export data.',
        positional=False)
    flags.AddExportSourceFlag(parser, Export.SUBDIR_BASE)
    flags.AddExportDestinationFlag(parser)

  def Run(self, args):
    storage_util.WarnIfWildcardIsPresent(args.source, '--source')
    env_ref = args.CONCEPTS.environment.Parse()
    source_path = posixpath.join(Export.SUBDIR_BASE,
                                 (args.source or '*').strip(posixpath.sep))
    return storage_util.Export(
        env_ref, source_path,
        args.destination,
        release_track=self.ReleaseTrack())
