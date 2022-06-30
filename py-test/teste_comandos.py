import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='abc@123')

# #################################
print('Jobs: {0}'.format(server.jobs_count()))

# #################################
jobs = server.get_all_jobs(folder_depth=None)
for job in jobs:
   print(job['fullname'])

# #################################
server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)

my_job = server.get_job_config('cool-job')
print(my_job) # prints XML configuration
server.build_job('empty')
server.disable_job('empty')
server.copy_job('empty', 'empty_copy')
server.enable_job('empty_copy')
server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

server.delete_job('empty')
server.delete_job('empty_copy')

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print(build_info)

# get all jobs from the specific view
jobs = server.ge

# ###################################
server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
view_config = server.get_view_config('EMPTY')
views = server.get_views()
server.delete_view('EMPTY')
print( views)