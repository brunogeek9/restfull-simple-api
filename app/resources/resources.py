from flask_restful import Resource

tasks = []

class TaskResource(Resource):
    def post(self,title):
        task = {'title':title}
        tasks.append(task)
        return task

    def get(self,title):
        for task in tasks:
            if task['title']:
                return task
        
        return {'title': None}

class AllTasks(Resource):
    def get(self):
        return {'tasks': tasks}
         
