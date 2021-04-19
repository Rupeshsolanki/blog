# blog
blog site to connect college Alumni to students

## Containerize Django application ##
Application is written in Django and there is one Dockerfile where instractions are given to build the image,
      To create image form that Dockerfile use commands
```sh
docker-compose build -t blog .

docker run --name <container-name> -itd -p 8000:8000 blog
```
By using the above command container will run on port 8000.

## Tag docker image and push it to Docker Hub ##

```sh
docker tag blog <docker-hub-username>/blog

docker login

docker push <docker-hub-username>/blog
```

## Now docker images is available publically, anyone can use this image by running the following command:

```sh
docker run -itd --name <container-name> -p 8000:8000 <docker-hub-username>/blog
```

## To run pods in OpenShift using this image use following commands ##

```sh
oc new-project my-project
```
```sh
oc new-app --name blog --docker-image=rupeshsolanki/blog
```
```sh
oc expose dc blog --port=8000
```
```sh
 oc expose svc blog --port=8000
 ```
