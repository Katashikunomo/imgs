import base64
import PyPDF2

# Tu cadena codificada en base64
base64_data = "JVBERi0xLjQKJdP0zOEKMSAwIG9iago8PAovQ3JlYXRpb25EYXRlKEQ6MjAyNDAxMTcyMjQxNTYrMDAnMDAnKQovQ3JlYXRvcihQREZTaGFycCAxLjUxLjUxODUgXCh3d3cucGRmc2hhcnAuY29tXCkpCi9Qcm9kdWNlcihQREZTaGFycCAxLjUxLjUxODUgXCh3d3cucGRmc2hhcnAuY29tXCkpCj4+CmVuZG9iagoyIDAgb2JqCjw8Ci9UeXBlL0NhdGFsb2cKL1BhZ2VzIDMgMCBSCi9NZXRhZGF0YSAxMiAwIFIKPj4KZW5kb2JqCjMgMCBvYmoKPDwKL1R5cGUvUGFnZXMKL0NvdW50IDEKL0tpZHNbNCAwIFJdCj4+CmVuZG9iago0IDAgb2JqCjw8Ci9UeXBlL1BhZ2UKL01lZGlhQm94WzAgMCA1OTUgODQyXQovUGFyZW50IDMgMCBSCi9Db250ZW50cyA1IDAgUgovUmVzb3VyY2VzCjw8Ci9Qcm9jU2V0IFsvUERGL1RleHQvSW1hZ2VCL0ltYWdlQy9JbWFnZUldCi9FeHRHU3RhdGUKPDwKL0dTMCA2IDAgUgo+PgovRm9udAo8PAovRjAgMTAgMCBSCj4+Cj4+Ci9Hcm91cAo8PAovQ1MvRGV2aWNlUkdCCi9TL1RyYW5zcGFyZW5jeQo+Pgo+PgplbmRvYmoKNSAwIG9iago8PAovTGVuZ3RoIDE1OAovRmlsdGVyL0ZsYXRlRGVjb2RlCj4+CnN0cmVhbQp4nE2OwQrCMAyG73mKnD10ada0GYiHifMsFnwBcSJTmL4/GDMGUvr/H+QLZIYZCDUxPkE6cZqcyJo873DZ4MtENpPdLOI0OfFPsuA/ua9AIWtGConUMmbB9wjN8Uw4fqAZzOcgWG+2yoFLLhhVQ1u0YL3ilogTURrsK5H01nvrvMP6gMwhpq7YeYvako1XvVtY1o6+cqhw8vcFetQxggplbmRzdHJlYW0KZW5kb2JqCjYgMCBvYmoKPDwKL1R5cGUvRXh0R1N0YXRlCi9jYSAxCj4+CmVuZG9iago3IDAgb2JqCjw8Ci9UeXBlL0ZvbnREZXNjcmlwdG9yCi9Bc2NlbnQgOTE3Ci9DYXBIZWlnaHQgOTE3Ci9EZXNjZW50IDIxNwovRmxhZ3MgMzIKL0ZvbnRCQm94Wy0yMTUgLTMwNyAxMDkzIDk1Ml0KL0l0YWxpY0FuZ2xlIDAKL1N0ZW1WIDAKL1hIZWlnaHQgNjA0Ci9Gb250"
