import gearman

gm_client = gearman.GearmanClient(['localhost:4730'])
submitted_job_request = gm_client.submit_job("zsl-gearman-task", "{}", priority=gearman.PRIORITY_HIGH, background=True)

check_request_status(submitted_job_request)
