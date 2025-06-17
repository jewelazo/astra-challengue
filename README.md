# Astra Challengue

## Installation

### Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/jewelazo/astra-challengue.git
   cd astra-challengue
   ```

2. Create `.env` file:
   ```bash
   cp .env.example .env
   ```

3. Build and run with Docker:
   ```bash
   docker compose up --build
   ```
4. Execute:
    ```bash
    # Apply database migrations
    docker compose exec web python manage.py migrate

    # Load initial data
    docker compose exec web python manage.py loaddata load_data.json 
    
    The application will be available at: `http://localhost:8000`

    # You can run unitests
    docker compose exec web python manage.py test apps.blog

    ```

### Without Docker

1. Create a new directory.
2. Open your favourite IDE and then open your directory. 
3. Open the terminal in working directory:
4. Clone this repository:
```
           git clone https://github.com/jewelazo/astra-challengue.git
```
5) Create a virtual environmnent:
```
            python -m venv .venv
```
6) Activate the virtual environment:
```
            .\.venv\Scripts\activate
```
7) Create your postgresql database and add its values in your .env file, please follow .env.example as template:

8) Install libraries:
```
            (env) pip install -r requirements.txt
```
9) Run Migrations:
```
            (env) python manage.py migrate
```
10) Go to project folder and run this command:
```
            (env) python manage.py runserver
```
11) Run unitests
```
            (env) python manage.py test apps.blog
```
# Debugging
```
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('title', instance.title)
        instance.save()
        return instance
```

- Solution:
```
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value

    def update(self, instance, validated_data):
        # The Post model has a field named 'title', not 'titulo'.
        # Add more fields to update
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
```

## API Endpoints 

You can test the API using [Postman](https://www.postman.com/) or any REST client.

- POST {{base_url}}/api/posts/               # Create post
- GET  {{base_url}}/api/posts/               # Get all posts
- GET  {{base_url}}/api/posts/{id}/          # Get post by id
- PUT  {{base_url}}/api/posts/{id}/          # Update post by id (replace)
- PATCH {{base_url}}/api/posts/{id}/         # Partial update post by id
- DELETE {{base_url}}/api/posts/{id}/        # Delete post by id
- GET {{base_url}}/api/project/{id}/         # Get project detail
- GET {{base_url}}/api/tasks/{id}/           # Get task detail
- GET {{base_url}}/api/tasks/                # Get all tasks



##  Updates coming soon ...

📄 Add API documentation with Swagger/OpenAPI

💾 Add user authentication and authorization
