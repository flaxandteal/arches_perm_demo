import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches_perm_demo"), "arches_perm_demo.urls", name="arches_perm_demo"),
)
