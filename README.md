# Astra Challengue

# Getting Started
1) Create a new directory.
2) Open your favourite IDE and then open your directory. 
3) Open the terminal in working directory:
4) Clone this repository:
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
9) Create your .env file:
```
            (env) cp .env.example .env
```
10) Run Migrations:
```
            (env) python manage.py migrate
```
11) Go to project folder and run this command:
```
            (env) python manage.py runserver
```
12) Run unitests
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
        # This method is redundant since ModelSerializer already implements it by default.
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # The Post model has a field named 'title', not 'titulo'.
        instance.titulo = validated_data.get('title', instance.title) # Post model has field title and not titulo
        instance.save()
        return instance
```