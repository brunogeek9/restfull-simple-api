from flask_restful import Resource, reqparse
from app.models.tables import Book
books = []
tasks = []
parser = reqparse.RequestParser()

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

class BookResource(Resource):
    def get(self):
        return {books, True}
    
    def post(self)
        parser.add_argument('title',type=str)
        parser.add_argument('n_pages',type=int)
        parser.add_argument('rate',type=float)
        args = parser.parse_args()
        print(args)
        books.append(args)
        return {
            'status': True
            'data': 'book {} added'.format(args['title']) 
        }

    def put(self):
        parser.add_argument('title',type=str)
        parser.add_argument('n_pages',type=int)
        parser.add_argument('rate',type=float)
        args = parser.parse_args()
        for book in books:
            if book['title'] == title
                #books['n_pages'] =
                book['n_pages'] = args['n_pages']
                return {
                    'status': True
                    'data': 'book {} updated'.format(args['title']) 
                }
        return {'message': 'data not'}, 400
         
