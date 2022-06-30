import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='abc@123')


# print(server.get_views())

# server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
# view_config = server.get_view_config('EMPTY')
# views = server.get_views()
# server.delete_view('EMPTY')
# print(views)

_nameApp = 'job1-test'

jobs = server.get_all_jobs()
print(jobs[0])
for _app in jobs[0]:
    print(_app)
    # if not _nameApp == _app.get('name'):      
    #     server.create_job('folder', jenkins.EMPTY_FOLDER_XML)
    #     server.create_job('folder/{0}'.format(_nameApp), jenkins.EMPTY_CONFIG_XML)


# server.build_job('folder/job1-test')
# queue_info = server.get_queue_info()
# id = queue_info[0].get('id')
# server.cancel_queue(id)

# # server.create_job('folder/empty', jenkins.EMPTY_FOLDER_XML)
# # server.copy_job('job1-test', 'folder/')
# # server.delete_job('folder/empty_copy')
# # server.delete_job('folder')

# # server.delete_job('job1-test')
# # server.delete_job('folder')