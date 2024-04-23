# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * Pants cannot yet infer dependencies on `resource` / `resources` targets, so we explicitly add
#   the dep.
python_sources(
    name="lib",
)

python_google_cloud_function(
    name="test",
    runtime="python312",
    handler="greeting.py:handle_query",
    type="event",
)
